from pdf_processing import extract_text_from_pdf

pdf_path = "UNIT 1 - CMA - II.pdf"
text = extract_text_from_pdf(pdf_path)
print("Extracted Text:\n", text)
