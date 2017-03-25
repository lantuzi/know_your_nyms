import random

vocab_file = 'vocab.txt'
with open(vocab_file) as f:
    lines = f.readlines()
vocab = [word.lower().strip() for word in lines]
random.shuffle(vocab)
print vocab
with open('random_vocab.txt', 'w') as f2:
    for word in vocab:
        f2.write(word + '\n')

