from schemas.requirement_document import  RequirementDocumentBase
import fitz  

def parse_requirement_document(file: RequirementDocumentBase) -> str:
    content = ""
    try:
        document = fitz.open(file.file_path)
        for page_number in range(len(document)):
            page_header = f"{'#' * 5} PAGE {page_number + 1} {'#' * 5}\n"
            page_footer = f"{'#' * 5} END OF PAGE {'#' * 5}\n"
            page_text = document[page_number].get_text()
            content += page_header + page_text + page_footer
        return content
    except Exception as e:
        raise Exception(f"Unable to parse document: {str(e)}")
