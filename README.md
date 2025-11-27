# 📘 RAG Sanskrit Project  
### Retrieval-Augmented Generation System for Sanskrit Text Understanding  

---

## 🚀 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline designed for **Sanskrit** question-answering.  
It combines **semantic retrieval** using embeddings and **answer generation** using *Llama 3 via Ollama*.

Sanskrit has limited digital resources and complex grammar. RAG helps overcome this by grounding the model in **actual Sanskrit text** retrieved from the document.

---

## 🧠 Features

- Extracts Sanskrit text from DOCX files  
- Cleans & preprocesses classical text  
- Splits into overlapping text chunks  
- Generates embeddings using Sentence Transformers  
- Stores vectors in **ChromaDB**  
- Retrieves semantically relevant Sanskrit passages  
- Generates grounded answers using **Llama 3 (Ollama)**  
- Works offline after initial setup  
- Fully modular Python codebase  

---

## 📂 Folder Structure

RAG_Sanskrit_RohanSoni/
│
├── code/
│ ├── rag_pipeline.py
│ ├── loader.py
│ ├── preprocess.py
│ ├── chunker.py
│ ├── embedder.py
│ ├── vectorstore_chroma.py
│ ├── retriever.py
│ ├── generator_ollama.py
│ └── init.py
│
├── data/
│ └── Rag-docs-fixed.docx
│
├── report/
│ └── RAG_Sanskrit_Project_Report.pdf
│
├── requirements.txt
└── README_Project.md


---

## 🔧 Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3 |
| Embedding Model | Sentence Transformers (MiniLM Multilingual) |
| Vector Store | ChromaDB |
| LLM | Llama 3 (via Ollama) |
| Storage Backend | DuckDB + Parquet |
| Libraries Used | numpy, python-docx, sentence-transformers, requests |

---

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/<your-username>/RAG_Sanskrit_RohanSoni.git
cd RAG_Sanskrit_RohanSoni

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Install Ollama

Download here: https://ollama.com/download

Pull the model:

ollama pull llama3


Ensure Ollama is running in the background.

▶️ Running the Project

Go to the code directory:

cd code
python rag_pipeline.py


You will see:

Index built. Ready to query.
Enter query:


Try a Sanskrit query such as:

मूर्खभृत्यस्य कथायाः सारं कथय।

🧪 Example Output
User Query
मूर्खभृत्यस्य कथायाः सारं कथय।

Retrieved Chunks (from Vector Store)
"अरे शंखनाद, गच्छ आपणम्..."  
"श्वानशावकं सन्चिकायाम् क्षिपति..."  
"दुग्धं दोरकेण बद्ध्वा मार्गे पतति..."

Generated Answer (Llama Output)
मूर्खभृत्यस्य कथा मूर्खताजन्यदोषं दर्शयति।
अज्ञतया कृतकार्याणि सर्वं विनाशं जनयन्ति...

🛠️ System Architecture
DOCX → Preprocess → Chunk → Embed → ChromaDB → Retrieve → Llama 3 → Answer
