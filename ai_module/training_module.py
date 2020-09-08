import sys, os
import numpy as np
import pickle, json, random

try:
    import nltk
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    
    from ai_module.ai_module import brain, save_brain
except ImportError as e:
    print("Error: " + e)
except:
    print("Error: ", sys.exc_info()[0])

def train():
    trained_path = os.path.join(os.getcwd(), "trained_data")

    if not os.path.exists(trained_path):
        os.makedirs(trained_path)

    words=[]
    classes = []
    documents = []
    ignore_words = ['?', '!']
    data_file = open("training_data\\intents.json").read()
    intents = json.loads(data_file)

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            tokenize_words = nltk.word_tokenize(pattern)
            words.extend(tokenize_words)
            documents.append((tokenize_words, intent['tag']))

            if intent['tag'] not in classes:
                classes.append(intent['tag'])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    pickle.dump(words, open("trained_data\\words.pkl", "wb"))
    pickle.dump(classes, open("trained_data\\classes.pkl", "wb"))

    training = []
    output_empty = [0] * len(classes)

    for doc in documents:
        bag = []
        pattern_words = doc[0]
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)
        
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:,0])
    train_y = list(training[:,1])

    model = brain(train_x, train_y)
    save_brain(model, train_x, train_y)
    print("AI Brain Has Been Created!")