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

def execute(command):
    arg = str(command).lower()

    if (arg == "help"):
        f = open('help.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        return

    try:
        if (arg == "train"):
            training_module.train()
            return
    except:
        print("Error: ", str(sys.exc_info()[0]))

    if (arg == "install" or arg == "uninstall" or arg == "train" or arg == "clean"):
        commands(arg)
        return