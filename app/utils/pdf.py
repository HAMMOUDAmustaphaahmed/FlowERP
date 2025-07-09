import pdfkit

def generate_pdf(html_content, output_path):
    pdfkit.from_string(html_content, output_path)