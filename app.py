from flask import Flask, render_template, request, jsonify
from models import AIModels
from feedback import FeedbackSystem

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'

# Initialize components
models = AIModels()
feedback = FeedbackSystem()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            question = request.form.get('question')
            text = request.form.get('text')
            prompt = request.form.get('prompt')

            if question:
                response = models.answer_question(question)
                function_name = 'Question Answering'
            elif text:
                response = models.summarize_text(text)
                function_name = 'Text Summarization'
            elif prompt:
                response = models.generate_content(prompt)
                function_name = 'Creative Generation'
            else:
                return jsonify({'response': 'Error: No valid input provided', 'function': 'Error'}), 400

            return jsonify({'response': response, 'function': function_name})

        except KeyError as ke:
            return jsonify({'response': f"Key Error: {str(ke)}", 'function': 'Error'}), 400
        except Exception as e:
            return jsonify({'response': f"Server Error: {str(e)}", 'function': 'Error'}), 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
