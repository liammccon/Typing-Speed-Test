def main():
    do_the_thing()

def do_the_thing():
    big_list, titles = combine_lines('big_phrases_unsorted')
    sentence_list = devide_into_sentences(big_list)
    filtered_list = filter_sentence_list(sentence_list, titles, 240, 290)

    f = open('filtered_file.txt', 'w')
    for item in filtered_list:
        f.write('#' + item[0] + '\n')
        f.write(item[1] + '\n')
        print(f'{len(item[1])}: {item}')

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


def filter_sentence_list(big_list, titles, min_chars = 275, max_chars = 325):
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
    return (big_strings, string_of_titles)

if __name__ == '__main__': main()

