# 📚 Document Chatbot

A simple chatbot that answers questions based on your documents using Google's Gemini API.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🤖 Powered by Google Gemini 1.5 Flash
- 📄 Supports multiple document formats (TXT, MD, JSON, CSV, HTML, XML, PY)
- 💬 Conversational memory within sessions
- 🎨 Clean, modern chat interface
- 🔄 Easy conversation reset
- 📁 Automatic document loading from `data/` folder

## 📸 Screenshot

```
┌─────────────────────────────────────┐
│      📚 Document Chatbot            │
│   Ask questions about your docs     │
├─────────────────────────────────────┤
│ 📄 Loaded: notes.txt, guide.md      │
├─────────────────────────────────────┤
│                                     │
│ 🤖 Hello! How can I help you?       │
│                                     │
│         What is in my documents? 👤 │
│                                     │
│ 🤖 Based on your documents...       │
│                                     │
├─────────────────────────────────────┤
│ [Type your message...] [Send][Reset]│
└─────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API key ([Get one free](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/document-chatbot.git
   cd document-chatbot
   ```

2. **Create project folders**
   ```bash
   mkdir data static
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your documents**
   
   Place your documents in the `data/` folder:
   ```
   data/
   ├── notes.txt
   ├── research.md
   └── data.json
   ```

5. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your Gemini API key:
   ```
   GEMINI_API_KEY=your-api-key-here
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser**
   
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
document-chatbot/
├── app.py              # Flask backend server
├── requirements.txt    # Python dependencies
├── .env                # Your API key (create from .env.example)
├── .env.example        # Example environment file
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── data/               # Your documents go here
│   └── (your files)
└── static/
    └── index.html      # Chat frontend
```

## 📄 Supported File Types

| Extension | Description |
|-----------|-------------|
| `.pdf`    | PDF documents |
| `.txt`    | Plain text files |
| `.md`     | Markdown files |
| `.json`   | JSON data files |
| `.csv`    | CSV spreadsheets |
| `.html`   | HTML documents |
| `.xml`    | XML files |
| `.py`     | Python source code |

## 🔧 Configuration

### Changing the Port

In `app.py`, modify the last line:
```python
app.run(debug=True, port=5000)  # Change 5000 to your desired port
```

### Using a Different Gemini Model

In `app.py`, change the model name:
```python
model = genai.GenerativeModel('gemini-1.5-flash')  # or 'gemini-1.5-pro'
```

## 🛠️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serves the chat interface |
| `/chat` | POST | Send a message and get a response |
| `/reset` | POST | Reset conversation history |
| `/documents` | GET | List loaded documents |

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini API](https://ai.google.dev/) for the AI capabilities
- [Flask](https://flask.palletsprojects.com/) for the web framework

---

Made with ❤️ for a school project