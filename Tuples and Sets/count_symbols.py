#first way
# text = input()
#
# for letter in sorted(set(text)):
#     print(f"{letter}: {text.count(letter)} time/s")


#second way
# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")

#third way
text = input()
my_dict = {}
value = 0
for i in text:
    for ch in i:
        if ch not in my_dict:
            my_dict[ch] = value
        if ch in my_dict:
            my_dict[ch] += 1

for letter, times in sorted(my_dict.items()):
    print(f"{letter}: {times} time/s")
