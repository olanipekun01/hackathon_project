from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import *
import uuid
import random
import string

import os

import fpdf
from fpdf import FPDF, HTMLMixin

from django.http import HttpResponse
from django.template.loader import render_to_string
# from weasyprint import HTML

# from io import BytesIO
# from django.template.loader import get_template
# from xhtml2pdf import pisa

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict


from django.contrib import messages

UserModel = get_user_model()

# import pdfkit
# config = pdfkit.configuration(wkhtmltopdf=r"C:\Users\AUO\Downloads\wkhtmltox-0.12.6-1.msvc2015-win64.exe")

current_academic_session = "2025/2026"
current_academic_semester = "second"

# Helper functions for role checks
def is_student(user):
    # print("User", User.role)
    return user.user_type == 'student'
    # return True

def is_instructor(user):
    return user.user_type == 'instructor'


def generate_pdf(reg_course, student, session, semester, confirmReg):
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
    pdf.cell(0, 4, f" {confirmReg.session.year} || {confirmReg.semester.name} SEMESTER", ln=True)




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
    pdf.cell(60, 7, f'FACULTY / COLLEGE:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.college}', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'PROGRAMME:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.programme}', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'DEGREE:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.degree} {student.programme}', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'EMAIL / PHONE NO:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{student.studentEmail} || {student.studentPhoneNumber}', ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(60, 7, f'LEVEL:')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 7, f'{confirmReg.level.name}', )

    if student.passport:
        image_path = os.path.join(settings.MEDIA_ROOT, student.passport.name)

        if os.path.exists(image_path):
            
            pdf.image(image_path, 170, 50, 23)

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
    unit = 0
    for co in reg_course:
        pdf.cell(25, 4, f'{co.course.courseCode}', border=1)
        pdf.cell(100, 4, f'{co.course.title}', border=1)
        pdf.cell(15, 4, f'{co.course.unit}', border=1)
        pdf.cell(15, 4, f'{co.course.status}', border=1)
        pdf.cell(30, 4, f'', border=1)
        pdf.ln()
        unit += co.course.unit

    pdf.set_font('Arial', 'B', 6)
    pdf.cell(25, 4, f'', border=1)
    pdf.cell(100, 4, f'Total Registered Units', border=1)
    pdf.cell(15, 4, f'{unit}', border=1)
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

    return pdf
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
@user_passes_test(is_student, login_url='/404')
def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        student = get_object_or_404(Student, user=user) 
    return render(request, 'dashboard.html', {'student': student})

# Create your views here.
@login_required
@user_passes_test(is_student, login_url='/404')
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
            return render(request, 'reg.html', {'student':student, 'sess': current_academic_session, 'semes': current_academic_semester, 'exist': 'true', 'semester_passed': semester, "session_passed": curr_session})
        # student = get_object_or_404(Student, user=user) 
        semester = get_object_or_404(Semester, name=semester)
        level = get_object_or_404(Level, name=student.currentLevel)
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

    if request.method == "GET" and "sess" in request.GET:
        sess = request.GET["sess"]
        semes = request.GET["semes"]

        reg_courses = Registration.objects.filter(
                student=student,
                semester=get_object_or_404(Semester, name=semes),
                session=get_object_or_404(Session, year=sess)
            )
        
        confirmReg = confirmRegister.objects.filter(
                student=student,
                semester=get_object_or_404(Semester, name=semes),
                session=get_object_or_404(Session, year=sess)
            ).first()

        return render(request, 'printCopy.html', {'courses': reg_courses, 'confirmReg': confirmReg, 'student':student, 'session_passed': sess, 'semester_passed': semes})

    return render(request, 'reg.html', {'student':student, 'sess': '2024/2025', 'semes': 'first'})

@login_required
@user_passes_test(is_student, login_url='/404')
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
            # print('course id', id)
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

            course_exist = Registration.objects.create(
                student=student,
                course=get_object_or_404(Course, id=id),
                session = get_object_or_404(Session, year=sess), 
                semester = get_object_or_404(Semester, name=semes)
            )
            course_exist.save()

            
            
            # course_exist = Registration.objects.filter(
            #     student=student,
            #     course=get_object_or_404(Course, id=id),
            #     semester=semester
            # ).first()

            # print('course exist', course_exist)

            # if course_exist:
            #     # course_exist = Registration.objects.filter(
            #     #     student=student,
            #     #     semester=semester,
            #     #     course=course
            #     # )
            #     print('yes it exist')
            #     # If the registration already exists, update the session and semester
            #     course_exist.session = get_object_or_404(Session, year=sess)
            #     # registration.semester = semester
            #     course_exist.save()
            # else:
            #     course_exist = Registration.objects.create(
            #         student=student,
            #         course=get_object_or_404(Course, id=id),
            #         session = get_object_or_404(Session, year=sess), 
            #         semester = get_object_or_404(Semester, name=semes)
            #     )
            #     course_exist.save()
        confirmReg = confirmRegister.objects.create(student=student, 
                session = get_object_or_404(Session, year=sess), 
                semester = get_object_or_404(Semester, name=semes),
                level = get_object_or_404(Level,name=student.currentLevel)
            )

        confirmReg.save()
        return redirect('/')
        
    return render(request, 'coursemain.html')

@login_required
@user_passes_test(is_student, login_url='/404')
def printCopy(request):
    if request.user.is_authenticated:
        user = request.user
        student = get_object_or_404(Student, user=user)
    # sess = "2024/2025"
    # semes = "first"
    # # sem=request.GET.get('key')
    # # sess=request.GET.get('keyII')

    # reg_courses = Registration.objects.filter(
    #             student=student,
    #             semester=get_object_or_404(Semester, name=sem),
    #             session=get_object_or_404(Session, year=sess)
    #         )

    if request.method == 'GET':
        return redirect('/')
    
    if request.method == 'POST':
        sess = request.POST["sess"]
        semes = request.POST["semes"]
        reg_courses = Registration.objects.filter(
                student=student,
                semester=get_object_or_404(Semester, name=semes),
                session=get_object_or_404(Session, year=sess)
            )
        
        confirmReg = confirmRegister.objects.filter(
                student=student,
                semester=get_object_or_404(Semester, name=semes),
                session=get_object_or_404(Session, year=sess)
            ).first()
        
        gen = generate_pdf(reg_courses, student, sess, semes, confirmReg)

        gen.output('fpdfdemo.pdf', 'F')
    
        response = HttpResponse(gen.output(dest='S').encode('latin1'), content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="fpdfdemo.pdf"'

        response['Content-Disposition'] = 'inline; filename="preview.pdf"'
        return response


    # return render(request, 'printCopy.html', {'courses': reg_courses,'student':student, 'sess': '2024/2025', 'semes': 'first'})
    return render(request, 'printCopy.html')

# def generatePDF(request):
    # pdf = pdfkit.from_url(request.build_absolute_uri('/print'), False, configuration=config)
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="file_name.pdf"'

    # html_string = render_to_string('template.html', {'data': 'Some context data'})
    # html = HTML(string=html_string)
    # pdf = html.write_pdf()

    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # pdf = render_to_pdf('printCopy.html')

    # return HttpResponse(pdf, content_type='application/pdf')

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
                if (user.user_type == "student"):
                    return redirect('/')
                elif (user.user_type == "instructor"):
                    return redirect('/instructor/dashboard')
                else:
                    # Redirect user to a 404 page
                    return redirect("/404")
            # elif user is not None and user.user_type == 'student':
            else:
                error_message = "Invalid credentials!"
                # return redirect('/accounts/login')
                return render(request, 'login.html', {'error': error_message})
        except User.DoesNotExist:
            error_message = "Invalid credentials!"
            # return redirect('/accounts/login')
            return render(request, 'login.html', {'error': error_message})

        return render(request, 'login.html', {'error': error_message})
    
    return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
@user_passes_test(is_student, login_url='/404')
def changePassword(request):
    if request.method == 'POST':
        old_password = request.POST['oldpassword']
        new_password = request.POST['newpassword']
        confirm_password = request.POST['newpassword']

        if new_password != confirm_password:
            return render(request, 'changepassword.html', {'error': "Use same password"})
        
        user = request.user

        if user.check_password(old_password):
            print('im here')
            user.set_password(new_password)
            return render(request, 'changepassword.html', {'success': "Password Change Successful!"})
        else:
            error_message = "Incorrect old password."
            return render(request, 'changepassword.html', {'error': error_message})

    return render(request, 'changepassword.html')


def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_user = Student.objects.filter(primaryEmail=email).first()
            if associated_user:
                subject = "Password Reset Requested"
                email_template_name = "password_reset_email.html"
                c = {
                    "email": associated_user.email,
                    'domain': get_current_site(request).domain,
                    'site_name': 'http://127.0.0.1:8000/',
                    "uid": urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    "user": associated_user,
                    'token': default_token_generator.make_token(associated_user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, c)
                try:
                    send_mail(subject, email, settings.DEFAULT_FROM_EMAIL, [associated_user.email], fail_silently=False)
                except:
                    return redirect("/password_reset/done/")
    else:
        form = PasswordResetForm()
    return render(request, "password_reset_form.html", {"form": form})

# Password reset confirm view (handles the link in the email)
def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect("/reset/done/")
        else:
            form = SetPasswordForm(user)
    else:
        form = None

    return render(request, 'password_reset_confirm.html', {'form': form})


# // Admin dashboards

@login_required
@user_passes_test(is_instructor, login_url='/404')
def adminDashboard(request):
    if request.user.is_authenticated:
        user = request.user
        instructor = get_object_or_404(Instructor, user=user) 
        countProgrammes = len(Programme.objects.filter(department=instructor.department))
        countCourses = len(Course.objects.filter(department=instructor.department))
        

    return render(request, 'admin/admin_dashboard.html', {"countProgrammes":countProgrammes, "countCourses": countCourses, "department": instructor.department })

@login_required
@user_passes_test(is_instructor, login_url='/404')
def adminProgrammeManagement(request):
    if request.user.is_authenticated:
        
        user = request.user
        instructor = get_object_or_404(Instructor, user=user) 
        programmes = Programme.objects.filter(department=instructor.department)
        # countCourses = len(Course.objects.filter(department=instructor.department))
        if request.method == "POST":
            programme_name = request.POST['programme_name']
            programme_duration = request.POST['programme_duration']
            programme_degree = request.POST['programme_degree']

            if Programme.objects.all().filter(name=programme_name).exists():
                messages.info(request, 'Programme already exist!')
                return redirect("/instructor/programmes")
        
            programmeObjects = Programme.objects.create(name=programme_name, department=instructor.department, 
                                          duration=programme_duration, degree=programme_degree)
            programmeObjects.save()
            messages.info(request, 'Programme Added!')
            return redirect('/instructor/programmes')



    return render(request, 'admin/admin_program_management.html', {"programmes": programmes, "department": instructor.department,})

@login_required
@user_passes_test(is_instructor, login_url='/404')
def UpdateProgramme(request):
    if request.user.is_authenticated:
        user = request.user
        instructor = get_object_or_404(Instructor, user=user)
        if request.method == "POST":
            p_id = request.POST["programme_id"]
            p_name = request.POST["programme_name"].strip()
            p_duration = request.POST["programme_duration"].strip()
            p_degree = request.POST["programme_degree"].strip()

            if p_name != "" and p_duration != "" and p_degree != "": 
                try:
                    programmes = Programme.objects.filter(department=instructor.department, id=p_id)[0]
                    programmes.name = p_name
                    programmes.degree = p_degree
                    programmes.duration = p_duration
                    programmes.save()
                    messages.info(request, f'Programme Updated')
                    return redirect("/instructor/programmes")
                except:
                    messages.info(request, f'Programme not available')
                    return redirect("/instructor/programmes")
            messages.info(request, f'Fields cannot be empty')
            return redirect("/instructor/programmes")
        return redirect("/instructor/programmes")
    

@login_required
@user_passes_test(is_instructor, login_url='/404')
def deleteProgramme(request, id):

    try:
        program = Programme.objects.filter(id=id)[0]
        print("1", program.name)
        if Programme.objects.all().filter(id=id).exists():
            messages.info(request, f'{program.name} deleted successfully')
            program = Programme.objects.filter(id=id).delete()
            
            return redirect("/instructor/programmes")
        messages.info(request, f'Programme not available')
        return redirect("/instructor/programmes")
    except:
        messages.info(request, f'Programme not available')
        return redirect("/instructor/programmes")
    

@login_required
@user_passes_test(is_instructor, login_url='/404')
def adminCourseManagement(request):
    if request.user.is_authenticated:
        user = request.user
        instructor = get_object_or_404(Instructor, user=user)

    return render(request, 'admin/course_management.html')

def F404(request):
    return render(request, 'admin/404.html')