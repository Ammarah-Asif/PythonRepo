#Tupple
a=("Sara","Mohammed","Ahmed","Ali","Omar","Mahmoud","Sami")
print(a)
print(a[2])
print(a.count("Ali"))
print(a.index("Omar"))
print(len(a))


#  List
names=[ "Hamza","Ahmed","Ali","Mohammed","Sami","Sara","Omar","Mahmoud","Zara","Zainab","Sierra","Ayezal","Aaira"]
print(names)

print(names[7])

print("add")
names.append("Ammarah")
print(names)

print("remove")
names.remove("Sami")
print(names)

names.pop(5)
print(names)

names.sort()
print(names)

names.reverse()
print(names)

count_Zainab = names.count("Zainab")
print(count_Zainab)


index_Sara = names.index("Sara")
print(index_Sara)

# sets

a=set()
print(a)
a={2,3,5,6,7,8,9,13,14,12,15,11}
print(a)

a.add(16)
print(a)

a.remove(5)
print(a)

len(a)
print(len(a))

a.pop()
print(a)


# Dictionary
words={"amplitude":"The maximum extent of a vibration or oscillation, measured from the position of equilibrium.",
   "watermark":"a faint design made in some paper during manufacture that is visible when held against the light and typically identifies the maker.",
   "calligraphy":"the art of producing decorative handwriting or lettering with a pen or brush.",
   "chlorophyll":"a green pigment, present in all green plants and in cyanobacteria, which is responsible for the absorption of light to provide energy for photosynthesis.",
   "shrub":"a woody plant which is smaller than a tree and has several main stems arising at or near the ground.",
"herbivorous":"animal feeding on plants.",
   "introvert":"a shy, reticent person.",
   "extrovert":"a person who is friendly and outgoing.",
   "vagabond":"a person who is unable to find a job or a home."
  }
print("This is my dictionary you can find in this list->",words.keys())
a=input("Enter the word you want to search for->")
print(words.get(a))
