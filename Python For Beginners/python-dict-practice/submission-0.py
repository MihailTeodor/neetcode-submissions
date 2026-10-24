from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    counts: dict[str, int] = {}

    for char in word:
        counts[char] = counts.get(char, 0) + 1
    return counts




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
