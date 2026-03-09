import os
import sys

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

from app.pipelines.rag_pipeline import build_vector_db

build_vector_db()

print("Vector database built successfully")