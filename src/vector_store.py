
import faiss
import numpy as np

from src.process_pdf import process_pdf
from src.embeddings import generate_embeddings


def create_vector_index(embeddings):

    # Get the number of dimensions in each embedding.
    dimension = embeddings.shape[1]

    # Create an exact inner-product search index.
    index = faiss.IndexFlatIP(dimension)

    # Add the embeddings to the index.
    index.add(embeddings.astype("float32"))

    return index


def search_vector_index(question, chunks, model, index, top_k=3):

    # Convert the question into an embedding.
    query_embedding = model.encode(
        question,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    # FAISS expects a 2D float32 array.
    query_embedding = np.array(
        [query_embedding],
        dtype="float32"
    )

    # Search the index.
    scores, indices = index.search(query_embedding, top_k)

    results = []

    for score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        results.append({
            "page": chunks[idx]["page"],
            "text": chunks[idx]["text"],
            "score": float(score)
        })

    return results


if __name__ == "__main__":

    # Process the PDF.
    chunks = process_pdf("data/sample.pdf")

    if not chunks:
        print("No chunks available.")
    else:

        # Generate embeddings.
        model, embeddings = generate_embeddings(chunks)

        # Create the FAISS index.
        index = create_vector_index(embeddings)

        print("\nFAISS Index Summary")
        print("-------------------")
        print(f"Total vectors stored: {index.ntotal}")
        print(f"Vector dimensions: {index.d}")

        # Search the index.
        question = "What does this document contain?"

        results = search_vector_index(
            question,
            chunks,
            model,
            index,
            top_k=3
        )

        print("\nFAISS Search Results")
        print("-------------------")
        print(f"Question: {question}")

        for i, result in enumerate(results, start=1):

            print(f"\nResult {i}")
            print(f"Page: {result['page']}")
            print(f"Similarity score: {result['score']:.4f}")
            print(f"Text: {result['text'][:300]}")
