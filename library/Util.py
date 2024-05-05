from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain import PromptTemplate

from config import API_KEY

from pprint import pprint

# #Module for Transcript Stuff
# import os
# import json
# from pathlib import Path as path
# from google.colab import drive

# #Secrets
# SecretName = 'docinteract'
# def api_key_for_colab():
#   from google.colab import userdata
#   api_key = userdata.get(SecretName)
#   return (api_key)

#Gemini Parameters
api_key = API_KEY
def set_model_parameters(model= "gemini-pro",
                         temperature=0.3,
                         top_p = None,
                         top_k = None,
                         max_output_tokens = 4096,
                         candidate_count =  1,
                         google_api_key = api_key
                         ):

  model = ChatGoogleGenerativeAI(model= model,
                                 temperature=temperature,
                                 top_p = top_p,
                                 top_k = top_k,
                                 max_output_tokens = max_output_tokens,
                                 candidate_count = candidate_count,
                                 google_api_key = google_api_key)
  return(model)

TASK_NAME = 'SomethingElse'
# MOUNT_ROOT = '/content/drive'
# Transcripts_Folder = MOUNT_ROOT + '/MyDrive/Transcripts/' + TASK_NAME

# transcript = [] # array of prompt-response pairs

# def add_to_transcript(prompt, response):

#   an_entry = dict(prompt = prompt, response = response)
#   transcript.append(an_entry)

# def timestamp_string ():

#   import datetime
#   dt = datetime.datetime.now()

#   #plus 10 to get filenames in ascending sorted order
#   ts = str(dt.year) + str(dt.month + 10) + str(dt.day + 10)
#   ts = ts + dt.strftime("%H") + dt.strftime("%M") + dt.strftime("%S")
#   ts = ts + dt.strftime("%f")

#   return(ts)

# def save_transcript_on_gdrive():

#   drive.mount(MOUNT_ROOT, force_remount=True)

#   if not os.path.exists(Transcripts_Folder):
#     os.mkdir(Transcripts_Folder)

#   transcript_name = timestamp_string()
#   gdrive_fname = str(path(Transcripts_Folder, transcript_name)) +  ".txt"

#   fname = open(gdrive_fname, "w")

#   json_str = json.dumps(transcript)
#   fname.write(json_str)

#   fname.close()
#   drive.flush_and_unmount()

#   return(gdrive_fname)