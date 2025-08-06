#text = input("Enter your sentence/word: ")
#search_count = input("Enter the word/character you want to search: ")
#text_count = text.count(search_count)
#print("There are", text_count, '"' + search_count + '"', "in your sentence", text)

string = "python console"
#print(string.endswith("Graza"))

#indexing is also possible
#print(string.endswith("Graza", 7,12))

#variable = string.partition("If")
#print (variable)

#new_str = string.zfill(8)
#print(new_str)

#new_str = string .replace("love", "hate", 1)
#print(new_str)

#new_str = string.rjust(7, "0")
#txt = "line 1\nline 2"
#lines = txt.splitlines(False)
#print(lines) #// outputs ['line 1', 'line 2']

#str = "Bananas in binary"
#search = str.find("a", 2,5)
#print(f"{search}")

#print(string.isdecimal())
#new_string = ("-" * 20 + "Menu" + "-" * 20)
#print(new_string)

#print (list(range(0,6,2)))

#print("Numbers 1 - 10\n")
#for i in range(1,10,1):
    #print(f"Number {i} is: {i}")
#print(f"So the answer is {range(0,4).count(1)}")

#print(range(2,6,1).index(3))

#print(range(2,6)[1])

#goat = ["LBJ", "MJ", "KOBE"]

#for i in goat:
 #   print(f"{i}")

# sum = 0
# for number in range(1,11):
#     print(f"number: {number}")
#     sum += number
# print(f"sum is: {sum}")

nums = [1, 2, 3, 4, 5, 6]
evens = []
for x in nums:
    if x % 2 == 0:
        evens.append(x)
print(evens)  # [2, 4, 6]

my_set = {1,2,3,4,5}
my_set.add(7)
print(my_set)
