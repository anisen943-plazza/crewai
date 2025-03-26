import sys
from plazza_analytics.crew import crew

def run():
    # Accept query from CLI or default to a test prompt
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("💬 Enter your business question: ")

    print("\n🤖 Starting Plazza Analytics Crew...\n")

    # Note: We're using "user_query" here to match the template in tasks.yaml
    result = crew.kickoff(inputs={"user_query": user_query})
    
    print("\n🧠 Final Answer:")
    print(result)

if __name__ == "__main__":
    run()