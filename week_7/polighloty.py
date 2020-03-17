amount_pupils = int(input())
famous_languages = set()
all_languages = set()
for counter, i in enumerate(range(amount_pupils)):
    known_languages = int(input())
    pupils_languages = set()
    for j in range(known_languages):
        pupils_languages.add(input())
    if counter == 0:
        famous_languages = pupils_languages
    famous_languages &= pupils_languages
    all_languages |= pupils_languages
print(len(famous_languages), *sorted(famous_languages), sep="\n")
print(len(all_languages), *sorted(all_languages), sep="\n")
