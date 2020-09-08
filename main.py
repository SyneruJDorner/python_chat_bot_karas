import sys

try:
    from ai_module import training_module
    from ai_module import chat_module
except ImportError as e:
    print("Error: " + str(e))
except:
    print("Error: ", str(sys.exc_info()[0]))

def commands(command):
    import os, subprocess
    
    full_path = os.path.join(os.getcwd(), "commands.bat")
    subprocess.call([full_path, command])
    pass

def main(argv):
    if (len(argv) >= 2):
        arg = str(argv[1]).lower()

        if (arg == "help"):
            f = open('help.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            return

        if (arg == "train"):
            training_module.train()
            return

        commands(arg)
        return

    chat_module.chat()

if __name__ == "__main__":
    main(sys.argv)