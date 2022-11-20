from fpdf import FPDF


class PdfReport(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, bill, flat1, flat2):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=22, style='B')
        pdf.cell(w=0, h=40, txt="Monthly charges invoice", border=0, align='C', ln=1)
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=0, h=40, txt=f"Period: {bill.period}", border=0, ln=2)
        pdf.cell(w=0, h=40, txt=f"Bill amount: {bill.amount}", border=0, ln=2)

        pdf.set_font(family='Times', size=14)
        pdf.cell(w=0, h=20, txt=f"{flat1.name} pays: {round(flat1.pay(bill, flat2), 2)}", border=0, ln=3)
        pdf.cell(w=0, h=20, txt=f"{flat2.name} pays: {round(flat2.pay(bill, flat1), 2)}", border=0, ln=4)

        pdf.output(self.file_name)