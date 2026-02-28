'''This program checks if a given word is a palindrome. A palindrome is a word that reads the same backward as forward.'''

def is_palindrome(word: str) -> bool:
    '''Check if the given word is a palindrome.'''
    reverse_word = word[::-1]
    return word == reverse_word

if __name__ == '__main__':
    word = input("Enter a word: ")
    if is_palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
    