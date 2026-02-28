# Python Interview Practice Problems

## String Manipulation Problems

### 1. Reverse a String
**Problem:** Write a function to reverse a string without using built-in reverse methods.
**Example:** `reverse_string("hello")` → `"olleh"`

### 2. Count Vowels
**Problem:** Write a function that counts the number of vowels (a, e, i, o, u) in a string.
**Example:** `count_vowels("hello world")` → `3`

### 3. Remove Duplicates
**Problem:** Write a function to remove duplicate characters from a string while preserving order.
**Example:** `remove_duplicates("programming")` → `"progamin"`

### 4. Anagram Checker
**Problem:** Write a function to check if two strings are anagrams (contain the same characters).
**Example:** `is_anagram("listen", "silent")` → `True`

### 5. First Non-Repeating Character
**Problem:** Find the first non-repeating character in a string.
**Example:** `first_non_repeating("aabbccd")` → `"d"`

## Array/List Problems

### 6. Find Maximum and Minimum
**Problem:** Write a function to find the maximum and minimum values in a list without using built-in functions.
**Example:** `find_max_min([3, 1, 4, 1, 5, 9, 2])` → `(9, 1)`

### 7. Two Sum
**Problem:** Given a list of integers and a target sum, find two numbers that add up to the target.
**Example:** `two_sum([2, 7, 11, 15], 9)` → `[0, 1]` (indices of 2 and 7)

### 8. Remove Duplicates from List
**Problem:** Remove duplicates from a list while preserving order.
**Example:** `remove_duplicates_list([1, 2, 2, 3, 4, 4, 5])` → `[1, 2, 3, 4, 5]`

### 9. Find Missing Number
**Problem:** Given a list of n-1 integers in the range 1 to n, find the missing number.
**Example:** `find_missing([1, 2, 4, 5, 6])` → `3`

### 10. Rotate Array
**Problem:** Rotate an array to the right by k steps.
**Example:** `rotate_array([1, 2, 3, 4, 5], 2)` → `[4, 5, 1, 2, 3]`

## Number Problems

### 11. Fibonacci Sequence
**Problem:** Generate the first n numbers in the Fibonacci sequence.
**Example:** `fibonacci(7)` → `[0, 1, 1, 2, 3, 5, 8]`

### 12. Factorial
**Problem:** Calculate the factorial of a number (both iterative and recursive).
**Example:** `factorial(5)` → `120`

### 13. Prime Number Checker
**Problem:** Check if a number is prime.
**Example:** `is_prime(17)` → `True`, `is_prime(15)` → `False`

### 14. Greatest Common Divisor (GCD)
**Problem:** Find the GCD of two numbers using Euclidean algorithm.
**Example:** `gcd(48, 18)` → `6`

### 15. Reverse Integer
**Problem:** Reverse the digits of an integer.
**Example:** `reverse_int(123)` → `321`, `reverse_int(-123)` → `-321`

## Dictionary/Set Problems

### 16. Word Frequency Counter
**Problem:** Count the frequency of each word in a string.
**Example:** `word_frequency("hello world hello")` → `{"hello": 2, "world": 1}`

### 17. Group Anagrams
**Problem:** Group words that are anagrams of each other.
**Example:** `group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])` → `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

## Algorithm Problems

### 18. Binary Search
**Problem:** Implement binary search on a sorted list.
**Example:** `binary_search([1, 2, 3, 4, 5, 6], 4)` → `3` (index)

### 19. Bubble Sort
**Problem:** Implement bubble sort algorithm.
**Example:** `bubble_sort([64, 34, 25, 12, 22, 11, 90])` → `[11, 12, 22, 25, 34, 64, 90]`

### 20. FizzBuzz
**Problem:** Print numbers 1 to n, but for multiples of 3 print "Fizz", multiples of 5 print "Buzz", and multiples of both print "FizzBuzz".
**Example:** `fizzbuzz(15)` → `1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz`

## Tips for Interview Practice

1. **Start with the problem statement** - Make sure you understand what's being asked
2. **Think about edge cases** - Empty strings, None values, single elements, etc.
3. **Consider time/space complexity** - Interviewers often ask about Big O notation
4. **Write clean code** - Use meaningful variable names, add docstrings
5. **Test your code** - Write test cases before or after implementation
6. **Explain your approach** - Be ready to walk through your solution

## Practice Order Recommendation

**Beginner:**
- Palindrome Checker ✓ (you've done this!)
- Reverse String
- Count Vowels
- Factorial
- FizzBuzz

**Intermediate:**
- Two Sum
- Anagram Checker
- Remove Duplicates
- Fibonacci
- Word Frequency

**Advanced:**
- Binary Search
- Group Anagrams
- Rotate Array
- GCD
- Prime Number Checker

