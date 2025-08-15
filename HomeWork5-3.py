import string
get_string= input("Введіть рядок: ")
for char in string.punctuation:
    get_string= get_string.replace(char, " ")
words = get_string.split()
hashtag = "#"
for word in words:
    cap_word=word.capitalize()
    hashtag += cap_word
if len(hashtag) > 140:
    print("Хештег занадто довгий, його буде обрізано до 140 символів")
    hashtag = hashtag[:140]
else:
    print("Хештег успішно створено")
print(hashtag)

