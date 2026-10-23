from typing import List

def contains_duplicate(words: List[str]) -> bool:
    list_length = len(words)

    words_set = set(words)

    if len(words_set) != list_length:
        return True
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
