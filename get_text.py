import fnctns

path = 'dcts/'
name = 'Tvortsyi_zaklinaniy.txt'
to_whitespace = '.-'
stop_words = ['И.', 'Г.', 'Ф.', 'notes', 'Прэтчетт', 'Терри', 'Нилу', 'Гэйману']
whitespace = '\t\n\r\x0b\x0c'
marks = '"#$%&\'()*+/:;<=>@[\\]^_`{|}~.,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*—“”…!?.'

text = fnctns.get_text(path = path,
                       name = name,
                       whitespace = whitespace,
                       marks = marks,
                       stop_words = stop_words) # take a list from txt

dct1, dct2 = fnctns.get_pairs(text) # take pairs of words

fnctns.save_dct(dct = dct1, tp = 1) # saving of the forward dicts

fnctns.save_dct(dct = dct2, tp = 2) # saving of the backward dicts



