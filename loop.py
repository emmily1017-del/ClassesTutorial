i=1

while(i<=20):
    print(i)
    i+=1
else:
    print("i is no longer less or equal to 20")
fruits = ["apple","mango","banana","pineapple","strawberry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(5,20,4):
    print(x)
fruit_response=input("What do you want to eat?")
print(fruit_response)