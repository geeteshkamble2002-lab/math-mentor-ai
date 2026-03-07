import os

directories = [
    "app/agents",
    "app/pipelines",
    "app/tools",
    "app/memory",
    "app/ui",
    "knowledge_base",
    "scripts",
    "data",
    "vector_db"
]

def create_folders():
    for folder in directories:
        os.makedirs(folder, exist_ok=True)
        print(f"Created: {folder}")

if __name__ == "__main__":
    create_folders()



from pathlib import Path

# List of files to create
files = [
    "run_app.py",
    "README.md",
    ".env.example",
    "app/ui/streamlit_app.py",
    "app/pipelines/ocr_pipeline.py",
    "app/pipelines/audio_pipeline.py",
    "app/pipelines/rag_pipeline.py",
    "app/agents/parser_agent.py",
    "app/agents/router_agent.py",
    "app/agents/solver_agent.py",
    "app/agents/verifier_agent.py",
    "app/agents/explainer_agent.py",
    "app/memory/memory_store.py",
    "app/tools/sympy_solver.py"
]

for file_path in files:
    path = Path(file_path)
    # Ensure the parent directory exists before creating the file
    path.parent.mkdir(parents=True, exist_ok=True)
    # Create the file (equivalent to 'touch')
    path.touch(exist_ok=True)
    print(f"Created: {file_path}")

