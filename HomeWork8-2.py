def is_palindrome(text):

    filtered_el = ''.join(el.lower() for el in text if el.isalnum())
    return filtered_el == filtered_el[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
