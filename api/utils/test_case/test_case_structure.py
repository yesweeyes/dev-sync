import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from typing import List
import json

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

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
      Response must be json parseable.Do not respond to user as ```json
      At the end, return an array of user stories in structured JSON parseable format,following this structure.Follow the given template below: 

      {example_template}
      """
      # context = {
      #     f"Title: story['Title']\n"
      #     f"Description: story['Description']\n"
      #     f"Acceptance Criteria: story['Acceptance Criteria']\n"
      #     f"Priority: story['Priority']\n"
      #     f"Story Points: story['Story Points']\n"
      #     f"Labels: story['Labels']\n"
      # }

      prompt_template = ChatPromptTemplate.from_messages(
        [("system",system_template), 
        ("user", "{context}"), 
        ("user", "{text}")
        ]
      )
      prompt = prompt_template.invoke({
          "example_template": example_template,
          "context": str(story) + summary,
          "text": "Generate necessary test cases for the content including functional and non-functional"
      })
      response = model.invoke(prompt)
      try:
        parsed_response = json.loads(response.content)  
        test_cases.append(parsed_response) 
      except json.JSONDecodeError:
        print("Error: Response is not a valid JSON format.") 

  return json.dumps(test_cases, indent=4)
