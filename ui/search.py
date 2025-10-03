from scripts.search import Search as S
from pynput import keyboard

# https://www.reddit.com/r/learnpython/comments/aqjfsh/taking_live_keyboard_input_in_python_idle_without/

class Search:
    tasks = []
    query = ""

    def start(t):
        print("search: ", end="", flush=True)
        Search.tasks = t
        with keyboard.Listener(on_press=Search.on_press) as listener:
            listener.join()

    def on_press(key):
        
        Search.__clear_screen()
        try:
            Search.query += key.char
            print("\rsearch: " + Search.query, end="", flush=True)
            
        except AttributeError:
            if key == keyboard.Key.backspace:
                Search.query = Search.query[:-1]
                print("\rsearch: " + Search.query, end="", flush=True)
            elif key == keyboard.Key.space:
                Search.query+=" "
                print("\rsearch: " + Search.query, end="", flush=True)
            elif key == keyboard.Key.esc or key == keyboard.Key.enter:
                # Stop listener
                return False

        print("")
        for task in S.linear(Search.tasks, Search.query):
            if(task.contains(Search.query)): 
                temp = task.clone()

                temp.description = Search.__colorSubstring(temp.description, Search.query)
                temp.name = Search.__colorSubstring(temp.name, Search.query)

                print(temp)

    def __clear_screen():
        # ANSI escape code: clear screen and move cursor to top-left
        print("\033[2J\033[H", end="")

    def __colorSubstring(string, substring):
        # 1. get indexes of all occurrences of substring in string
        #    goes backwards for step 2
        occurrences = []
        for i in range(len(string) - len(substring) + 1, -1, -1):
            if (string[i:i + len(substring)].lower() == substring.lower()):
                occurrences.append(i)

        # 2. add parentheses around occurrence
        for occurrence in occurrences:
            string = string[:occurrence] + "(" + string[occurrence:]
            string = string[:occurrence + len(substring) + 1] + ")" + string[occurrence + len(substring) + 1:]
        
        # 3. remove redundant parentheses
        #    goes backwards for step 4
        redundancies = []
        i = 0
        for j in range(len(string) - 1, -1, -1):
            if (string[j] == "("):
                i -= 1
            if ((string[j] == "(" or string[j] == ")") and i > 0):
                redundancies.append(j)
            if (string[j] == ")"):
                i += 1

        for j in redundancies:
            string = string[:j] + string[j + 1:]

        # 4. replace parentheses with color escape codes
        return string.replace("(", "\033[35m").replace(")", "\033[0m")

    def __colorSubstring2(string, substring):
        # 1. get indexes of all occurrences of substring in string
        #    goes backwards for step 2
        occurrences = []
        for i in range(len(string) - len(substring) + 1, -1, -1):
            if (string[i:i + len(substring)].lower() == substring.lower()):
                occurrences.append(i)

        # 2. add parentheses around occurrence
        for occurrence in occurrences:
            string = string[:occurrence] + "(" + string[occurrence:]
            string = string[:occurrence + len(substring) + 1] + ")" + string[occurrence + len(substring) + 1:]
        
        # 3. remove redundant parentheses
        #    goes backwards for step 4
        redundancies = []
        i = 0
        for j in range(len(string) - 1, -1, -1):
            if (string[j] == "("):
                i -= 1
            if ((string[j] == "(" or string[j] == ")") and i > 0):
                redundancies.append(j)
            if (string[j] == ")"):
                i += 1

        for j in redundancies:
            string = string[:j] + string[j + 1:]

        # 4. replace parentheses with color escape codes
        return string.replace("(", "\033[35m").replace(")", "\033[0m")


