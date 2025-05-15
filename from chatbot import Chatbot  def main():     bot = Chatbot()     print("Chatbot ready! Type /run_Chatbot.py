from chatbot import Chatbot

def main():
    bot = Chatbot()
    print("Chatbot ready! Type /reset to start over, Ctrl+C to quit.")

    while True:
        try:
            user_input = input("> ")
            response = bot.generate_response(user_input)
            print(response)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
