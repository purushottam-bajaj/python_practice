'''This program checks if a given word is a palindrome. '''

def is_palindrome(my_word: str) -> bool:
    '''Check if the given word is a palindrome.'''
    reverse_word = my_word[::-1]
    return my_word == reverse_word

if __name__ == '__main__':
    word = input("Enter a word: ")
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")

#Done
