import os
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. Check your .env file."
    )

client = genai.Client(api_key=api_key)


chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_or_create_collection(
    name="study_notes"
)


file_path = Path("data/notes.txt")

if not file_path.exists():
    raise FileNotFoundError(
        "data/notes.txt was not found."
    )

text = file_path.read_text(
    encoding="utf-8"
)



def create_chunks(text, chunk_size=300, overlap=50):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


chunks = create_chunks(text)

print(f"Number of chunks: {len(chunks)}")


def create_embedding(text):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    return response.embeddings[0].values


embeddings = []

for chunk in chunks:
    embedding = create_embedding(chunk)
    embeddings.append(embedding)


print(f"Created {len(embeddings)} embeddings.")
print(f"Vector dimensions: {len(embeddings[0])}")



collection.upsert(
    ids=[
        f"chunk-{i}"
        for i in range(len(chunks))
    ],
    documents=chunks,
    embeddings=embeddings
)

print(f"Stored {len(chunks)} chunks in Chroma.")

def search_documents(query, n_results=3):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(n_results, len(chunks))
    )

    return results


def generate_answer(question, context):

    prompt = f"""
You are a study assistant.

Answer the question using ONLY the information
provided in the context.

If the answer cannot be found in the context,
say:

"I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


question = input("\nAsk a question: ")


results = search_documents(question)

retrieved_documents = results["documents"][0]

context = "\n\n".join(
    retrieved_documents
)


answer = generate_answer(
    question,
    context
)


print("\n--- Answer ---")
print(answer)