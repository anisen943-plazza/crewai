import sys
import time
from plazza_analytics.crew import crew

def run():
    # Accept query from CLI or default to interactive input
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("💬 Enter your business question (type 'exit' to quit): ")
        
        # Check for exit command
        if user_query.lower() in ['exit', 'quit', 'q']:
            print("Exiting Plazza Analytics...")
            return
    
    # Basic input validation
    if not user_query or user_query.isspace():
        print("❌ Please provide a valid question.")
        return
    
    start_time = time.time()
    print(f"\n🤖 Starting Plazza Analytics Crew...\n")
    
    try:
        # Pass the user query to the CrewAI system
        result = crew.kickoff(inputs={"user_query": user_query})
        
        # Display the result
        print("\n🧠 Final Answer:")
        print(result)
        
        # Show processing time
        elapsed_time = time.time() - start_time
        print(f"\n⏱️ Processing time: {elapsed_time:.2f} seconds")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("Please try again with a different query.")

if __name__ == "__main__":
    run()