from search import search_web
from llm import generate_answer

def run():
    print("Program started...\n")

    query = input("Ask something: ")

    # Step 1: Get search results
    links = search_web(query)

    if not links:
        print("\nNo search results found. Answering generally...\n")

    print("\n--- ANSWER ---\n")

    # Step 2: Generate answer
    answer = generate_answer(query, links)
    print(answer)

    print("\n--- SOURCES ---\n")

    # Step 3: Show sources
    if links:
        for link in links:
            print(link)
    else:
        print("No sources available")

if __name__ == "__main__":
    run()