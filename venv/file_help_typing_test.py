import random

def make_phrase(min_chars, max_chars):
    big_list, titles = combine_lines('big_phrases_unsorted')
    sentence_list = devide_into_sentences(big_list)
    filtered_list = filter_sentence_list(sentence_list, titles, min_chars, max_chars)

    f = open('filtered_file.txt', 'w')
    for item in filtered_list:
        f.write('#' + item[0] + '\n')
        f.write(item[1] + '\n')
        #print(f'{len(item[1])}: {item}')

def devide_into_sentences(big_list):
    new_list = []
    for para in big_list:
        while para != para.replace('  ', ' '): #remove any double spaces
            para = para.replace('  ', ' ')
        para = para.rstrip()
        sentence_list = []
        min_index = 0
        index = 0
        done_with_para = False

        while not done_with_para:
            if para[index: index + 1] == '.':
                if len(para) == index + 1:  # if it is the end of the paragraph
                    sentence_list.append(para[min_index: index + 1].lstrip())
                    done_with_para = True
                elif not (index > 4 and (para[index - 2: index + 1] == 'Mr.' or para[index - 3: index + 1] == 'Mrs.')):
                    sentence_list.append(para[min_index:index + 1].lstrip())
                    min_index = index + 1
            elif len(para) == index + 1:  # if the last sentence of para doesnt have a period
                sentence_list.append((para[min_index: index + 1] + '.').lstrip())
                done_with_para = True
            index += 1

        new_list.append(sentence_list)
    return new_list


def filter_sentence_list(big_list, titles, min_chars, max_chars):
    #takes the sentence list and makes a new list of strings that are within the word count bound
    #can combine sentences within the same chapter but not sentences outside of that
    new_list = []
    for sentence_list in big_list:
        index = 0
        current_title = titles[big_list.index(sentence_list)]
        while index < len(sentence_list) - 1:
            current_sentece = sentence_list[index]
            length = len(current_sentece)
            if length <= max_chars:
                while index < len(sentence_list) -1 and length <= max_chars:
                    if length >= min_chars:
                        new_list.append((current_title, current_sentece))
                    index+=1
                    current_sentece += ' ' + sentence_list[index]
                    length = len(current_sentece)
            else:
                index += 1
    return new_list


def iterate_lines(file_name):
    f = open(file_name)
    for line in f:
        if not line.strip() :
            continue
        else:
            yield line

def combine_lines(file_name):
    big_strings = []
    string_of_titles = []
    current_string = ''
    new, add, skip = 0, 1, 2
    for line in iterate_lines(file_name):
        to_do = None
        if line[0: 5] == '#From':
            string_of_titles.append(line[1:].rstrip())
            to_do = new
        elif line[0:1] == '#':
            to_do == skip
        else:
            to_do = add

        if to_do == new and current_string:
            big_strings.append(current_string)
            current_string = ''
        elif to_do == add:
            current_string += line.rstrip() + ' '
    big_strings.append(current_string)
    return big_strings, string_of_titles

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