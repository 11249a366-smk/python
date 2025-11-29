import PyPDF2

def combine_selected_pages(pdf_info_list, output_filename):
    pdf_writer = PyPDF2.PdfWriter()
    for pdf_file, page_numbers in pdf_info_list:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in page_numbers:
                if 0 <= page_num < len(pdf_reader.pages):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

pdf_inputs = [
    ("sample1.pdf", [0, 2]),
    ("sample2.pdf", [1]),
    ("sample3.pdf", [0, 1])
]

combine_selected_pages(pdf_inputs, "combined_output.pdf")
