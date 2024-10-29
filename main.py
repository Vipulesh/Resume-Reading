from typing_extensions import TypedDict
import random
from typing import Literal
from IPython.display import Image, display
import json

from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import tools_condition
from langgraph.prebuilt import ToolNode

from agents.resume_reader_agent import ResumeReaderAgent
from agents.extractor_agent import ExtractorAgent
from agents.validator_agent import ValidatorAgent

import os, getpass
from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()
api_key = os.getenv("LANGSMITH_API_KEY")
if not api_key:
    raise EnvironmentError("LANGSMITH_API_KEY environment variable not set.")

LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY=api_key
LANGCHAIN_PROJECT="pibit-assessment"

groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=groq_api_key, model="llama3-8b-8192")

def get_resume_text(file_path: str) -> str:
    """
    Reads the resume text from the file.
    Args:
        file_path (str): The path to the resume file.
    """
    reader_agent = ResumeReaderAgent(file_path)
    resume_text = reader_agent.read_resume()
    return resume_text

def extract_entities(resume_text: str) -> str:
    """
    Extracts structured information from resume text using Gemini.
    Args:
        resume_text (str): The resume text to extract information from.
    """
    extractor_agent = ExtractorAgent()
    extracted_data = extractor_agent.extract_entities(resume_text)
    return extracted_data

def validate_entities(extracted_data: str) -> str:
    """
    Validates the extracted entities.
    Args:
        extracted_data (str): The extracted data from the resume
    """
    validator_agent = ValidatorAgent(extracted_data)
    validation_results = validator_agent.validate_entities()
    return validation_results

tools = [get_resume_text, extract_entities, validate_entities]

llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with reading a resume and validating the extracted entities. You just need to return the validated entities as a json object.")

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

builder = StateGraph(MessagesState)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")
react_graph = builder.compile()

# Show
display(Image(react_graph.get_graph(xray=True).draw_mermaid_png()))

file_path = "211010258_Vipulesh.pdf"
messages = [HumanMessage(content=f"Read the resume from the file: {file_path}")]
messages = react_graph.invoke({"messages": messages})

for m in messages['messages']:
    m.pretty_print()

