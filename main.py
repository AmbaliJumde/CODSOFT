def recomm(category):
    recomms = {
        "movies": [
            "Chhichhore by Nitesh Tiwar",
            "Brahmastra by Ayan Mukherj",
            "Oppenheimer by Christoph",
            "Inception by Christopher",
            "Avengers Endgame by Russo Brothers",
            "A Gentleman by Raj & DK",
        ],
        "books": [
            "The Girl in Room 105 by Chetan Bhagat",
            "The Da Vinci Code by Dan Brown",
            "Murder on the Orient Express by Agatha Christie",
            "The Girl on the Train by Paula Hawkins",
        ],
        "places": [
            "Kolkata",
            "Mumbai",
            "Bangalore",
            "London",
            "New York",
        ],
    }
    return recomms.get(category.lower(), [])

def recommbot():
    print("AI Recommendation Chatbot: Hello! I'm your AI recommendation chatbot. I can recommend you movies, books, places. ")
    while True:
        print("AI Recommendation Chatbot: Please choose a category: movie, books, places, or type 'exit' to quit.")
        userInput = input("You: ")

        if userInput.lower() == "exit":
            print("AI Recommendation Chatbot: BYE!")
            break

        recomms = recomm(userInput)

        if recomms:
            print("AI Recommendation Chatbot: Here are some recommendations for you:")
            for idx, recommendation in enumerate(recomms, start=1):
                print(f"{idx}. {recommendation}")
        else:
            print("AI Recommendation Chatbot: I'm sorry, but I can only recommend movies, books, and places.")

recommbot()
