from markdown_pdf import MarkdownPdf,Section



def generate_markdown_pdf(markdown_code):
    pdf = MarkdownPdf(toc_level=2)
    try:
        pdf.add_section(Section(markdown_code, toc=False))
        #pdf.save("markdown.pdf")
    except Exception as e:
        print(f"Error while generate_markdown_pdf ",e)
       
    return pdf


