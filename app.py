from flask import Flask, render_template, request, redirect, url_for, session
# pip install -q --upgrade google-generativeai
# pip install -q --upgrade langchain
# pip install -q --upgrade langchain-google-genai

from pprint import pprint

from library import DoSomethingElse
from config import SESSION_SECRET

app = Flask(__name__)

app.secret_key = SESSION_SECRET


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/prompt/<prompt_type>')
def FileUpload(prompt_type):
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
        previous_instruction = session.get('previous_instruction', "")
        return render_template('something_else.html', previous_instruction=previous_instruction)
    elif request.method == 'POST':
        previous_instruction = session.get('previous_instruction', "")
        new_instruction = request.form.get('new_instruction', '')
        
        response, updated_previous_instruction = DoSomethingElse.do_the_work(new_instruction=new_instruction,previous_instruction=previous_instruction)
        session['previous_instruction'] = updated_previous_instruction
        return render_template('something_else_response.html', response=response)
    
@app.route('/something_else_response', methods=['GET', 'POST'])
def something_else_response():
    if request.method == 'GET':
        previous_instruction = session.get('previous_instruction', "")
        return render_template('something_else.html', previous_instruction=previous_instruction)
    elif request.method == 'POST':
        previous_instruction = session.get('previous_instruction', "")
        new_instruction = request.form.get('new_instruction', '')
        
        response, updated_previous_instruction = DoSomethingElse.do_the_work(new_instruction=new_instruction,previous_instruction=previous_instruction)
        session['previous_instruction'] = updated_previous_instruction
        return render_template('something_else_response.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
