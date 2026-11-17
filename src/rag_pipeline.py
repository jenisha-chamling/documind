

from src.process_pdf import process_pdf
from src.embeddings import generate_embeddings
from src.vector_store import create_vector_index, search_vector_index


def build_rag_pipeline(pdf_path="data/sample.pdf"):

    chunks = process_pdf(pdf_path)

    if not chunks:
        raise ValueError(
            f"No text chunks could be extracted from: {pdf_path}"
        )

    model, embeddings = generate_embeddings(chunks)

    index = create_vector_index(embeddings)

    return chunks, model, index


def ask_question(question, chunks, model, index, top_k=3):

    results = search_vector_index(
        question,
        chunks,
        model,
        index,
        top_k=top_k
    )

    return results



def retrieve_context(question, chunks, model, index, top_k=3):
    # Retrieve the most relevant document passages
    results = search_vector_index(
        question,
        chunks,
        model,
        index,
        top_k=top_k
    )

    return results
