import re

pattern = re.compile('Ali')
string = 'Ali Hi Iam Md Azaz Hi Iam Md Azaz Ali.'
#search = re.search("Md", string)

# print(search.group())
# print(search.start())
# print(search.end())
# print(search.span())
# print(pattern.search(string))
# print(pattern.findall(string))
# print(pattern.fullmatch(string))
print(pattern.match(string))
