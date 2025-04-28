import json
from typing import List
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from app.config import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GEMINI_API_KEY)

example_template = '''
Module Name:Mention the name of the user story through which the test case is being created
Title: Test case title.
Description:  Describe the test objective in brief.
Preconditions: Any prerequisite that must be fulfilled before the execution of this test case
Test Steps:List all the test execution steps in detail.
Post-condition: What should be the state of the system after executing this test case?
Priority: High
Test Type:This field can be used to classify tests based on test types.
'''
    
    
def generate_test_case_helper(user_stories: List[dict], summary) -> str:

  test_cases = []
  for story in user_stories:
      system_template = f"""
      You are an expert in generating test cases for a given context, including edge cases and performance test cases.
      The response must be in pure JSON format, without any markdown code blocks (no ```json wrapping).
      At the end, return an array of test cases in a structured JSON format, following this structure.

      {example_template}
      """

      prompt_template = ChatPromptTemplate.from_messages(
        [("system",system_template), 
        ("user", "{context}"), 
        ("user", "{text}")
        ]
      )
      prompt = prompt_template.invoke({
          "example_template": example_template,
          "context": str(story),
          "text": f"Generate necessary test cases for the context using additional content {summary} including functional and non-functional.Do not start with ```json"
      })
      response = model.invoke(prompt)
      print(response)
      try:
        parsed_response = json.loads(response.content)  
        test_cases.append(parsed_response) 
      except json.JSONDecodeError:
        print("Error: Response is not a valid JSON format.") 

  return json.dumps(test_cases, indent=4)
