from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .forms import *
from .models import *
from .serialzer import *

@api_view(['POST'])
def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.data)
        print(form)
        if form.is_valid():
            form.save()
            return Response({'message': 'Class added successfully'}, status=201)
        else:
            return Response(form.errors, status=400)
    else:
        return Response({'message': 'Only POST requests are allowed'}, status=405)


def register_student(request):
    student_class = Class.objects.all()
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        pimage = request.FILES.get('pimage')
        selected_class = request.POST.get('class')
        print('image',pimage)
        try:
            StudentUser.objects.create_user(phone=phone, password=password)
            
            new_object = StudentProfile(
                user=StudentUser.objects.get(phone=phone),
                first_name=fname,
                last_name=lname,
                email=email,
                date_of_birth=dob,
                image=pimage,
                student_class=Class.objects.get(class_name=selected_class)
            )

            # Save the object to the database
            new_object.save()
            return HttpResponse('You have Registered Sucessfully!! <br> <a href="/student-login/">login</a>')
        except:
            return redirect('/register-student/')
    return render(request, 'registration.html', {'class': student_class})


@api_view(['POST'])
def student_login(request):
    form = LoginForm(request.data)
    if form.is_valid():
        phone_number = form.cleaned_data['phone_number']
        password = form.cleaned_data['password']
        user_status = StudentProfile.objects.get(user=StudentUser.objects.get(phone=phone_number)).status
        if user_status == False:
            return Response({'error': 'status is not active, please connect with admin!'}, status=status.HTTP_403_FORBIDDEN)
        else:
            user = authenticate(phone=phone_number, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)
    else:
        return Response({'error': 'Invalid form data'}, status=400)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_student_profile(request):
    print(request.data)
    try:
        profile = request.user.profile
    except StudentProfile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = StudentProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)