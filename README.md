# DocuMind – PDF Semantic Search and Retrieval System

DocuMind is a Python-based document retrieval prototype that enables users to search PDF documents using natural-language queries.

It extracts text from PDF files, divides the content into smaller chunks, converts those chunks into semantic embeddings, and retrieves relevant passages using similarity search.

The project explores the retrieval component of a Retrieval-Augmented Generation (RAG) workflow.

## Features

- **PDF Text Extraction:** Extracts text and page information using PyMuPDF.
- **Text Chunking:** Splits extracted content into smaller, overlapping chunks while preserving page metadata.
- **Semantic Embeddings:** Generates 384-dimensional embeddings using Sentence Transformers.
- **NumPy Semantic Search:** Implements similarity search using normalized vector dot products.
- **FAISS Vector Search:** Creates a FAISS index for similarity-based document retrieval.
- **Retrieval Evaluation:** Evaluates retrieval relevance using predefined natural-language questions.

## Architecture

```text
                 PDF Document
                      |
                      v
              PDF Text Extraction
                   PyMuPDF
                      |
                      v
                 Text Chunking
              (Page Information)
                      |
                      v
              Embedding Generation
           Sentence Transformers
              all-MiniLM-L6-v2
                      |
                      v
               +------+------+
               |             |
               v             v
          NumPy Search   FAISS Index
               |             |
               +------+------+
                      |
                      v
             Natural Language Query
                      |
                      v
                Query Embedding
                      |
                      v
              Similarity Search
                      |
                      v
             Top-K Relevant Passages
```

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Semantic embedding generation |
| all-MiniLM-L6-v2 | Pretrained embedding model |
| NumPy | Numerical operations and similarity calculations |
| FAISS | Vector indexing and similarity search |

## Project Structure

```text
documind/
│
├── data/
│   └── sample.pdf
│
├── src/
│   ├── __init__.py
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── process_pdf.py
│   ├── embeddings.py
│   ├── semantic_search.py
│   ├── vector_store.py
│   ├── rag_pipeline.py
│   ├── test_rag.py
│   └── evaluate_retrieval.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/jenisha-chamling/documind.git
cd documind
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add a PDF document

Place your PDF file inside the `data/` directory.

The default document is:

```text
data/sample.pdf
```

The first execution downloads the pretrained embedding model. Subsequent executions can use the locally cached model.

## Usage

### Run the main retrieval pipeline

```bash
python -m src.test_rag
```

### Run NumPy-based semantic search

```bash
python -m src.semantic_search
```

### Run retrieval evaluation

```bash
python -m src.evaluate_retrieval
```

### Use a different PDF document

The retrieval pipeline accepts a configurable PDF path:

```python
from src.rag_pipeline import build_rag_pipeline, ask_question

chunks, model, index = build_rag_pipeline("data/your_document.pdf")

results = ask_question(
    "What is machine learning?",
    chunks,
    model,
    index,
    top_k=3
)

for result in results:
    print("Page:", result["page"])
    print("Similarity:", result["score"])
    print("Passage:", result["text"])
```

## Retrieval Evaluation

The retrieval pipeline was evaluated using eight natural-language questions covering different topics from the sample machine learning document.

Example questions:

- What is machine learning?
- What is supervised learning?
- What is reinforcement learning?
- What is the difference between training and testing data?
- What is classification?
- How does an agent interact with its environment?
- What is overfitting?
- What is a prediction algorithm?

Retrieved passages were manually inspected to assess their relevance.

### Example Retrieval Result

**Query:** What is reinforcement learning?

**Retrieved passage:** A passage on page 72 defines reinforcement learning as an area of machine learning in which an agent learns through interactions with an environment.

This demonstrates how the system retrieves document content relevant to a natural-language query.

### Implementation Verification

| Component | Result |
|---|---|
| Extracted text chunks | 568 |
| Generated embedding vectors | 568 |
| Embedding dimensions | 384 |
| FAISS index | 568 vectors |
| NumPy and FAISS comparison | Matching top-three results |
| Dependency compatibility | Passed `pip check` |

These figures represent the current sample-document run. They are implementation checks, not a formal retrieval accuracy measurement.

**Note:** Similarity scores indicate how closely a passage matches a query in embedding space. They do not guarantee that the retrieved passage fully answers the question.

## Sample Document and Attribution

**Document:** Introduction to Machine Learning

- Author: Philip S. Thomas
- Institution: University of Massachusetts Amherst
- Course: COMPSCI 389, Spring 2022
- License: CC0 1.0 Universal

Source: https://people.cs.umass.edu/~pthomas/courses/COMPSCI_389_Spring2022/389_S22.pdf

The author has dedicated the document to the public domain under CC0.

## Current Limitations

- The system retrieves relevant passages but does not generate answers using an LLM.
- Scanned PDFs without extractable text are not processed using OCR.
- Retrieval relevance is assessed through manual inspection rather than a formal benchmark.
- The current implementation processes one PDF at a time.
- The FAISS index is built in memory and is not persisted between runs.

## Future Improvements

- Integrate an LLM for context-grounded answer generation.
- Support multiple PDF documents.
- Persist and reload FAISS indexes.
- Improve document-aware chunking and retrieval evaluation.
- Develop a simple interface for document uploads and queries.


---

*DocuMind is an educational project exploring semantic search, vector embeddings, and document retrieval as foundational components of RAG systems.*