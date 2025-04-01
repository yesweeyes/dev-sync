import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

example_output = """{
      "summary": "User Registration",
      "description": "As a new user, I want to register an account so that I can access the platform.
      I want register and login features so that if new user i will login else register by creating new account",
      "Acceptance Criteria":"The user should be able to enter their details (name, email, password).The system should send a confirmation email after registration.
      The user should be able to log in using the registered credentials.",
      "issueType": "Story",
      "labels": ["authentication", "user-management"],
      "storyPoints": 3,
      "Priority:High
  } in json format"""


def generate_user_story(context: str, user_prompt: str):
  system_template = "Generate user story for content given by user in format described in example: \n{example_output} "

  prompt_template = ChatPromptTemplate.from_messages(
      [("system", system_template), ("user", "{context}"), ("user", enhanced_user_prompt)]
  )

  prompt = prompt_template.invoke({
    "example_output": example_output,
    "context": context,
    "enhanced_user_prompt": enhanced_user_prompt,
    })
  
  response =model.invoke(prompt)
  return response.content


