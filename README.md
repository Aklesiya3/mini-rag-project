# Mini RAG — Document Question Answering

A simple **Retrieval-Augmented Generation (RAG)** system built from scratch using **Python, Gemini, and ChromaDB**.

This project was built to understand how RAG works internally without using frameworks such as LangChain or LlamaIndex.

## 🚀 What is RAG?

RAG (Retrieval-Augmented Generation) allows an AI model to answer questions using information from external documents.

Instead of relying only on the model's existing knowledge, the system:

```text
Document
   ↓
Chunking
   ↓
Embeddings
   ↓
ChromaDB
   ↓
User Question
   ↓
Retrieve Relevant Chunks
   ↓
Gemini
   ↓
Answer
```

## ✨ Features

* 📄 Loads information from a text document
* ✂️ Splits documents into smaller chunks
* 🔢 Converts text into vector embeddings
* 🗄️ Stores embeddings in ChromaDB
* 🔍 Retrieves relevant chunks using vector similarity
* 🤖 Uses Google Gemini to generate answers
* 🛡️ Avoids answering questions when the information isn't present in the provided documents
* 🧩 Built without LangChain or LlamaIndex

## 🛠️ Technologies

* **Python**
* **Google Gemini API**
* **Gemini Embedding Model**
* **ChromaDB**
* **python-dotenv**

## 📁 Project Structure

```text
mini-rag/
│
├── data/
│   └── notes.txt
│
├── main.py
├── requirements.txt
├── .gitignore
└── .env
```

> `.env` contains the API key and should never be committed to GitHub.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd mini-rag
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload your `.env` file.

### 5. Run the project

```bash
python main.py
```

You will see:

```text
Ask a question:
```

Enter a question related to the information in `data/notes.txt`.

For example:

```text
What is photosynthesis?
```

The system retrieves relevant information and generates an answer using Gemini.

## 🧪 Example

### Question

```text
What is photosynthesis?
```

### Answer

```text
Photosynthesis is the process by which green plants
convert light energy into chemical energy.
```

If you ask something that isn't contained in the document:

```text
What is the capital of France?
```

The system responds:

```text
I don't know based on the provided documents.
```

This demonstrates that the answer is grounded in the provided document rather than simply relying on the model's general knowledge.

## 🧠 RAG Pipeline

The project follows six main steps:

### 1. Ingest

Read the document from `data/notes.txt`.

### 2. Chunk

Split the document into smaller pieces so they can be searched efficiently.

### 3. Embed

Convert each chunk into a numerical vector using a Gemini embedding model.

### 4. Store

Store the chunks and their embeddings in ChromaDB.

### 5. Retrieve

Convert the user's question into an embedding and search ChromaDB for the most relevant chunks.

### 6. Generate

Send the retrieved chunks and the user's question to Gemini, which generates the final answer.

## 🎯 Purpose

This project is part of my learning journey into **Large Language Models and AI Engineering**.

The main goal was to understand the fundamentals of RAG by building the pipeline manually before using higher-level frameworks.

## 🔮 Future Improvements

Possible improvements include:

* Better semantic chunking
* Metadata and source citations
* Multiple documents
* Multiple subjects
* Hybrid search
* Reranking
* Retrieval evaluation with Ragas
* Web-based user interface
* Conversation history
* Turning the system into a full Study Assistant

## 👩‍💻 Author

**Aklesiya Endalkachew**

Software Engineering Student | UI/UX Designer | AI/LLM Learner
