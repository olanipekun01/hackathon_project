from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
import uuid
import random
import string

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

current_academic_session = "2025/2026"
current_academic_semester = "second"

def generate_password(length=8):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


def is_student_registered_for_semester(student, semester, session):
    """
    Check if a student is registered for a specific semester in a session.
    :param student: The student instance
    :param semester: The semester to check (e.g., 'First', 'Second')
    :param session: The session instance (e.g., '2023/2024')
    :return: True if registered, False otherwise
    """
    return Registration.objects.filter(
        student=student, 
        semester=semester, 
        session=session
    ).exists()


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# Create your views here.
@login_required
def index(request):
    print('user', request.user)
    if request.user.is_authenticated:
        user = request.user
        student = get_object_or_404(Student, user=user) 
        print("student", student)
    if request.method == "POST":
        # user = CustomUser.objects.get(email='otelo@au.com')
        sess = request.POST["session"]
        semes = request.POST["semester"]
        # print('session', session)
        # print('session', semester)
        stud = student
        curr_session = get_object_or_404(Session, year=sess)
        semester = get_object_or_404(Semester, name=semes)
        is_registered = is_student_registered_for_semester(stud, semester, curr_session)
        if is_registered:
            return render(request, 'index.html', {'student':student, 'sess': current_academic_session, 'semes': current_academic_semester, 'exist': 'true'})
        # student = get_object_or_404(Student, user=user) 
        semester = get_object_or_404(Semester, name=semester)
        level = get_object_or_404(Level, name=student.level)
        courses = Course.objects.filter(
            level=level,
            programmes=student.programme,
            semester=semester
        )
        carryover_courses = Registration.objects.filter(student=student, semester=get_object_or_404(Semester, name=semes), passed=False, carried_over=True)
        # print('carryover courses',carryover_courses)
        # print('user', user.id)
        # print('student', student)
        # print('courses', courses)
        return render(request, 'coursemain.html', {'courses': courses, 'student':student, 'sess': curr_session, 'semes': semester,'carryover': carryover_courses })

    return render(request, 'index.html', {'student':student, 'sess': '2024/2025', 'semes': 'first'})

@login_required
def courseMain(request):
    if request.user.is_authenticated:
        user = request.user
        student = get_object_or_404(Student, user=user) 
    if request.method == 'POST':
        # student
        courses = request.POST.getlist('courses')  # Assuming departments are selected in a form
        sess = request.POST["sess"]
        semes= request.POST["semes"]
        # print("sess", session, "semes", semester)
        for id in courses:
            print('course id', id)
            # course = get_object_or_404(Course, id=id)
            # Registration.dept.add(department)
            # registration = Registration.objects.create(student = student,
            #                                  course=get_object_or_404(Course, id=id),
            #                                  session = get_object_or_404(Session, year="2024/2025"),
            #                                  semester = get_object_or_404(Semester, name="first"),
            #                                 )
            # registration.save()
            course=get_object_or_404(Course, id=id),
            print('course name', course)
            semester = get_object_or_404(Semester, name=semes)
            
            course_exist = Registration.objects.filter(
                student=student,
                course=get_object_or_404(Course, id=id),
                semester=semester
            ).first()

            print('course exist', course_exist)

            if course_exist:
                # course_exist = Registration.objects.filter(
                #     student=student,
                #     semester=semester,
                #     course=course
                # )
                print('yes it exist')
                # If the registration already exists, update the session and semester
                course_exist.session = get_object_or_404(Session, year=sess)
                # registration.semester = semester
                course_exist.save()
            else:
                course_exist = Registration.objects.create(
                    student=student,
                    course=get_object_or_404(Course, id=id),
                    session = get_object_or_404(Session, year=sess), 
                    semester = get_object_or_404(Semester, name=semes)
                )
                course_exist.save()
        return redirect('/')
        
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
            user = auth.authenticate(username=email, password=password)
            # user = User.objects.get(email=email)
            # if user.check_password(password):
            #     # Log the user in (assuming you're using Django's session framework)
            #     # login(request, user)
            #     return redirect('/')  # Redirect to the dashboard or homepage
            # else:
            #     error_message = "Invalid password."
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                error_message = "User does not exist."
                return redirect('/accounts/login')
        except User.DoesNotExist:
            error_message = "User does not exist."
            return redirect('/accounts/login')

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