def get_num_words(string_to_count : str):
    list_of_words = string_to_count.split()

    return len(list_of_words)

def count_characters(book : str):
    book = book.lower()
    cha_dict ={}
    for i in book:
        if not i in cha_dict: cha_dict[i] = 1
        else : cha_dict[i]+=1

    return cha_dict

def sort_on(dict):
    return dict["num"]

def sort_dictionary(raw_dict):
    raw_list=[]
    for chara in raw_dict:
        if chara.isalpha():
            raw_list.append({"cha":chara , "num":raw_dict[chara]})
    
    raw_list.sort(key=sort_on,reverse=True)

    return raw_list #is sorted now