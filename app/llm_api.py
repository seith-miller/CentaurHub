from flask import Blueprint, request, jsonify, current_app
import openai

bp = Blueprint('llm_api', __name__)

@bp.route('/send_prompt', methods=['POST'])
def send_prompt():
    prompt = request.form['prompt']
    openai.api_key = current_app.config['OPENAI_API_KEY']
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150
        )
        text_response = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        text_response = str(e)

    return jsonify({'response': text_response})
