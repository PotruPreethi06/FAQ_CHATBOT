# FAQ Chatbot using NLP

## Overview
This project is a simple FAQ Chatbot built using Python and Natural Language Processing (NLP). The chatbot answers user queries by comparing them with a predefined set of frequently asked questions and returning the most relevant response.

## Features
- Interactive command-line chatbot
- NLP-based text processing
- FAQ matching using TF-IDF Vectorization
- Similarity measurement using Cosine Similarity
- Fast and lightweight implementation
- Easy to customize with new FAQs

## Technologies Used
- Python
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## Project Structure

```text
FAQ_CHATBOT/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/FAQ_CHATBOT.git
cd FAQ_CHATBOT
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install scikit-learn
```

## Running the Chatbot

```bash
python chatbot.py
```

Example:

```text
FAQ Chatbot Started

You: What is AI?
Bot: AI stands for Artificial Intelligence.

You: Who developed Python?
Bot: Python was developed by Guido van Rossum.
```

## How It Works

1. Stores a list of FAQ questions and answers.
2. Converts questions into numerical vectors using TF-IDF.
3. Converts the user's query into a vector.
4. Computes cosine similarity between the query and stored FAQs.
5. Returns the answer corresponding to the most similar question.

## Future Improvements

- GUI using Tkinter
- Voice-based interaction
- Database integration
- Web deployment using Flask or Streamlit
- Dynamic FAQ management
## final output:
<img width="857" height="195" alt="image" src="https://github.com/user-attachments/assets/887648a1-6147-4bee-902c-f90fbe917128" />
