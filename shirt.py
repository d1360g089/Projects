import fpdf
from fpdf import FPDF



class PDF(FPDF):
    def title(self):
        image_path = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
        self.image(image_path, 0, y=20, w=210, h=277)
        self.set_font("helvetica", "B", 18)
        self.cell(80)
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        self.ln(20)
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page %s" % self.page_no(), 0, 0, align="C")


pdf = PDF()
pdf.add_page()
pdf.ouput("CS50_Shirt.pdf")


