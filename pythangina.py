import os
import sys
import cmd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'keywords'))

from keywords import keywords, splitters

def translate(code, file_extension):
    inside_single_quote = False
    inside_double_quote = False

    tokens = []
    current_token = ""
    for c in code:
        if c in ["'", '"']:
            if c == "'":
                inside_single_quote = not inside_single_quote
            else:
                inside_double_quote = not inside_double_quote
        if not inside_single_quote and not inside_double_quote:
            if current_token in keywords:
                current_token = keywords[current_token]
        current_token += c
        if c in splitters:
            tokens.append(current_token)
            current_token = ""
    tokens.append(current_token)

    translated_code = "".join(tokens)

    if file_extension == ".puta":
        translated_code = translated_code.replace(".puta", ".py")
        
    return translated_code

def interpret(filepath):
    _, file_extension = os.path.splitext(filepath)
    
    if file_extension != ".puta":
        raise ValueError("Di-wastong extension ng file. Dapat .puta")

    with open(filepath, "r") as f:
        code = f.read()

    translated_code = translate(code, file_extension)
    
    exec(translated_code)

class TagalogInterpreter(cmd.Cmd):
    intro = "Maligayang pagdating sa Tagalog Python Interpreter! I-type ang 'help' para sa isang listahan ng mga command."
    prompt = ">> "

    def do_execute(self, filepath):
        "Magpaandar ng python file na nakasulat sa Tagalog."
        try:
            interpret(filepath)
        except Exception as e:
            print(f"Error: {e}")

    def do_exit(self):
        "Mag-exit ng interpreter."
        return True

if __name__ == "__main__":
    interpreter = TagalogInterpreter()
    interpreter.cmdloop()
