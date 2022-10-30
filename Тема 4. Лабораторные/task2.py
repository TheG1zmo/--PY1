def get_count_char(str_):
    str_ = str_.lower()
    dict_ = {}
    def_count = 0
    for i in str_ :
        if i.isalpha() :
            dict_ [i] = dict_.get(i, def_count) + 1
    return dict_
def percent (dict_1) :
    sum_ = 0
    for i in dict_1 : sum_ += dict_1[i]
    for i in dict_1 :
        dict_1 [i] = round (dict_1 [i] / sum_ * 100, 2)
    return  dict_1

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent(get_count_char(main_str)))
