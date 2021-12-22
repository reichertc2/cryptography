from cryptography.corpus_loader import word_list, name_list
import re



def encrypt(plain,key):
    intial_phrase = plain.split()
    # word_count = 0

    for word in intial_phrase:
        mod_word = re.sub(r'[^A-Za-z]+','', word)
        num_word = mod_word.ascii_letters
        print(num_word)
    
    







def decrypt(encode,key):
    pass

def crack(encode):
    pass

encrypt("apple", 1)