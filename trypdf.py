import fpdf
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # logo
        self.image('achieverslogo.png', 10, 8, 20)
        # font
        self.set_font('helvetica', 'B', 14)
        # padding
        self.cell(75)
        #Title
        self.cell(10,  5, 'ACHIEVERS UNIVERSITY, OWO', border=False, ln=1, align='C')
        # line break
        self.ln(1)

        self.set_font('helvetica', 'B', 10)
        # padding
        self.cell(75)
        #Title
        self.cell(16,  5, 'Owo, Ondo State, Nigeria Website: www.achievers.edu.ng', border=False, ln=1, align='C')
        self.ln(1)

        self.set_font('helvetica', 'B', 11)
        # padding
        self.cell(75)
        #Title
        self.cell(16,  5, 'COURSE REGISTRATION FORM', border=False, ln=1, align='C')
        self.ln(1)

        self.set_font('helvetica', 'B', 10)
        # padding
        self.cell(75)
        #Title
        self.cell(16,  5, f'Academic Session: 2023/2024     Semester: First', border=False, ln=1, align='C')
        self.ln(1)
         # logo
        self.image('profile_pic.jpg', 170, 8, 23)

pdf = PDF('P', 'mm', 'Letter')

#set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# add a page
pdf.add_page()


pdf.set_font('helvetica', 'BIU', 16)
pdf.set_font('times', '', 12)

for i in range (1, 41):
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)
pdf.output('fpdfdemo.pdf', 'F')