# from cryptography.corpus_loader import word_list, name_list
import re


def encrypt(plain,key):
    intial_phrase = plain.split()
    letters_list = []
    for word in intial_phrase:
        mod_word = re.sub(r'[^A-Za-z]+','', word)
        for num_let in mod_word:
            num_word = num_let.split()
            for letter in num_word:
                number = int(ord(letter))
                new_num = (number + key)
                print('new_num prior to sort: ',new_num)
                if new_num > 122 or new_num < 97:
                    new_num = new_num - 26
                    print('new_num: lower case:',new_num)
                if new_num < 90 and new_num < 97:
                    new_num = new_num - 26
                    print('new_num: upper case:',new_num)
                letters_list.append(chr(new_num))
    encoded_phrase = ''.join(letters_list)
    return encoded_phrase







def decrypt(encode,key):
    pass

def crack(encode):
    pass

print(encrypt("BANANA", 10))