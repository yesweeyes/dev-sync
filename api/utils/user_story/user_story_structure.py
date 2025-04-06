import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

if not os.environ.get("GROQ_API_KEY"):
  raise RuntimeError("Invalid GROQ api key provided")

model = init_chat_model("llama-3.3-70b-versatile", model_provider="groq")

example_output = \
"""
[{
    "summary": "User Registration",
    "description": "As a new user, I want to register an account so that I can access the platform.",
    "Acceptance Criteria": "The user should be able to enter their details (name, email, password).",
    "issueType": "Story",
    "labels": ["authentication", "user-management"],
    "storyPoints": 3,
    "Priority": "High"
}]
"""


def generate_user_story_helper(text_chunks: str, user_prompt: str):
  system_template = \
  """
  You are an AI specialized in generating user stories. Maintain context across multiple inputs.
  Do not respond to user with Hear are the responses. Response must be json parseable.
  At the end, return an array of user stories in structured JSON parseable format,following this structure:
  {example_output}
  """

  context = \
  """
  Generate user stories customised to the given request:\n
  """.join([chunk for chunk in text_chunks])

  prompt_template = ChatPromptTemplate.from_messages(
      [("system", system_template), ("user", "{context}"), ("user", user_prompt)]
  )

  prompt = prompt_template.invoke({
    "example_output": example_output,
    "context": context,
    "enhanced_user_prompt": user_prompt,
    })

  response = model.invoke(prompt)
  return response.content


