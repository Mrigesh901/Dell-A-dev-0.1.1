from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate

from config import API_KEY
from pprint import pprint

api_key = API_KEY
def set_model_parameters(model= "gemini-pro",
                         temperature=0.3,
                         top_p = None,
                         top_k = None,
                         max_output_tokens = 4096,
                         candidate_count =  1,
                         google_api_key = api_key
                         ):
  print("set_model_parameters fired")
  model = ChatGoogleGenerativeAI(model= model,
                                 temperature=temperature,
                                 top_p = top_p,
                                 top_k = top_k,
                                 max_output_tokens = max_output_tokens,
                                 candidate_count = candidate_count,
                                 google_api_key = google_api_key)
  return(model)

def set_prompt_softwired():

  #https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/
  prompt_template = """Paraphrase this text:

  {input_text}

  In the style of a {style}.

  Paraphrase: """

  prompt = PromptTemplate(template=prompt_template, input_variables=["style", "input_text"])

  return(prompt)


def paraphrase_softwired(paraphrase_text,style):

    input_text = paraphrase_text
    style = style
    #print("paraphrase_softwired fired..")
    model = set_model_parameters()
    #print("MODEL: ",model)

    prompt = set_prompt_softwired()
    #print("PROMPT: ", prompt)

    chain = LLMChain(prompt = prompt, llm = model)
    #print("CHAIN: ", chain)

    resp = chain.invoke({"style" : style,
                         "input_text": input_text
                         })

    ptext = resp["text"]
    #pprint("PARAPHRASED TEXT: " + ptext)
    pprint("hello from paraphrase.py")
    return ptext