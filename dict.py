counts = dict()
names = "marquard", "cwen", "cwen", "zhen", "marquard", "zhen", "csev", "zhen", "csev", "marquard"
#Let's use a Dictionary. One commom use of dictionaries is counting how often we "see" things

# There will be an error to reference a key which is not in the dictionary
# We can use "in" operator to see if a key is in the dictionary.


for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

#We can also use "get" method for dictionaries
# "get" is the default value if key does not exist and no traceback.

 
x = counts.get(name, 0)

counts = dict()
names = ["csev", "cwen", "zqian", "cwen"]
for name in names:
    counts[name] = counts.get(name, 0) + 1

cnt = dict()
print("Enter a line of text: ")
line = open("txt.txt", "r" )
words = line.split()
print("Words:", words)
print("Counting.....")
for word in words:
    cnt[word] = cnt.get(word, 0) + 1
print("Counts: ", cnt)

# This is the for loop to look up the keys in the dictionary.

for key in cnt:
    print(key, cnt[key])
