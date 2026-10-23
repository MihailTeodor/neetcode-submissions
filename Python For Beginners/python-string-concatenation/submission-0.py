def concatenate(s1: str, s2: str) -> str:
    s1s2 = s1 + s2

    if len(s1s2) > 10:
        return "Too long!"
    
    return s1s2




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
