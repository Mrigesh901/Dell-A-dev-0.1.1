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


def do_something_else(model, previous_instruction, new_instruction):

    #Previous_instruction is used to prefill the textbox in the GUI, so that user can optionally modify it
    #Not used in this program

    #Now on SomethinElse:Screen1 in GUI
    # new_instruction = input("Enter what you have in mind:")
    new_instruction = new_instruction
    prompt = set_prompt()
    #print("PROMPT: ", prompt)
    chain = LLMChain(prompt = prompt, llm = model)
    #print("CHAIN: ", chain)

    resp = chain.invoke({"input_text": new_instruction,})

    text = resp["text"]
    pprint(text)
    previous_instruction = new_instruction
    # add_to_transcript(new_instruction, text)

    return(text,previous_instruction)



def do_the_work(new_instruction,previous_instruction):
  model = Util.set_model_parameters()
  previous_instruction = previous_instruction
  text, previous_instruction = do_something_else(model, previous_instruction, new_instruction)
  return text,previous_instruction
