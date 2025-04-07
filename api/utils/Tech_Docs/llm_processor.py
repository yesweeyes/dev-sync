import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from fpdf import FPDF

load_dotenv(".env")
Gemini_api_Key = os.getenv("GEMINI_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=Gemini_api_Key, api_version="v1")


hld_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
    You are a software engineer. Generate a detailed High-Level Design (HLD) document based on:
    {content}
    Include Introduction, high-level architecture, network diagram, key modules, and formal structure.
    """
)


lld_prompt = PromptTemplate(
    input_variables=["content"],
    template="""
    You are a software engineer. Generate a detailed Low-Level Design (LLD) document based on:
    {content}
    Include Introduction, architecture diagram, data flow, and implementation details.
    """
)

def process_with_llm(docx_path):
    from docx import Document

    doc = Document(docx_path)
    content = "\n".join([para.text for para in doc.paragraphs])

    hld_chain = LLMChain(llm=llm, prompt=hld_prompt)
    lld_chain = LLMChain(llm=llm, prompt=lld_prompt)

    hld_response = hld_chain.run(content=content)
    lld_response = lld_chain.run(content=content)

    hld_pdf_path = os.path.join("outputs", "HLD_Document.pdf")
    lld_pdf_path = os.path.join("outputs", "LLD_Document.pdf")

    save_to_pdf(hld_response, hld_pdf_path)
    save_to_pdf(lld_response, lld_pdf_path)

    return hld_pdf_path, lld_pdf_path

def save_to_pdf(content, file_name):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(file_name)
