
from src.rag_pipeline import build_rag_pipeline, ask_question

# Build the retrieval pipeline
chunks, model, index = build_rag_pipeline()

# Ask a question
question = "What is reinforcement learning and how does an agent learn from experience?"

# Retrieve relevant passages
results = ask_question(
    question,
    chunks,
    model,
    index
)

# Display results
for result in results:
    print(f"\nPage: {result['page']}")
    print(f"Score: {result['score']:.4f}")
    print(f"Text: {result['text']}")
    print("-" * 60)
