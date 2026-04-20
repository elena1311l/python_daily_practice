def analyze_message(text):
    lower_text = text.lower()
    words=lower_text.split()
    is_python=0
    for item in words:
        if item=="python":
            is_python+=1
    return is_python, len(words)

message = "I am learning Python and it is great"
print (analyze_message(message))


def long_words_count(textes):
    new_text=textes.split()
    count=0
    for word in new_text:
        if len(word)>=5:
            print(word)
            count+=1
    return count
texxt="Python is a powerful programming language"
print(long_words_count(texxt))