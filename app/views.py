from django.shortcuts import render,redirect, get_object_or_404
from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
import uuid

# Create your views here.
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