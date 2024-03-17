# school_management

admin credentials:- 
{
    phone: admin,
    password: 123
}


1. Create form view to Add Class

        API endpoint : 
        http://127.0.0.1:8000/add-class/

        No authentication added:

        accepter params json data:- {"class_name":"add your class name here( i have added first, secound, third )"}


2. Register Student and select class from dropdown

        asked for dropdown so crated a template based registration.

        url:- http://127.0.0.1:8000/register-student/


3. Create Login for Student

        API endpoint : 
        http://127.0.0.1:8000/student-login/

        accepter params json data:- {"phone_number":"user phone no.","password":"user password"}

        dummy data = {"phone_number":"123","password":"123"}

        after login token will be provided


4. Student can update profile like image and other fields

        http://127.0.0.1:8000/update-profile/

        TokenAuthentication and IsAuthenticated permission added
        
        autherization should be added on header with params:- Authorization Token {add your token here}

        dummy data:- {"first_name":"manmohan",
                       "last_name":"singh",
                       "email":"manurawat771998@gmail.com",
                       "date_of_birth":"1998-07-07",
                       "image":"data:image/jpeg;base64,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"
                    }


5. Activate Deactivate Student from admin

    this can be done through admin pannel credential are at top of the document.



Thank You!
