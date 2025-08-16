import string

range_of_letters = input(f"Enter a range of letters (a-c), (a-H): ").strip()
letters = range_of_letters.split('-')
letter_one= letters[0].strip()
letter_two = letters[1].strip()
index_one = string.ascii_letters.index(letter_one)
index_two = string.ascii_letters.index(letter_two)
if index_one<= index_two:
    result = string.ascii_letters[index_one:index_two+1]
    print(result)


