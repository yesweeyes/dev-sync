import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit
from app.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY, api_version="v1")


hld_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
    You are a solution architect. Generate a detailed High-Level Design (HLD) document based on the following content:
    {content}

    The generated document should include :
    1. Title (for example, High-Level Design (HLD) for "document name")
    2. Table of content with page number (a complete table format)
    3. Introduction, including - Why this HLD?, Scope of this doc, Intended audience, definitions, references, System overview
    4. System Design, includin - Application Design, process flow, Information flow.
    5. High level Architecture image, workflow of the user's typical process
    6. Key modules
    7. Network Diagram image
    8. UML Class diagram image
    9. Database Design
    10. User Interface, Hardware and Software Interface
    11. Error Handling
    12. Help
    13. Performance specifications
    14. Security
    15. Reliability 
    16. Tools Used
    Include all the mentioned topics compulsorily and add other topics based on the content in detail
    Make sure all pages have page numbers, have a formal structure and the diagrams should be embedded wherever appropriate.
    """
)


lld_prompt = PromptTemplate(
    input_variables=["hld_response"],
    template="""
    You are a software developer. Generate a detailed Low-Level Design (LLD) document based on the following HLD document:
    {hld_response}
    
    The generated document should include:
    1. Title (for example, Low-Level Design (LLD) for "document name")
    2. Table of content with page numbers
    3. Introduction, include - Purpose, Scope, Audience, References, Definitions
    4. System Overview, include - System description, system context,Implementation details
    5. Detailed Design, include - Module Descriptions, Class diagrams, Sequence diagrams, state diagrams, activity diagrams, UML diagrams
    6. Data Design, include - Data structures, Database design, data flow
    7. Interface design , include - User interface, External interfaces
    8. Algorithms - Complexity analysis
    9. Security Design- Security measures, authentication and authorization , Data protection
    10. Error handling and Logging
    11. Testing and Validation- unit testing, integration testing and Validation
    12. Deployment considerations, assumptions and dependencies
    Include all the mentioned topics compulsorily and add other topics based on the content in detail
    Make sure all pages have page numbers, have a formal structure and the diagrams should be embedded wherever appropriate.
    """
)

def generate_hld(content):
    hld_chain = LLMChain(llm=llm, prompt=hld_prompt)
    hld_response=hld_chain.run(content=content)
    hld_pdf_path = os.path.join("output", "HLD_Document.pdf")
    os.makedirs("output", exist_ok=True)
    save_to_pdf(hld_response, hld_pdf_path)

    return hld_response, hld_pdf_path

def generate_lld(hld_response):
    lld_chain=LLMChain(llm=llm,prompt=lld_prompt)
    lld_response=lld_chain.run(hld_response=hld_response)
    lld_pdf_path=os.path.join("output","LLD_Document.pdf")
    os.makedirs("output",exist_ok=True)
    save_to_pdf(lld_response,lld_pdf_path)

    return lld_response,lld_pdf_path


def process_with_llm(text_chunks):
   
    hld_response,hld_path=generate_hld(text_chunks)
    lld_response,lld_path=generate_lld(hld_response)

    return hld_path,lld_path


# pdfmetrics.registerFont(TTFont("DejaVu","fonts\DejaVuSans.ttf"))

def save_to_pdf(content, file_name):
    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 12)

    #aligining the contents into different lines
    lines = simpleSplit(content, "Helvetica", 12, width - 100)

    y = height - 50
    for line in lines:
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50
        c.drawString(50, y, line)
        y -= 24

    c.save()