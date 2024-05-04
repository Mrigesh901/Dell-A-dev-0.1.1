from flask import Flask, render_template, request, redirect, url_for, session
# pip install -q --upgrade google-generativeai
# pip install -q --upgrade langchain
# pip install -q --upgrade langchain-google-genai

from pprint import pprint

from library import paraphrase, DoSomethingElse
from config import SESSION_SECRET

app = Flask(__name__)

app.secret_key = SESSION_SECRET


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/prompt/<prompt_type>')
def screen1(prompt_type):
    custom_string = ""
    if prompt_type == "Paraphrase the text":
        custom_string = "Provide the text you want me to paraphrase:"
        return render_template('paraphrase_template.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Draft the document":
        custom_string = "Enter below what document you want to create and click Do"
        return render_template('something_else.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Update document":
        custom_string = "Provide the document you want me to update:"
        return render_template('screen1.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Answer questions about a document":
        custom_string = "Provide below the document you want to explore:"
        return render_template('screen1.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Summarise a document":
        custom_string = "Provide the document you want me to summarize:"
        return render_template('screen1.html', prompt_type=prompt_type, custom_string=custom_string)

    elif prompt_type == "Something Else":
        custom_string = "Enter Below what you have in mind and click Do"
        return render_template('something_else.html', prompt_type=prompt_type, custom_string=custom_string)



@app.route('/screen2', methods=['GET'])
def screen2():
    prompt_type = request.args.get('prompt_type')
    custom_string = request.args.get('custom_string')
    custom_string1 = request.args.get('custom_string1')
    # Now you can use prompt_type and custom_string as needed
    return render_template('screen2.html', prompt_type=prompt_type, custom_string=custom_string, custom_string1=custom_string1)


@app.route('/submit_follow_up', methods=['POST'])
def submit_follow_up():
    custom_prompt = request.form.get('customPrompt', '')

    # Process custom prompt if needed
    
    return redirect(url_for('index'))



@app.route('/submit_paraphrase', methods=['POST'])
def submit_paraphrase():
    paraphrase_text = request.form.get('ParaphraseText', '')  # Get the value of inputText from the form
    style = request.form.get('ParaphraseStyle', '')  # Get the value of style from the form
    
    paraphrase.set_prompt_softwired()

    # Call set_hardwired function with the extracted values
    output=paraphrase.paraphrase_softwired(paraphrase_text, style)
    return render_template('result.html', result=output)



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


if __name__ == '__main__':
    app.run(debug=True)
