from typing import List

def my_len(word: str) -> int:
    count = 0
    for _ in word:
        count += 1
    return count

def my_abs(n: int) -> int:
    if n < 0:
        return -n
    return n

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=my_len, reverse=True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=my_abs)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
