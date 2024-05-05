from flask import Flask, render_template, request, redirect, url_for, session
# pip install -q --upgrade google-generativeai
# pip install -q --upgrade langchain
# pip install -q --upgrade langchain-google-genai

from pprint import pprint

from library import DoSomethingElse, Util
from config import SESSION_SECRET

app = Flask(__name__)

app.secret_key = SESSION_SECRET

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prompt/<prompt_type>')
def RenderPromptPage(prompt_type):
    custom_string = ""
    if prompt_type == "Draft the document":
        custom_string = "Enter below what document you want to create and click Do"
        return render_template('something_else.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Update document":
        custom_string = "Provide the document you want me to update:"
        return render_template('FileUpload.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Answer questions about a document":
        custom_string = "Provide below the document you want to explore:"
        return render_template('FileUpload.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Summarise a document":
        custom_string = "Provide the document you want me to summarize:"
        return render_template('FileUpload.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Something Else":
        custom_string = "Enter Below what you have in mind and click Do"
        return render_template('something_else.html', prompt_type=prompt_type, custom_string=custom_string)


@app.route('/playwithresponse', methods=['GET'])
def playwithresponse():
    prompt_type = request.args.get('prompt_type')
    custom_string = request.args.get('custom_string')
    custom_string1 = request.args.get('custom_string1')
    # Now you can use prompt_type and custom_string as needed
    return render_template('playwithresponse.html', prompt_type=prompt_type, custom_string=custom_string, custom_string1=custom_string1)


@app.route('/something_else', methods=['GET', 'POST'])
def something_else():
    if request.method == 'GET':
        print("somethingelse GET fired")
        previous_instruction = session.get('previous_instruction', "")
        custom_string = "Enter Below what you have in mind and click Do"
        return render_template('something_else.html', new_instruction=previous_instruction,custom_string=custom_string)
    elif request.method == 'POST':
        new_instruction = request.form.get('new_instruction', '')
        response, updated_previous_instruction = DoSomethingElse.do_the_work(instruction=new_instruction)
        session['previous_instruction'] = updated_previous_instruction
        Util.add_to_transcript(new_instruction,response=response)
        return render_template('something_else_response.html', response=response)


@app.route('/something_else_response', methods=['GET', 'POST'])
def something_else_response():
    if request.method == 'GET':
        previous_instruction = session.get('previous_instruction', "")
        return render_template('something_else.html', previous_instruction=previous_instruction)
    elif request.method == 'POST':
        return redirect(url_for('something_else'))


@app.route('/something_else_final', methods=['GET', 'POST'])
def something_else_final():
    download_link = url_for('download_transcript')
    return render_template('Something_else_final.html', transcript = Util.transcript, download_link=download_link)


@app.route('/download_transcript', methods=['GET'])
def download_transcript():
    transcript_content = ""
    for entry in Util.transcript:
        transcript_content += f"Prompt: {entry['prompt']}\n"
        transcript_content += f"Response: {entry['response']}\n\n"

    # Return the transcript file as a downloadable attachment
    return transcript_content, 200, {'Content-Type': 'text/plain', 'Content-Disposition': 'attachment; filename="transcript.txt"'}



if __name__ == '__main__':
    app.run(debug=True)
