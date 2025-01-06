from markitdown import MarkItDown

# Function to parse the CV file and return the text content (what ever the cv extention is)
def cv_parser(file_path):
    md = MarkItDown()
    result = md.convert(file_path)
    return result.text_content