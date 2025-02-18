from pdf_processing import extract_text_from_pdf

# Path to your sample PDF
pdf_path = "UNIT 1 - CMA - II.pdf"

# Extract text
extracted_text = extract_text_from_pdf(pdf_path)

# Print the extracted text
print("Extracted Text from PDF:")
print(extracted_text)
