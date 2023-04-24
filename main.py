import tools
import agents
import storage

init_llm()


def main():
    
    while True:
        try:
            user_input = input("Enter your business name and description")     
            # Do something with the user input
            tasks = agents.tasks(user_input)
            print(tasks)
            
            
        except Exception as e:
            # Handle the error here
            print("An error occurred:", e)
            
        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C) here
            print("Keyboard interrupt detected. Exiting.")
            break