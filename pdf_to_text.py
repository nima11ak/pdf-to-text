

import pdfplumber


def extract_text_from_pdf(file_path):
    all_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + "\n"

    return all_text

pdf_file ="b.pdf"

output_file = "output.text"

text = extract_text_from_pdf(pdf_file)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

    print("...متن استخراج و ذخیره شد...")


#---------------------------------------------------
