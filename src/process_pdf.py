
from src.pdf_loader import extract_text
from src.text_splitter import split_text


def process_pdf(pdf_path):

    # Step 1: Extract text from the PDF.
    pages = extract_text(pdf_path)

    if not pages:
        print("No pages could be extracted.")
        return []

    # Step 2: Split extracted text into chunks.
    chunks = split_text(
        pages,
        chunk_size=500,
        overlap=50
    )

    return chunks


if __name__ == "__main__":

    pdf_path = "data/sample.pdf"

    chunks = process_pdf(pdf_path)

    print("\nPDF Processing Summary")
    print("----------------------")

    print(f"Total chunks created: {len(chunks)}")

    for index, chunk in enumerate(chunks[:2], start=1):

        print(f"\n--- Chunk {index} ---")
        print(f"Source page: {chunk['page']}")
        print(f"Characters: {len(chunk['text'])}")
        print(chunk["text"])
