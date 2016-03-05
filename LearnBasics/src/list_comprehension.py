
"Example 1 - normal code"
list_containing_names_with_spaces = [" sachin  ", " dravid   ", "laxman   "]
clean_list=[]
for name in list_containing_names_with_spaces:
    clean_list.append(name.strip())
print(clean_list)

"using list comprehension"
list_containing_names_with_spaces = [" sachin  ", " dravid   ", "laxman   "]
clean_list=[name.strip() for name in list_containing_names_with_spaces]
print(clean_list)


"Example 2 - with If statement - Normal code"
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))


"using list comprehension"
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print word_lengths
