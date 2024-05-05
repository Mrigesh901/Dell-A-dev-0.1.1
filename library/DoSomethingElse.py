from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate

from pprint import pprint
from library import Util

def set_prompt():

  template = """Generate text from this prompt:

  {input_text}

  Text: """

  prompt = PromptTemplate(template=template, input_variables=["input_text"])

  return(prompt)


def do_something_else(model, instruction):

    #Now on SomethinElse:Screen1 in GUI
    # new_instruction = input("Enter what you have in mind:")
    prompt = set_prompt()
    #print("PROMPT: ", prompt)
    chain = LLMChain(prompt = prompt, llm = model)
    #print("CHAIN: ", chain)

    resp = chain.invoke({"input_text": instruction,})

    text = resp["text"]
    #pprint(text)
    return(text,instruction)



def do_the_work(instruction):
  model = Util.set_model_parameters()
  text, previous_instruction = do_something_else(model, instruction)
  return text,previous_instruction
