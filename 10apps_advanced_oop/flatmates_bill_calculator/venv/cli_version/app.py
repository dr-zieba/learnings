from fpdf import FPDF
from pdfreport import PdfReport
from flats import Bill, Flatmate

bills_amount = input("Type bills` amount: ")
bills_period = input("Type bills` period (format month year): ")

bill = Bill(float(bills_amount), bills_period)


flat1 = Flatmate("Johnn", 20)
flat2 = Flatmate("Marry", 25)

pdf_report = PdfReport("cli_version/report.pdf")
pdf_report.generate(bill, flat1, flat2)

print(f"{flat1.name} pays: {flat1.pay(bill, flat2)}")
print(f"{flat2.name} pays: {flat2.pay(bill, flat1)}")

