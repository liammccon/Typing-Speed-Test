import random
import time
from decimal import *

def main():
    input('press enter to start')
    t1 = time.time()
    random_string_from_text, text_title = random_phrase_and_title('filtered_file.txt')
    user_string = user_input(f'''Type: {random_string_from_text} 
~{text_title}
----> ''')
    t2 = time.time()
    accuracy_float = compare_char_sequence(random_string_from_text, user_string)
    user_words = string_to_word_char_list(user_string)
    words_per_min = ((len(user_words) / (t2 - t1)) * 60)
    print(f'Words per minute: %.2f ' % words_per_min)
    print(f'Accuracy: %.0f percent' % (accuracy_float * 100))
    print('Your score: %.0f' %get_score(words_per_min, accuracy_float))
    #print('Elapsed time: %.2f seconds.' % (t2 - t1))


def get_score(wpm, accuracy_float):
    return wpm * (accuracy_float * accuracy_float) * 10 #bad accuracy heavily lowers score


def user_input(string = 'Type: '):
    return input(string)

def string_to_seq_list(string, seq_length = 3):
    if not isinstance(string, str):
        raise TypeError
    seq_list = []
    index = 0
    while index <= len(string) - seq_length:
        seq_list.append(string[index: index + seq_length + 1])
        index += 1
    return seq_list

def string_to_word_char_list(string):
    if isinstance(string, list): #for redundancy and simplicity :)
        return string
    elif not isinstance(string, str):
        raise TypeError('Need to enter a string')
    string = string + ' ' #needed to add the last word of each string
    index = 0
    words_letters = []
    new_word = []
    while  index < len(string):
        current_letter = string[index: index + 1]
        if string[index: index + 1] == ' ':
            if new_word:
                words_letters.append(new_word)
                new_word = []
        else: new_word.append(current_letter)
        index += 1
    return words_letters

def random_phrase_and_title(file_name):
    f = open(file_name)
    line_list = []
    title = ''
    for line in f:
        if line[0: 1] == '#':
            title = line[1:]
            continue
        line_list.append(line.rstrip())
    return line_list[random.randint(0, len(line_list) - 1 )], title

def compare_char_sequence(model_string, user_string, seq_size = 3):
    model_string = model_string.rstrip()
    model_string = model_string.lstrip()
    user_string = user_string.rstrip()
    user_string = user_string.lstrip()
    model_seq_list = string_to_seq_list(model_string, seq_size)
    model_seq_list_copy = model_seq_list.copy()
    user_seq_list = string_to_seq_list(user_string, seq_size)
    user_seq_list_copy = user_seq_list.copy()
    seq_from_model_in_user = 0
    seq_from_user_in_model = 0
    model_seq_list_length = len(model_seq_list)
    user_seq_list_length = len(user_seq_list)
    for seq in model_seq_list:
        if seq in user_seq_list_copy:
            user_seq_list_copy.remove(seq)
            seq_from_model_in_user += 1
    for seq in user_seq_list:
        if seq in model_seq_list_copy:
            model_seq_list_copy.remove(seq)
            seq_from_user_in_model += 1
    model_in_user_percent = seq_from_model_in_user / model_seq_list_length
    user_in_model_percent = seq_from_user_in_model / user_seq_list_length
    smaller_of_both = model_in_user_percent if model_in_user_percent < user_in_model_percent else user_in_model_percent
    return smaller_of_both

#JUST tests how many of the model sentence's words are in the user's sentence
#DOES NOT factor in word order, 'partial credit' for words only slightly mispelled,
#or extra words in the user sentence not in the model.
def simple_word_accuracy(model, user):
    if isinstance(model, list) and isinstance(user, list):
        correct_words = 0
        for word in model:
            if user.__contains__(word):
                correct_words += 1
        accuracy = correct_words / len(model)
        return accuracy
    else:
        if isinstance(model, str):
            new_model = string_to_word_char_list(model)
        elif isinstance(model, list):
            new_model = model
        else: new_model = None
        if isinstance(user, str):
            new_user = string_to_word_char_list(user)
        elif isinstance(user, list):
            new_user = user
        else: new_user = None
        if new_model and new_user:
            return simple_word_accuracy(new_model, new_user)
        else:
            raise TypeError('Enter a word / letter list or a string')



if __name__ == '__main__': main()
