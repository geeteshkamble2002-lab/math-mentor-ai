from sentence_transformers import SentenceTransformer
import torch
import os

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create a simple persistent vector DB using PyTorch
DB_PATH = "vector_db.pt"

class SimpleVectorDB:
    def __init__(self, path):
        self.path = path
        self.docs = []
        self.embeddings = None
        if os.path.exists(path):
            data = torch.load(path)
            self.docs = data["docs"]
            self.embeddings = data["embeddings"]

    def add(self, docs, embeddings):
        self.docs.extend(docs)
        if self.embeddings is None:
            self.embeddings = embeddings
        else:
            self.embeddings = torch.cat([self.embeddings, embeddings], dim=0)
        torch.save({"docs": self.docs, "embeddings": self.embeddings}, self.path)

    def query(self, query_embedding, n_results=2):
        if self.embeddings is None or len(self.docs) == 0:
            return {"documents": [[]]}
            
        # Calculate cosine similarity
        query_tensor = torch.tensor(query_embedding).unsqueeze(0).to(self.embeddings.device)
        
        similarities = torch.nn.functional.cosine_similarity(query_tensor, self.embeddings)
        
        # Get top k results
        k = min(n_results, len(self.docs))
        top_k = torch.topk(similarities, k)
        
        results = [self.docs[i] for i in top_k.indices.tolist()]
        return {"documents": [results]}

collection = SimpleVectorDB(DB_PATH)


def load_documents():
    folder = "knowledge_base"
    docs = []
    if not os.path.exists(folder):
        return docs
        
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        docs.append(text)
    return docs


def build_vector_db():
    docs = load_documents()
    if not docs:
        return
        
    embeddings = model.encode(docs, convert_to_tensor=True)
    collection.add(docs, embeddings)


def retrieve_context(query):
    # Auto-initialize the DB if empty
    if len(collection.docs) == 0:
        build_vector_db()
        
    embedding = model.encode([query])[0]
    results = collection.query(query_embedding=embedding, n_results=2)
    docs = results["documents"]

    retrieved_docs = []
    for doc_list in docs:
        for doc in doc_list:
            retrieved_docs.append(doc)

    return retrieved_docs