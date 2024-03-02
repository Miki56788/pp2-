#1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#sets unordered and unchangeble but u can remove and add {}
#sets undex

#2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")