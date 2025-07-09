def w_count(word):
    word=word.lower()
    freq={}
    for letter in word:
        if letter.isalpha():
            freq[letter]=freq.get(letter,0)+1
    if not freq:
        return "not valid"
    max_count=max(freq.values())
    max_letter=[letter for letter,count in freq.items() if count==max_count]

    return f"Most used letter :{'. '.join(max_letter)}|count:{max_count}"
print(w_count("machine learning"))
