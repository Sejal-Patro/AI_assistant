from models import AIModels

# Create an instance of AIModels
ai = AIModels()

def main():
    while True:
        print("\nAI Assistant - Choose an Option")
        print("1. Answer Questions")
        print("2. Summarize Text")
        print("3. Generate Creative Content")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            query = input("Ask your question: ")
            print("Answer:", ai.answer_question(query))
        elif choice == "2":
            text = input("Enter text to summarize: ")
            print("Summary:", ai.summarize_text(text))
        elif choice == "3":
            topic = input("Enter a topic for a story: ")
            print("Story:", ai.generate_content(topic))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
