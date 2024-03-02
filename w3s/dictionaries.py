#1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  #key : Value
}
print(car.get("model"))
print(car["model"])
#dictionaries a ={} ordered changeable and allow duplicates 

#2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print (car.get("year"))
#3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#4
car.pop("model")
#delete

#5
car.clear()
#delete full 
#dictionaries a ={} ordered changeable and allow duplicates 