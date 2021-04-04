#Practice Problem 1
s = "6.00 is 6.001 and 6.002"
new_str = ""
new_str += s[-1]
new_str += s[0]
new_str += s[4::30]
new_str += s[13:10:-1]
print(new_str)
print()

#Practice Problem 2
s1 = "mit u rock"
s2 = "i rile mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break

#Practice Problem 3
word1 = "Chapman"
word2 = ""
for i in range(len(word1)):
    word2 += word1[-(i+1)]
print(word2)
