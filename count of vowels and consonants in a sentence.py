# find number of vowels in a sentence
sentence = "A quick brown fox jumps over the lazy dog"
counter=0
vowels="aeiouAEIOU"
for i in sentence:
    if(i in vowels):
        counter=counter+1
print("number of vowels in sentence is:",counter)
# for consonants
sentence ="A quick brown fox jumps over the lazy dog"
counter_new=00
vowels="aeiouAEIOU"
for j in sentence:
    if(j not in vowels and j.isalpha()):
            counter_new=counter_new+1
print("number of consonants in sentence is:",counter_new)
