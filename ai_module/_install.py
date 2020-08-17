# ======================================================================
# This file is used to download and import all dependancies and packages
# required for this project
# ======================================================================
# pip install nltk
# pip install numpy
# pip install tensorflow
# pip install pickle
# pip install keras
# ======================================================================

import sys, subprocess, os, shutil

def install(package, *args):
    install_string = [sys.executable, "-m", "pip", "install", package]
    install_string = install_string + list(args)
    print(" ".join(install_string))
    subprocess.check_call(" ".join(install_string))

def install_all():
    install('nltk')
    install('numpy')
    install('tensorflow')
    install('keras')

    try:
        import nltk
        nltk.download('wordnet')
    except ImportError:
        print("Unable to import nltk and download 'wordnet'")
        pass

def clean():
    folder = os.path.join(os.getcwd(), "trained_data")

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    print('Completed cleaning up training data.')