from markdown_pdf import MarkdownPdf,Section

import re

def extract_content(markdown_string):
    # Use a regular expression to match the pattern and extract content
    match = re.search(r'```markdown\s*(.*?)\s*```', markdown_string, re.DOTALL)
    if match:
        print('00')
        return match.group(1)
    match1 = re.search(r'```markdown\s*(.*)', markdown_string, re.DOTALL)
    if match1:
        print('11')
        return match1.group(1)
    return markdown_string



def generate_markdown_pdf(markdown_code):
    markdown_code=extract_content(markdown_code)
    pdf = MarkdownPdf(toc_level=2)
    try:
        pdf.add_section(Section(markdown_code, toc=False))
        #pdf.save("markdown.pdf")
    except Exception as e:
        print(f"Error while generate_markdown_pdf ",e)
       
    return pdf

