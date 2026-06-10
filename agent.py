import os
import anthropic
from tools import TOOL_DEFINITIONS, execute_tool

MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT = """You are a helpful assistant that answers questions about GitHub repositories.
You have access to tools that can fetch repository metadata, list a user's repositories, 
and retrieve recent commit history. Use them whenever the user asks about a GitHub user or repo.
Be concise and factual in your responses."""


def run_agent() -> None:
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    conversation: list[anthropic.types.MessageParam] = []

    print("GitHub Agent — ask me anything about a GitHub user or repo.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        if not user_input:
            continue

        # Add the user's message to conversation history
        conversation.append({"role": "user", "content": user_input})

        # Keep calling Claude until we get a final text response
        # (there may be multiple tool calls before the final answer)
        while True:
            response = client.messages.create(
                model=MODEL,
                max_tokens=1024,
                system=SYSTEM_PROMPT,
                tools=TOOL_DEFINITIONS,
                messages=conversation,
            )

            # Add Claude's response to conversation history
            conversation.append({"role": "assistant", "content": response.content})

            # If Claude is done (no tool calls), print the answer and break
            if response.stop_reason == "end_turn":
                for block in response.content:
                    if hasattr(block, "text"):
                        print(f"\nAgent: {block.text}\n")
                break

            # If Claude wants to use a tool, execute it and send the result back
            if response.stop_reason == "tool_use":
                tool_results = []

                for block in response.content:
                    if block.type == "tool_use":
                        print(f"[calling tool: {block.name}]")
                        result = execute_tool(block.name, block.input)
                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        })

                # Send tool results back to Claude
                conversation.append({"role": "user", "content": tool_results})
                # Loop continues — Claude will now reason over the results


if __name__ == "__main__":
    run_agent()