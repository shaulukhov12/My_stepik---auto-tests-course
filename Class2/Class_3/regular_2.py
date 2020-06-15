import re
# print (re.match)
# print (re.search)
# print (re.findall)
# print (re.sub)

#[] -- можно указывать множество символов подходящих под шаблон
pattern = r"a[ab]+?a"# Использовать * для получения Любое число символа b включая 0 или знак + чтобы найти больше 0
string = "abaaba"
print(re.match(pattern, string))
print(re.findall(pattern, string))