from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
import uuid
import random
import string

def generate_password(length=8):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        user = User.objects.get(email='otelo@au.com')
        student = get_object_or_404(Student, user=user)
        semester = get_object_or_404(Semester, name='first')
        level = get_object_or_404(Level, name=student.level)
        courses = Course.objects.filter(
            level=level,
            programmes=student.programme,
            semester=semester
        )
        print('user', user.id)
        print('student', student)
        print('courses', courses)
        return render(request, 'coursemain.html', {'courses': courses, 'student':student, 'sess': '2024/2025', 'semes': 'first'})

    return render(request, 'index.html')


def courseMain(request):
    return render(request, 'coursemain.html')

def register(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()  # Save the user instance
            user_type = user.user_type
            
            if user_type == 'student':
                student_form = StudentSignupForm(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user  # Link student to user
                    student.save()
            elif user_type == 'instructor':
                instructor_form = InstructorSignupForm(request.POST)
                if instructor_form.is_valid():
                    instructor = instructor_form.save(commit=False)
                    instructor.user = user  # Link instructor to user
                    instructor.save()
            
            return redirect('success_page')  # Redirect to success page after signup
    else:
        user_form = UserSignupForm()
        student_form = StudentSignupForm()
        instructor_form = InstructorSignupForm()
    
    return render(request, 'signup.html', {
        'user_form': user_form,
        'student_form': student_form,
        'instructor_form': instructor_form,
    })
    
    
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                # Log the user in (assuming you're using Django's session framework)
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard or homepage
            else:
                error_message = "Invalid password."
        except User.DoesNotExist:
            error_message = "User does not exist."

        return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')

def change_password_view(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        
        user = request.user

        if user.check_password(old_password):
            user.set_password(new_password)
            return redirect('password_changed_success')
        else:
            error_message = "Incorrect old password."
            return render(request, 'change_password.html', {'error': error_message})

    return render(request, 'change_password.html')