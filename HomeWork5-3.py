import string
get_string= input("Введіть рядок: ")
for char in string.punctuation:
    get_string= get_string.replace(char, " ")
words = get_string.split()
for word in words:
    word.capitalize()
hashtag = "#" + "".join(word.capitalize() for word in words)
if len(hashtag) > 140:
    print("Хештег занадто довгий")
print(hashtag)

