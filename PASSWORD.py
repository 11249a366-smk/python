sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
digit_count = 0
uppercase_count = 0
lowercase_count = 0

for ch in sentence:
    if ch.isdigit():
        digit_count += 1
    elif ch.isupper():
        uppercase_count += 1
    elif ch.islower():
        lowercase_count += 1

print("Number of words:", word_count)
print("Number of digits:", digit_count)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
