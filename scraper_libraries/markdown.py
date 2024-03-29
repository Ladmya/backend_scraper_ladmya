import markdown

def convert_markdown_string_to_html_string(response_text):
    markdown_to_html = markdown.markdown(response_text)
    return markdown_to_html