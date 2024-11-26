from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as ai

app = Flask(__name__)
CORS(app)

# Replace with your Google API Key
API_KEY = "AIzaSyB7yd0G0z_1PshFcHyRQi3PjHUSLjGwBnc"
ai.configure(api_key=API_KEY)

@app.route('/chat', methods=['POST'])
def chat_with_ai():
    try:
        data = request.json
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"response": "கேள்வி உள்ளிடவும்!"})  # "Please input a question!"

        # Generate response using Google Generative AI
        response = ai.generate_text(prompt=user_message)
        if response and response.candidates:
            ai_response = response.candidates[0].text.strip()
        else:
            ai_response = "பதிலளிக்க முடியவில்லை. மீண்டும் முயற்சிக்கவும்."  # "Unable to respond. Please try again."

        return jsonify({"response": ai_response})
    except Exception as e:
        return jsonify({"response": f"சர்வர் பிழை: {str(e)}"})  # "Server error"

if __name__ == '__main__':
    app.run(debug=True)
