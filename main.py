# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    list = ['An invitation to      dinner. Mrs.  Bennet  planned the courses. Hi   Im liam. And im joe.',
            'Here is another sentence. Mr. Liam said hey. Now i end without period  ']
    str = '123'
    new_list = devide_into_sentences(list)
    print(new_list)

def filter_sentence_list(big_list, min_chars = 0, max_chars = 0):
    #takes the sentence list and makes a new list of strings that are within the word count bound
    #can combine sentences within the same chapter but not sentences outside of that
    new_list = []
    for sentence_list in big_list:
        index = 0
        while index < len(sentence_list):
            current_sentece = sentence_list[index]
            while len(current_sentece) <= max_chars:
                if len(current_sentece) >= min_chars:
                    new_list.append(current_sentece)
                    index += 1
                else:
                    index+=1
                    current_sentece += ' ' + sentence_list[index]
    return new_list


def devide_into_sentences(big_list):
    new_list = []
    for para in big_list:
        while para != para.replace('  ', ' '): #remove any double spaces
            para = para.replace('  ', ' ')
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


def compare_char_sequence(model_string, user_string, seq_size = 3):
    model_seq_list = string_to_seq_list(model_string)
    user_seq_list = string_to_seq_list(user_string)
    seq_from_model_in_user = 0
    seq_from_user_in_model = 0
    model_seq_list_length = len(model_seq_list)
    user_seq_list_length = len(user_seq_list)
    for seq in model_seq_list:
        if seq in user_seq_list:
            user_seq_list.remove(seq)
            #Y: user.remove seq; seq_from_model_in_user+=1
            #N: do nothing

def string_to_seq_list(string, seq_length = 3):
    if not isinstance(string, str):
        raise TypeError
    seq_list = []
    index = 0
    while index <= len(string) - seq_length:
        seq_list.append(string[index: index + seq_length + 1])
        index +=1
    return seq_list

# Press the green button in the gutter to run the script.
if __name__ == '__main__': main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
