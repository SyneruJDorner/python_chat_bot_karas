import sys
from ai_module import _install as install

from ai_module import training_module
from ai_module import chat_module

def main():
    if (len(sys.argv) >= 2):
        arg = str(sys.argv[1]).lower()

        if (arg == "help"):
            f = open('ai_module/help.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            return

        if (arg == "install"):
            install.install_all()
            return

        if (arg == "clean"):
            install.clean()
            return

        if (arg == "train"):
            training_module.train()
            return
            
    chat_module.chat()

if __name__ == "__main__":
    main()