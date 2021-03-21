import os
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл.'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт.'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л.'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л.'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл.'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг.'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч.'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г.'}
#     ],
#     'Фахитос':[
#     {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г.'},
#     {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт.'},
#     {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л.'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт.'}
#     ]
#   }
# lst = []
# for blood in cook_book.keys():
#   lst.append(blood)

def book_reading():
    cook_book = {}
    with open("recipes.txt", "r", encoding="utf-8") as f:
        for line in f:
            name_dish = line.strip()
            count = int(f.readline())
            ing_list = []
            for elem in range(count):
                ingr = f.readline().strip()
                split_ing = ingr.split(" | ")
                ings = {}
                ings['ingredient_name'] = split_ing[0]
                ings['quantity'] = int(split_ing[1])
                ings['measure'] = split_ing[2]
                ing_list.append(ings)
            f.readline().strip()
            cook_book[name_dish]=ing_list
    return cook_book

#
# print(book_reading())

# def book_creation(recipes):
#   dishes = []
#   with open("book_recipec.txt", "w", encoding="utf-8") as f:
#     for dish, ingredients in recipes.items():
#       dishes.append(dish)
#       f.write(f"{dish}\n")
#       f.write(f"{len(ingredients)}\n")
#       i = 0
#       while i!=len(ingredients):
#         f.write(f'{ingredients[i]["ingredient_name"]} | {ingredients[i]["quantity"]} | {ingredients[i]["measure"]}\n')
#         i+=1
#       f.write("\n")
        # if i==len(ingredients):
        #   print("---------------")
      # for one_ing in ingredients[0].values():
      #   f.write(f"{one_ing}\n")
        # for i in one_ing.values():
          # f.write(f"{i}\n")

    # return dishes

# def get_shop_list_by_dishes(dishes):
#   ingredients = {}
#   i=0
#   for dish, ings in cook_book.items():
#     if dish == dishes[i]:
#       # print(ing)
#       j=0
#       amount_ings = {}
#       while j != len(ings):
#         ings[j]["quantity"] *= 2
#         # print(ings)
#         for val in ings[j].items():
#           print(v)
#         #   # print(k,v)
#         #   amount_ings["quantity"] = v
#         #   amount
#
#
#         j+=1
#       i+=1
#   print(ingredients)
#
# get_shop_list_by_dishes(lst)

def get_shop_list_by_dishes(dishes, count_person):
  ingredients = dict()
  for name_dish in dishes:
    if name_dish in book_reading():
      for ings in book_reading()[name_dish]:

        amount_ings = dict()
        if ings['ingredient_name'] not in ingredients:
          amount_ings['quantity'] = ings['quantity'] * count_person
          amount_ings['measure'] = ings['measure']
          ingredients[ings['ingredient_name']] = amount_ings
        else:
          ingredients[ings['ingredient_name']]['quantity'] += ings['quantity'] * count_person
    else:
      print("Данного блюда нет в книге")

#


def sorting():
  file1 = os.path.join(os.getcwd(), "1.txt")
  file2 = os.path.join(os.getcwd(), "2.txt")
  file3 = os.path.join(os.getcwd(), "3.txt")
  file4 = os.path.join(os.getcwd(), "total.txt")
  files_lst = {}

  with open(file1, "r", encoding="utf-8") as f1:
    f1_lst = f1.readlines()
    files_lst[file1] = f1_lst

  with open(file2, "r", encoding="utf-8") as f2:
    f2_lst = f2.readlines()
    files_lst[file2] = f2_lst

  with open(file3, "r", encoding="utf-8") as f3:
    f3_lst = f3.readlines()
    files_lst[file3] = f3_lst

  # print(files_lst)
  sort_val_lst = sorted(files_lst.values(), reverse=True)
  sort_files_list = {}
  for v in sort_val_lst:
    for k in files_lst.keys():
      if files_lst[k] == v:
        sort_files_list[k] = v

  with open(file4, "w", encoding="utf-8") as f4:
    for key, val in sort_files_list.items():
      f4.write(f"\n{os.path.basename(key)}\n")
      f4.write(f"{len(val)}\n")
      f4.writelines(val)
      f4.write("\n")
  return

get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 4)
sorting()
