from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
import uuid
import random
import string

import fpdf
from fpdf import FPDF, HTMLMixin

from django.http import HttpResponse
from django.template.loader import render_to_string
# from weasyprint import HTML

# from io import BytesIO
# from django.template.loader import get_template
# from xhtml2pdf import pisa

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import pdfkit
config = pdfkit.configuration(wkhtmltopdf=r"C:\Users\AUO\Downloads\wkhtmltox-0.12.6-1.msvc2015-win64.exe")

current_academic_session = "2025/2026"
current_academic_semester = "second"


def generate_pdf(reg_course, student, session, semester):
    class PDF(FPDF, HTMLMixin):
        def header(self):
            # logo
            self.image('achieverslogo.png', 10, 4, 20)
            # font
            self.set_font('helvetica', 'B', 14)
            # padding
            # self.cell(0)
            #Title
            self.cell(170,  0, 'ACHIEVERS UNIVERSITY, OWO', border=False, ln=1, align='C')
            # line break
            self.ln(1)

            self.set_font('helvetica', 'B', 10)
            # padding
            # self.cell(75)
            #Title
            self.cell(170,  7, 'Owo, Ondo State, Nigeria Website: www.achievers.edu.ng', border=False, ln=1, align='C')
            self.ln(1)

            self.set_font('helvetica', 'B', 11)
            # padding
            # self.cell(75)
            #Title
            self.cell(170,  5, 'UNDERGRADUATE PROGRAMME', border=False, ln=1, align='C')
            self.ln(1)

            self.set_font('helvetica', 'B', 10)
            # padding
            # self.cell(75)
            #Title
            self.cell(170,  5, f'COURSE REGISTRATION FORM', border=False, ln=1, align='C')
            self.ln(1)
            # logo
            self.image('achieverslogo.png', 170, 4, 23)

    pdf = PDF('P', 'mm', 'Letter')

    #set auto page break
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    
    pdf.ln()


    pdf.set_font('times', 'B', 6)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(129, 4, f"Printed on: Monday 14th October 2024 || 12:06PM")


    pdf.set_font('times', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 4, f" {session} || {semester} SEMESTER", ln=True)




    pdf.set_font('times', 'B', 10)
    pdf.set_fill_color(6, 75, 37)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(180, 7, f"   :. Students' Personal Information", ln=True, fill=True, align='L')

    pdf.set_font('helvetica', 'BIU', 13)
    pdf.set_font('times', 'B', 7)

    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'FUll NAME:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.surname}, {student.otherNames}', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'MATRIC NO / JAMB NO:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.matricNumber} [95753342EC]', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'FACULTY:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'Science', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'PROGRAMME:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.programme}', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'DEGREE:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'B.SC. INDUSTRIAL CHEMISTRY', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'EMAIL / PHONE NO:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'ONI.ADURAGBEMI.191131@FUOYE.EDU.NG || 07039300133, 07058381197', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'CURRENT LEVEL:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'200', )
    pdf.image('profile_pic.jpg', 170, 50, 23)

    pdf.ln()

    # pdf.cell(100, 10, 'Title', border=0, fill=True)
    # pdf.cell(15, 10, 'Unit', border=0, fill=True)

    # pdf.set_font('Arial', 'B', 8)
    # pdf.set_fill_color(0, 0, 0)
    # pdf.set_text_color(255, 255, 255)
    # pdf.cell(25, 8, 'Code', border=1, fill=True)
    # pdf.cell(100, 8, 'Title', border=1, fill=True)
    # pdf.cell(15, 8, 'Unit', border=1, fill=True)
    # pdf.cell(15, 8, 'Status', border=1, fill=True)
    # pdf.cell(30, 8, 'Signature', border=1, fill=True)
    # pdf.ln()

    # Add table rows with padding and borders
    pdf.set_font('Arial', 'B', 6)
    pdf.set_text_color(0, 0, 0)
    for row in range(15):
        pdf.cell(25, 4, f'CHM 201', border=1)
        pdf.cell(100, 4, f'Introduction to chemistry', border=1)
        pdf.cell(15, 4, f'3', border=1)
        pdf.cell(15, 4, f'C', border=1)
        pdf.cell(30, 4, f'', border=1)
        pdf.ln()

    pdf.set_font('Arial', 'B', 6)
    pdf.cell(25, 4, f'', border=1)
    pdf.cell(100, 4, f'Total Registered Units', border=1)
    pdf.cell(15, 4, f'24', border=1)
    pdf.cell(15, 4, f'', border=1)
    pdf.cell(30, 4, f'', border=1)
    pdf.ln()






    pdf.set_font('helvetica', 'BIU', 16)
    pdf.set_font('times', '', 9)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'Key: C=Core, E=Elective, R=Required', ln=True)

    pdf.ln(4)

    pdf.set_font('helvetica', 'BIU', 16)
    pdf.set_font('times', '', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(145, 7, f'Signature of Student: _____________________________________')
    pdf.cell(0, 7, f'Date: __________________________', ln=True)



    pdf.set_font('times', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(180, 7, f'FOR OFFICIAL USE ONLY', align='C', ln=True)






    pdf.set_font('times', 'B', 6)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(180, 2, f'I certify that the above named student has submitted four(4) copies of his/her first semester course registration form and he/she is qualified to register the above listed courses', align='C', ln=True)

    pdf.ln(6)

    pdf.set_font('helvetica', 'BIU', 16)
    pdf.set_font('times', '', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(145, 7, f'Signature of Academic Advisor: ____________________________')
    pdf.cell(0, 7, f'Date: __________________________', ln=True)
    pdf.ln(6)

    pdf.set_font('helvetica', 'BIU', 16)
    pdf.set_font('times', '', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(145, 7, f'Signature of H.O.D.: _____________________________________')
    pdf.cell(0, 7, f'Date: __________________________', ln=True)
    pdf.ln(6)

    pdf.set_font('helvetica', 'BIU', 16)
    pdf.set_font('times', '', 7)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(145, 7, f'Signature of DEAN: _____________________________________')
    pdf.cell(0, 7, f'Date: __________________________', ln=True)

    pdf.ln(3)

    pdf.set_font('times', 'B', 6)
    pdf.set_text_color(255, 0, 0)
    pdf.cell(180, 2, f'Note:This form should be printed and returned to the Examination Officer at least Four weeks before the commencement of the examinations.', align='C', ln=True)
    pdf.cell(180, 2, f'No Candidate shall be allowed to write any \nexamination in any course unless he/she has satisfied appropriate registration & finanacial regulations.', align='C')


    response = HttpResponse(pdf.output(dest='S').encode('latin1'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="fpdfdemo.pdf"'
    return response
    # for i in range (1, 41):
    #     pdf.cell(0, 10, f'This is line {i} :D', ln=True)
    # pdf.output('fpdfdemo.pdf', 'F')


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
def startReg(request):
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
            return render(request, 'reg.html', {'student':student, 'sess': current_academic_session, 'semes': current_academic_semester, 'exist': 'true'})
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

    return render(request, 'reg.html', {'student':student, 'sess': '2024/2025', 'semes': 'first'})

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

@login_required
def printCopy(request):
    if request.user.is_authenticated:
        user = request.user
        student = get_object_or_404(Student, user=user)
    sess = "2024/2025"
    semes = "first"

    reg_courses = Registration.objects.filter(
                student=student,
                semester=get_object_or_404(Semester, name=semes),
                session=get_object_or_404(Session, year=sess)
            )
    
    if request.method == 'POST':
        reg_courses = Registration.objects.filter(
                student=student,
                semester=get_object_or_404(Semester, name=semes),
                session=get_object_or_404(Session, year=sess)
            )
        
        generate_pdf(reg_courses, student, '2024/2025', 'first')


    return render(request, 'printCopy.html', {'courses': reg_courses,'student':student, 'sess': '2024/2025', 'semes': 'first'})

# def generatePDF(request):
    # pdf = pdfkit.from_url(request.build_absolute_uri('/print'), False, configuration=config)
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="file_name.pdf"'

    # html_string = render_to_string('template.html', {'data': 'Some context data'})
    # html = HTML(string=html_string)
    # pdf = html.write_pdf()

    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    pdf = render_to_pdf('printCopy.html')

    return HttpResponse(pdf, content_type='application/pdf')

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