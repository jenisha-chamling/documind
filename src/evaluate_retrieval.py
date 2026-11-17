
from src.rag_pipeline import build_rag_pipeline, ask_question

# Questions used to evaluate document retrieval
questions = [
    "What is machine learning?",
    "What is supervised learning?",
    "What is reinforcement learning?",
    "What is the difference between training and testing data?",
    "What is classification?",
    "How does an agent interact with its environment?",
    "What is overfitting?",
    "What is a prediction algorithm?",
]

# Build the retrieval pipeline once
chunks, model, index = build_rag_pipeline()

print("\nDOCUMIND RETRIEVAL EVALUATION")
print("=" * 60)

# Test each question
for number, question in enumerate(questions, start=1):

    results = ask_question(
        question,
        chunks,
        model,
        index,
        top_k=3
    )

    print(f"\nTest {number}: {question}")
    print("-" * 60)

    for rank, result in enumerate(results, start=1):
        print(
            f"Rank {rank} | "
            f"Page: {result['page']} | "
            f"Score: {result['score']:.4f}"
        )
        print(f"Text: {result['text'][:300]}")
        print()
