# BlenderBot Chatbot with Gradio UI

A conversational AI chatbot powered by Facebook's BlenderBot (400M distill) transformer model.  
This project demonstrates how to build, Dockerize, and deploy a chatbot with a user-friendly Gradio interface, ready for deployment on IBM Code Engine or any container platform.

---

## Features

- Uses Hugging Face Transformers `facebook/blenderbot-400M-distill` model for state-of-the-art conversational AI.
- Maintains conversation history with simple context window management.
- Interactive web UI built with Gradio for easy testing and demo.
- Dockerfile included for containerized deployment.
- Instructions to deploy on IBM Code Engine serverless container platform.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Docker (optional, for container builds)
- IBM Cloud CLI & Code Engine CLI (for IBM deployment)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/blenderbot-chatbot.git
cd blenderbot-chatbot
pip install -r requirements.txt
```

### Running Locally

```bash
python demo.py
```

Open your browser at http://localhost:7860 to interact with the chatbot.

### Docker
Build and run the Docker container:

```bash
docker build -t blenderbot-chatbot .
docker run -p 7860:7860 blenderbot-chatbot
```

### Deploy on IBM Code Engine
Follow the IBM Code Engine instructions to build and deploy this containerized app with a public URL.

## Project Structure
```bash
├── run_Chatbot.py    # Main CLI app
├── chatbot.py        # Chatbot class and logic
├── gradio_app.py     # Gradio Interface
├── requirements.txt  # Python dependencies
├── Dockerfile        # Docker container setup
├── README.md         # Project documentation
├── LICENSE           # License
├── app.py            # Flask app
└── .gitignore        # Git ignore rules
```

### Usage
Type your messages in the input box.

The chatbot keeps context for better conversational flow.

Use /reset command to clear the conversation history.

### License
See the LICENSE file for details.

## Acknowledgements

Hugging Face Transformers
Facebook BlenderBot
Gradio

## Notes:
For the front end I used the free front end offered by IBM here @ https://github.com/ibm-developer-skills-network/LLM_application_chatbot/tree/main

### Feel free to reach out if you want to collaborate or have any questions!
