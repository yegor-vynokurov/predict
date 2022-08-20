import fnctns

dct1 = fnctns.load_dct(tp = 1) # load foreward dict
dct2 = fnctns.load_dct(tp = 2) # load backward dict
word = input('введите слово: ')
state = int(input('предсказание вперёд - введите 1, предсказание назад - введите 2, совмещённое - 3: ') or '1')
ln = int(input('выберите длину предсказания: ') or '30')
sent = fnctns.sentence(word = word, dctn1 = dct1, dctn2 = dct2, state = state, ln = ln)
# print(sent)
sent = fnctns.prnt(sent) # take of sentence

print(sent)

with open("dcts/answer.txt", "w", encoding="utf-8") as file:
    print(sent, file=file)

input()