
import re


def split_text(pages, chunk_size=500, overlap=50):

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be non-negative and smaller than chunk_size."
        )

    chunks = []
    pending_heading = None

    for page in pages:

        text = page["text"].strip()
        page_number = page["page"]

        if not text:
            continue

        # Carry a standalone heading into the next page.
        if pending_heading:
            text = pending_heading + "\n" + text
            pending_heading = None

        # Detect pages containing only a short heading.
        if len(text) <= 80 and not re.search(r"[.!?]", text):
            pending_heading = text
            continue

        # Split text into sentences.
        sentences = re.split(r"(?<=[.!?])\s+", text)

        units = []

        for sentence in sentences:
            sentence = sentence.strip()

            if not sentence:
                continue

            if len(sentence) <= chunk_size:
                units.append(sentence)
            else:
                step = chunk_size - overlap

                for start in range(0, len(sentence), step):
                    units.append(sentence[start:start + chunk_size])

        start = 0

        while start < len(units):

            current_chunk = []
            current_length = 0
            end = start

            while end < len(units):

                sentence = units[end]
                extra_length = len(sentence)

                if current_chunk:
                    extra_length += 1

                if current_length + extra_length > chunk_size:
                    break

                current_chunk.append(sentence)
                current_length += extra_length
                end += 1

            if not current_chunk:
                start += 1
                continue

            chunks.append({
                "page": page_number,
                "text": " ".join(current_chunk)
            })

            if end >= len(units):
                break

            next_start = end
            overlap_length = 0

            while next_start > start:
                previous_sentence = units[next_start - 1]

                if overlap_length + len(previous_sentence) > overlap:
                    break

                overlap_length += len(previous_sentence) + 1
                next_start -= 1

            start = next_start if next_start > start else end

    return chunks
