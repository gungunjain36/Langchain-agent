from agent.agent import run_agent

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = run_agent(query)
    print("AI:", response)
