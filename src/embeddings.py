
from sentence_transformers import SentenceTransformer
from src.process_pdf import process_pdf


def generate_embeddings(chunks):

    # Load a pretrained embedding model.
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Extract text from each chunk.
    texts = [chunk["text"] for chunk in chunks]

    # Convert text into numerical vectors.
    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return model, embeddings


if __name__ == "__main__":

    # Process the PDF.
    chunks = process_pdf("data/sample.pdf")

    if not chunks:
        print("No chunks available for embedding.")
    else:

        model, embeddings = generate_embeddings(chunks)

        print("\nEmbedding Generation Summary")
        print("-----------------------------")

        print(f"Total chunks: {len(chunks)}")
        print(f"Embedding shape: {embeddings.shape}")
        print(f"Vector dimensions: {embeddings.shape[1]}")

        print("\nFirst chunk:")
        print(chunks[0]["text"][:200])

        print("\nFirst 10 embedding values:")
        print(embeddings[0][:10])
