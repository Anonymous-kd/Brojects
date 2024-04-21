class jarvis:
    def __init__(self):
        self.name = "jarvis"

    def intro(self):
        return f"Hello! I am  {self.name} (based off of ironman). How can I help you today?"

    def response(self, user_input):
        if "hello" or 'hi' in user_input.lower():
            print("Hello! How are you?")
        elif "how are you" in user_input.lower():
            print("I'm just a computer program, so I don't have feelings, but I'm here to assist you!")
        else:
            print("I'm sorry, I didn't understand that. Can you please repeat or ask me something else?")

# Main program
def main():
    ai = jarvis()
    print(ai.intro())

    while True:
        user_input = input("You: ")
        response = ai.response(user_input)
        print(f"{ai.name}: {response}")

if __name__ == "__main__":
    main()