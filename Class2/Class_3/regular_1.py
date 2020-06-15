import re
# print (re.match)
# print (re.search)
# print (re.findall)
# print (re.sub)

#[] -- можно указывать множество символов подходящих под шаблон
pattern = r"a[abc]c"
string = "aac"
match_object = re.search(pattern, string)
print(match_object)

string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern,"abc",string)
print(fixed_typos)