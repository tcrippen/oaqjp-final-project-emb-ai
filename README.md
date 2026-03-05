# AI Emotion Detection Web Application

This project is a Flask-based web application that performs basic emotion detection from text input.  
It was developed as part of the IBM Developing AI Applications with Python and Flask certification.

## Project Structure

oaqjp-final-project-emb-ai
│
├── app.py
├── requirements.txt
├── static/
├── templates/
├── reports/
│   └── screenshots/
└── README.md


## Environment Setup

1. Clone the repository

git clone https://github.com/tcrippen/oaqjp-final-project-emb-ai.git

2. Navigate to the project folder

cd oaqjp-final-project-emb-ai

3. Create a virtual environment

py -3.14 -m venv .venv

4. Activate the virtual environment

PowerShell:
.\.venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt


## Running the Application

Start the Flask server:

python app.py

The application will start at:

http://127.0.0.1:5000


## Testing the Emotion Endpoint

Example PowerShell request:

Invoke-RestMethod -Uri "http://127.0.0.1:5000/emotion" -Method POST -ContentType "application/json" -Body '{"text":"I am happy today"}'

Example JSON response:

{
  "text": "I am happy today",
  "emotion": "joy"
}


## Screenshots

Screenshots showing the environment setup, running application, and endpoint test are stored in:

reports/screenshots
