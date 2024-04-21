class Jarvis:
    def __init__(self):
        self.name = "Jarvis"

    def greet(self):
        return f"Hello! I am {self.name}. How can I help you today?"

    def respond(self, user_input):
        if "hello" in user_input.lower() or 'hi' in user_input.lower():
            return "Hello! How are you?"
        elif "how are you" in user_input.lower():
            return "I'm just a computer program, so I don't have feelings, but I'm here to help!(im good thanks for asking)"
        elif 'Whats your plan?' in user_input.lower() or 'plans' in user_input.lower() :
            return 'oh i havent got any plans(imma take over the world)'
        elif 'Who created you?' in user_input.lower() :
            return 'oh i was created  by a lil guy from Andinet International School'
        else:
            return "I'm sorry, I didn't understand that. Can you please repeat or ask me something else?"

# Main program
def main():
    ai = Jarvis()
    print(ai.greet())

    while True:
        user_input = input("You: ")
        response = ai.respond(user_input)
        print(f"{ai.name}: {response}")

if __name__ == "__main__":
    main()