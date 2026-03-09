from sentence_transformers import SentenceTransformer
import chromadb
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create persistent vector DB
client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection("math_knowledge")


def load_documents():

    folder = "knowledge_base"

    docs = []

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        docs.append(text)

    return docs


def build_vector_db():

    docs = load_documents()

    embeddings = model.encode(docs)

    for i, doc in enumerate(docs):

        collection.add(
            documents=[doc],
            embeddings=[embeddings[i].tolist()],
            ids=[str(i)]
        )


def retrieve_context(query):

    embedding = model.encode([query])[0]

    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=2
    )

    docs = results["documents"]

    retrieved_docs = []

    for doc_list in docs:
        for doc in doc_list:
            retrieved_docs.append(doc)

    return retrieved_docs