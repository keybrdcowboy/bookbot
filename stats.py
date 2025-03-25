def word_count(book_text):
    list_of_words = []
    list_of_words = book_text.split()
    return len(list_of_words)

def char_count(book_text):
    char_count_dict = {}

    for i in book_text:
        if i.lower() in char_count_dict:
            char_count_dict[i.lower()] = char_count_dict[i.lower()] + 1
        else:
            char_count_dict[i.lower()] = 1
    
    return char_count_dict

def dict_sort(dict):
    return dict["value"]

def pretty_print(char_dict):
    list_sorted_dicts = []

    for i in char_dict:
        #print(i)
        #print(char_dict[i])
        if i.isalpha():
            #print(i)
            #print(char_dict[i])
            list_sorted_dicts.append({"letter": i, "value": char_dict[i]})

    #print(len(list_sorted_dicts))
    
    #for i in list_sorted_dicts:
    #    if i['letter'] == 'e':
    #        print(i)
    #print(list_sorted_dicts)
    list_sorted_dicts.sort(reverse=True, key=dict_sort)
    #print(list_sorted_dicts)
    return list_sorted_dicts