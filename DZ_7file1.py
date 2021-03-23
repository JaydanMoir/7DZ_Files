import os

def book_reading():
  cook_book = {}
  file_book = os.path.join(os.getcwd(), "recipes.txt")
  with open(file_book, "r", encoding="utf-8") as f:
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
      cook_book[name_dish] = ing_list
  return cook_book


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
  return ingredients


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

  return file4

# print(book_reading())
print(get_shop_list_by_dishes(book_reading(), 4))
sorting()
