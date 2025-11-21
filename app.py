import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai
from pathlib import Path

app = Flask(__name__, static_folder='static')
CORS(app)

# Configure Gemini API
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-pro')

# Store conversation history
conversation_history = []

def load_documents(data_folder='data'):
    """Load all documents from the data folder."""
    documents = []
    data_path = Path(data_folder)
    
    if not data_path.exists():
        print(f"Warning: '{data_folder}' folder not found. Creating it...")
        data_path.mkdir(exist_ok=True)
        return ""
    
    supported_extensions = {'.txt', '.md', '.py', '.json', '.csv', '.html', '.xml'}
    
    for file_path in data_path.rglob('*'):
        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append(f"--- Document: {file_path.name} ---\n{content}\n")
                    print(f"Loaded: {file_path.name}")
            except Exception as e:
                print(f"Error loading {file_path}: {e}")
    
    return "\n".join(documents)

# Load documents at startup
DOCUMENTS_CONTEXT = load_documents()
print(f"Loaded {len(DOCUMENTS_CONTEXT)} characters of document content")

SYSTEM_PROMPT = f"""You are a helpful assistant that answers questions based on the provided documents. 
Use the information from these documents to answer user questions accurately.
If the answer cannot be found in the documents, say so clearly.

Here are the documents you have access to:

{DOCUMENTS_CONTEXT}

---
Now answer the user's questions based on the above documents."""

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history
    
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Build conversation with context
    conversation_history.append({"role": "user", "parts": [user_message]})
    
    try:
        # Create chat with system prompt
        chat = model.start_chat(history=[])
        
        # Send system prompt + conversation
        full_prompt = SYSTEM_PROMPT + "\n\nConversation so far:\n"
        for msg in conversation_history[:-1]:
            role = "User" if msg["role"] == "user" else "Assistant"
            full_prompt += f"{role}: {msg['parts'][0]}\n"
        full_prompt += f"\nUser: {user_message}"
        
        response = chat.send_message(full_prompt)
        assistant_message = response.text
        
        conversation_history.append({"role": "model", "parts": [assistant_message]})
        
        return jsonify({'response': assistant_message})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'Conversation reset'})

@app.route('/documents', methods=['GET'])
def get_documents():
    """Return list of loaded documents."""
    data_path = Path('data')
    if not data_path.exists():
        return jsonify({'documents': []})
    
    docs = [f.name for f in data_path.rglob('*') if f.is_file()]
    return jsonify({'documents': docs})

if __name__ == '__main__':
    app.run(debug=True, port=5000)