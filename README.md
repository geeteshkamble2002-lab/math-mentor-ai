
# 🧮 AI Math Mentor: Multi-Agent Reasoning System

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)

An advanced, multi-agent AI system designed to solve complex mathematics through text, image (OCR), or voice. This project leverages **Retrieval-Augmented Generation (RAG)**, symbolic computation, and a specialized agentic workflow to provide verified, step-by-step solutions.

---

## 🚀 Key Features

* **Multimodal Input:** Solve problems via text, uploaded images (OCR), or voice commands (Speech-to-Text).
* **Agentic Workflow:** A pipeline of specialized agents (Parser, Router, Solver, Verifier) ensures high accuracy.
* **RAG Integration:** Uses a vector database to retrieve relevant mathematical theorems and formulas.
* **Symbolic Intelligence:** Powered by SymPy for rigorous mathematical proofs and calculations.
* **Explainable AI:** Generates detailed, human-readable, step-by-step derivations.
* **Self-Learning Memory:** Remembers previously solved problems to speed up recurring queries.

---

## 🏗️ System Architecture



The system operates on a linear pipeline where each agent hands off refined data to the next:

1.  **Input Layer:** Processes Text, Images (PaddleOCR), or Audio (Whisper).
2.  **Parser Agent:** Extracts the core mathematical expression from natural language.
3.  **Router Agent:** Categorizes the problem (e.g., Calculus, Algebra, Statistics).
4.  **Memory & RAG:** Checks `ChromaDB` for similar past problems and retrieves necessary theorems.
5.  **Solver Agent:** Executes symbolic math using `SymPy`.
6.  **Verifier Agent:** Re-checks the solution for logical consistency.
7.  **Explainer Agent:** Translates the logic into a step-by-step educational guide.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | Streamlit |
| **LLM Orchestration** | LangChain / Custom Agents |
| **Math Engine** | SymPy |
| **Speech-to-Text** | OpenAI Whisper |
| **OCR** | PaddleOCR |
| **Vector Database** | ChromaDB |
| **Embeddings** | Sentence Transformers |

---

## 📂 Project Structure

```text
math-mentor-ai
├── app
│   ├── agents           # Individual Agent logic (Parser, Solver, etc.)
│   ├── pipelines        # OCR and Speech processing logic
│   ├── memory           # Persistent memory storage logic
│   └── ui               # Streamlit dashboard code
├── data                 # Local datasets and memory.json
├── scripts              # Utility scripts for DB initialization
├── vector_db            # ChromaDB persistent storage
└── requirements.txt     # Project dependencies

```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/yourusername/math-mentor-ai.git](https://github.com/yourusername/math-mentor-ai.git)
cd math-mentor-ai

```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Initialize Vector DB

```bash
python scripts/build_vector_db.py

```

### 5. Run the App

```bash
streamlit run app/ui/streamlit_app.py

```

---

## 💡 Usage Examples

* **Text:** "What is the limit of (sin x)/x as x approaches 0?"
* **Image:** Upload a photo of a handwritten quadratic equation.
* **Voice:** Click the mic and say, "Integrate x squared from 0 to 5."

---

## 🛣️ Roadmap

* [ ] Support for 3D Graph Plotting.
* [ ] Integration with LaTeX for high-quality PDF exports.
* [ ] Fine-tuning a specialized Llama-3 model for math reasoning.

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Author:** Geetesh Kamble – AI/ML Engineer