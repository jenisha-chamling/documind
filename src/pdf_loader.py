
import pymupdf


def extract_text(pdf_path):

    try:
        document = pymupdf.open(pdf_path)

        if document.page_count == 0:
            raise ValueError("The PDF contains no pages.")

        extracted_pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text").strip()

            if not text:
                print(f"Warning: Page {page_number} contains no extractable text.")

            extracted_pages.append({
                "page": page_number,
                "text": text
            })

        return extracted_pages

    except (FileNotFoundError, ValueError, pymupdf.FileDataError) as error:
        print(f"PDF processing error: {error}")
        return []

    finally:
        if "document" in locals():
            document.close()


if __name__ == "__main__":

    pdf_path = "data/sample.pdf"

    pages = extract_text(pdf_path)

    print(f"\nTotal pages extracted: {len(pages)}")

    for page in pages:
        print(f"\n--- Page {page['page']} ---")
        print(page["text"])
