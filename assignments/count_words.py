def count_words():
    str1 = input("Enter words: ")

    word_list = str1.split(" ")

    for word in set(word_list):
        n = word_list.count(word)
        print(f"{word} repeated {n} of times")


count_words()
