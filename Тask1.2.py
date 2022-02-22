time = int(input("введите время в секундах >>>"))

hors = time // 3600

minutes = (time - hors * 3600) // 60

seconds = time - (hors * 3600 + minutes * 60)

print(f"время в формате чч:мм:сс {hors} : {minutes} : {seconds}")
