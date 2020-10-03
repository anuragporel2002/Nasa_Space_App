#Report Saver
#------------------------Modules------------------------------------------------------
from fpdf import FPDF

#------------------------Functions----------------------------------------------------
def save(name,age,sex,system,height,weight,activity,program,work_start,work_end,preparation,refresh,sleep_hour,sleep_buffer,sleep_cycle,title):
#------------------------Instance Creation & Addition of First Page-------------------
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial",'B',20) 
#------------------------Create Cells & Add Data--------------------------------------
    pdf.cell(200, 10, txt = "Sleep Schedule and Nutrition Report",ln = 1, align = 'C')
    pdf.set_font("Arial", size = 13)
    pdf.cell(200, 10, txt = "________________________________________________________________________", ln=2, align='L') 
    pdf.cell(200, 10, txt = "Name: "+name, ln=3, align='L')
    pdf.cell(200, 10, txt = "Age:"+str(age)+"                                             Sex:"+sex+"                                      System: "+system, ln=4, align='L')
    if system=='Metric':
        pdf.cell(200, 10, txt = "Weight: "+str(weight)+" kg"+"                                                                                  Height: "+str(height)+" cm", ln=5, align='L')
    elif system=='Imperial':
        pdf.cell(200, 10, txt = "Weight: "+str(weight)+" lbs."+"                                                                          Height: "+str(height)+" inches", ln=5, align='L')
    pdf.cell(200, 10, txt = "Activity Status: "+activity+"                                              Program: "+program, ln=6, align='L')
    pdf.cell(200, 10, txt = "Work Start Time                               : "+work_start, ln=7, align='L')
    pdf.cell(200, 10, txt = "Work End Time                                : "+work_end, ln=8, align='L')
    pdf.cell(200, 10, txt = "Preparation Time After Waking Up  : "+str(preparation)+" hrs.", ln=9, align='L')
    pdf.cell(200, 10, txt = "Refresh Time After Work                 : "+str(refresh)+" hrs.", ln=9, align='L')
    pdf.cell(200, 10, txt = "Buffer Time Before Sleep                : "+str(sleep_buffer)+" mins.", ln=9, align='L')
    pdf.cell(200, 10, txt = "________________________________________________________________________", ln=10, align='L')
    pdf.cell(200, 10, txt = "Daily Required Sleep Hour : "+str(sleep_hour)+" hrs.", ln=9, align='L') 
    pdf.cell(200, 10, txt = "Number of Sleep Cycles (90 min each) : "+str(sleep_cycle), ln=9, align='L')
        

#------------------------Save .pdf file-----------------------------------------------   
    pdf.output(title)

#------------------------Run Code-----------------------------------------------------
if __name__=="__main__":
    save("Anurag Porel",19,"M","Metric",165,69,"Sedentary","Maintain Weight","10:30:00","17:30:00",1.5,2,7.5,30,5,"report.pdf")
        