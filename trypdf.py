import fpdf
from fpdf import FPDF, HTMLMixin


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
pdf.cell(0, 4, f" 2019/2020 || FIRST SEMESTER", ln=True)




pdf.set_font('times', 'B', 10)
pdf.set_fill_color(6, 75, 37)
pdf.set_text_color(255, 255, 255)
pdf.cell(180, 7, f"   :. Students' Personal Information", ln=True, fill=True, align='L')

pdf.set_font('helvetica', 'BIU', 13)
pdf.set_font('times', 'B', 7)

pdf.set_text_color(0, 0, 0)
pdf.cell(60, 7, f'FUll NAME:')
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 7, f'Otelo Oteh', ln=True)
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 7, f'MATRIC NO / JAMB NO:')
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 7, f'Aubch244248 [95753342EC]', ln=True)
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 7, f'FACULTY:')
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 7, f'Science', ln=True)
pdf.set_text_color(0, 0, 0)
pdf.cell(60, 7, f'PROGRAMME:')
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 7, f'industrial chemistry', ln=True)
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



# for i in range (1, 41):
#     pdf.cell(0, 10, f'This is line {i} :D', ln=True)
pdf.output('fpdfdemo.pdf', 'F')