
import numpy as np

from src.process_pdf import process_pdf
from src.embeddings import generate_embeddings


def semantic_search(question, chunks, model, embeddings, top_k=3):

    # Convert the user's question into an embedding.
    query_embedding = model.encode(
        question,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # Compare the question with every chunk.
    similarity_scores = np.dot(embeddings, query_embedding)

    # Get the indices of the most similar chunks.
    top_indices = np.argsort(similarity_scores)[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append({
            "page": chunks[index]["page"],
            "text": chunks[index]["text"],
            "score": float(similarity_scores[index])
        })

    return results


if __name__ == "__main__":

    # Process the PDF.
    chunks = process_pdf("data/sample.pdf")

    if not chunks:
        print("No chunks available.")
    else:

        # Generate embeddings for all chunks.
        model, embeddings = generate_embeddings(chunks)

        # Ask a question.
        question = "What does this document contain?"

        # Search for the three most relevant chunks.
        results = semantic_search(
            question,
            chunks,
            model,
            embeddings,
            top_k=3
        )

        print("\nSemantic Search Results")
        print("----------------------")
        print(f"Question: {question}")

        for i, result in enumerate(results, start=1):

            print(f"\nResult {i}")
            print(f"Page: {result['page']}")
            print(f"Similarity score: {result['score']:.4f}")
            print(f"Text: {result['text'][:300]}")
