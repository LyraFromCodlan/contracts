n = int(input())
meals = list()
required_ingridients = set()

shop=list()
nutrition=list()
for meal_index in range(0,n):
    ingridients = list()
    meals.append([info.lower() for info in input().split()])
    for ingridient_index in range(0,int(meals[meal_index][2])):
        ingridients.append([data.lower() for data in input().split()])
        required_ingridients.add(ingridients[ingridient_index][0])
    meals[meal_index].append(ingridients.copy())
    ingridients.clear()
k=int(input())
for shop_ingridient_index in range(0,k):
    ingridient = [data.lower() for data in input().split()]
    if ingridient[0] in required_ingridients:
        shop.append(ingridient)
m=int(input(()))
for nutrition_ingirdient_index in range(0,m):
    ingridient=[data.lower() for data in input().split()]
    if ingridient[0] in required_ingridients:
        nutrition.append(ingridient)

print("meals")
print(meals)
print("required ingridients")
print(required_ingridients)
print("shop")
print(shop)
print("nutrition")
print(len(nutrition))