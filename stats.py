# We need file path, word count, sorted dictionary into a list.

def sort_on(d):
    return d["num"]

def report(file_path):
    with open(file_path) as f:
        text = f.read()
    word_sum = {}
    filtered_words = []
    total_words = 0
    for item in text.lower().split():
        if item in word_sum:
            word_sum[item] += 1
        else:
            word_sum[item] = 1
    for item in word_sum:
        filtered_words.append({"word": item, "num": word_sum[item]})
        total_words += word_sum[item]
    filtered_words.sort(key=sort_on, reverse=True)
    character_sum = {}
    filtered_characters = []
    total_letters = 0
    for item in text.lower():
        if not item.isalpha():
            continue
        if item in character_sum:
            character_sum[item] += 1
        else:
            character_sum[item] = 1
    for item in character_sum:
        filtered_characters.append({"char": item, "num": character_sum[item]})
        total_letters += character_sum[item]
    filtered_characters.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    for item in filtered_words[:10]:
        print(f"{item['word']}: {item['num']}")
    print("--------- Character Count -------")
    for item in filtered_characters[0:10]:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
