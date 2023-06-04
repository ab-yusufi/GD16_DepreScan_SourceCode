from fpdf import FPDF

# cell height
ch = 8
class PDF(FPDF):
    def __init__(self):
        super().__init__()
    def header(self):
        self.set_font('Arial', '', 12)
        self.cell(0, 8, '', 0, 1, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 12)
        self.cell(0, 8, f'Page {self.page_no()}', 0, 0, 'C')

tableCol1 = ["Depression Score", "Enthusiasm", "Optimisum","PHQ"]
tableCol3 = ["0-20%", "40-100%", "70-100%","0-4"]
phqText = ""

def create_pdf(pname,pemail,pphone,page,pgender,dscore,enthu,anx,phq):
    #set phq text
    if(int(phq) <= 4):
        phqText = "Minimal Depression"
    elif(int(phq) > 4 and int(phq) <= 9):
        phqText = "Mild Depression"
    elif(int(phq) > 9 and int(phq) <= 14):
        phqText = "Moderate Depression"
    elif(int(phq) > 14 and int(phq) <= 19):
        phqText = "Moderately Severe Depression"
    elif(int(phq) > 19 and int(phq) < 27):
        phqText = "Severe Depression"
    tableCol2 =[dscore,enthu,anx,phq]
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(w=0, h=20, txt="Patient Report", ln=1)
    pdf.set_font('Arial', '', 16)
    pdf.cell(w=40, h=ch, txt="Name: ", border =1,ln=0)
    pdf.cell(w=140, h=ch, txt=pname, border =1,ln=1)
    pdf.cell(w=40, h=ch, txt="Email: ", border =1,ln=0)
    pdf.cell(w=140, h=ch, txt=pemail,border =1, ln=1)
    pdf.cell(w=40, h=ch, txt="Phone Number: ", border =1,ln=0)
    pdf.cell(w=140, h=ch, txt=pphone, border =1,ln=1)
    pdf.cell(w=40, h=ch, txt="Age: ", border =1,ln=0)
    pdf.cell(w=45, h=ch, txt=page,border =1, ln=0)
    pdf.cell(w=45, h=ch, txt="Gender: ", border =1,ln=0)
    pdf.cell(w=50, h=ch, txt=pgender,border =1, ln=1)
    pdf.ln(ch)
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(w=0, h=20, txt="Your Scores", ln=1, align="C")
    # Table Header
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(w=15, h=ch, txt='', ln=0, align='C')
    pdf.cell(w=50, h=ch, txt='Test Name', border=1, ln=0, align='C')
    pdf.cell(w=50, h=ch, txt='Result', border=1, ln=0, align='C')
    pdf.cell(w=50, h=ch, txt='Reference Range', border=1, ln=1, align='C')
    # Table contents
    pdf.set_font('Arial', '', 16)
    for i in range(0, len(tableCol1)):
        pdf.cell(w=15, h=ch, txt='', ln=0, align='C')
        #Enthusiasm
        if(i == 1):
            if(int(tableCol2[i][:-1]) >= 40):
                pdf.set_text_color(r=255, g= 255, b = 255)
                pdf.set_fill_color(r=0, g= 255, b = 0)
            else:
                pdf.set_text_color(r=255, g= 255, b = 255)
                pdf.set_fill_color(r=255, g= 0, b = 0)
        elif(i <= 2):
            #Depression
            if(i == 0):
                if(int(tableCol2[i][:-1]) >= 21):
                    pdf.set_text_color(r=255, g= 255, b = 255)
                    pdf.set_fill_color(r=255, g= 0, b = 0)
                else:
                    pdf.set_text_color(r=255, g= 255, b = 255)
                    pdf.set_fill_color(r=0, g= 255, b = 0)
            #Optimisum
            elif(i == 2):
                if(int(tableCol2[i][:-1]) <= 70):
                    pdf.set_text_color(r=255, g= 255, b = 255)
                    pdf.set_fill_color(r=255, g= 0, b = 0)
                else:
                    pdf.set_text_color(r=255, g= 255, b = 255)
                    pdf.set_fill_color(r=0, g= 255, b = 0)
        #PHQ-9 Conditions
        else:
            if(int(tableCol2[i]) <= 4 and int(tableCol2[i]) >= 1):
                pdf.set_text_color(r=255, g= 255, b = 255)
                pdf.set_fill_color(r=255, g=140, b=0)
            elif(int(tableCol2[i]) >= 5):
                pdf.set_text_color(r=255, g= 255, b = 255)
                pdf.set_fill_color(r=255, g= 0, b = 0)
            elif(int(tableCol2[i]) == 0):
                pdf.set_text_color(r=255, g= 255, b = 255)
                pdf.set_fill_color(r=0, g= 255, b = 0)
        pdf.cell(w=50, h=ch, 
                txt=tableCol1[i], 
                border=1, ln=0, align='C',fill=True)
        pdf.cell(w=50, h=ch, 
                txt=tableCol2[i], 
                border=1, ln=0, align='C',fill=True)
        pdf.cell(w=50, h=ch, 
                txt=tableCol3[i], 
                border=1, ln=1, align='C', fill=True)
    if(int(phq) == 0):
        pdf.set_text_color(r=0, g= 255, b = 0)
    elif(int(phq) <= 4 and int(phq) >= 1):
        pdf.set_text_color(r=255, g=140, b=0)
    else:
        pdf.set_text_color(r=255, g= 0, b = 0)
    pdf.ln(ch)
    pdf.cell(w=50, h=ch, txt=f'According to your assessment, you are in "{phqText}".', ln=1)
    
    pdf.set_text_color(r=0,g=0,b=0)
    pdf.ln(ch)
    pdf.cell(w=50, h=ch, txt='Note:', ln=1)
    # pdf.multi_cell(w=180, h=ch, txt="1) The results obtained from this test not an indicative of depression level of the patient.")
    pdf.cell(w=30, h=ch, txt="1) The test results should be interpreted by a certified medical professional.", ln=1)
    pdf.multi_cell(w=180, h=ch, txt="2) The result is for indicative purpose only. The result published are for immediate information to the patient. ")
    # pdf.cell(w=30, h=ch, txt="4) For accurate analysis contact the doctor. ", ln=1)
    pdf.ln(ch)
    pdf.cell(w=30, h=ch, txt="=> We are dedicated to provide utmost support for your mental health.", ln=1)
    pdf.cell(w=30, h=ch, txt="=> For free medical assistance call Tele Manas.", ln=1)
    pdf.cell(w=30, h=ch, txt="=> Tele Manas is a comprehensive mental health care service ", ln=1)
    pdf.cell(w=30, h=ch, txt="=> Dial 14416 or 18008914416", ln=1)
    pdf.ln(ch)

    pdf.set_font('Arial', 'B', 30)
    pdf.set_text_color(r=0, g= 0, b = 255)
    pdf.cell(w=180, h=ch, txt="Thank You", ln=1, align="C")
    pdf.output(f'./example.pdf', 'F')

create_pdf("Yash Kandalkar","yashkandalkar555@gmail.com","9370003979","21","Male","21%","39%","70%","0")