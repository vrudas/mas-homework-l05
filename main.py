import uuid

from agent import agent


def main():
    print("Research Agent with RAG (type 'exit' to quit)")
    print("-" * 40)

    # Create a unique thread ID for this conversation session
    thread_id = str(uuid.uuid4())

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        for chunk in agent.stream(
            {"messages": [("user", user_input)]},
            config={"configurable": {"thread_id": thread_id}}
        ):
            if "model" in chunk and "messages" in chunk["model"]:
                for msg in chunk["model"]["messages"]:
                    if hasattr(msg, "tool_calls") and msg.tool_calls:
                        for call in msg.tool_calls:
                            print(f"-> {call["name"]} {call["args"]}"[:200])

                    if hasattr(msg, "content") and msg.content:
                        print(f"\nAgent: {msg.content}")


if __name__ == "__main__":
    main()
