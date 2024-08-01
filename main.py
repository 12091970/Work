#http://dia-calc.ru/cats/?cat=products



product = {'номер': 1, 'продукт': 'ИНЖИР'},{'номер': 2, 'продукт': 'ХЛЕБ ПШЕНИЧНЫЙ'},\
          {'номер': 3, 'продукт': 'ЧЕРНОСЛИВ'}, \
          {'номер': 4,'продукт':'КРУПА(овсяная,манная,пшеничная'},\



product_0XE = {'продукт':'МЯСО ЛЮБОЕ(ВАРЁНОЕ)'},{'продукт':'МАСЛО РАСТИТЕЛЬНОЕ'},\
    {'продукт': 'СЫР,ТВОРОГ'},  {'продукт':'ЗЕЛЕНЬ'}







weight = {"номер":1001, "граммы":"20"},{"номер":1002,"граммы":"40"},\
{"номер":1003,"граммы": "60"}


global choice_id1
def product_id():
    global choice_id1
    choice_id1 = int(input("Введите номер продукта:"))
    location1 = [l for l in product if l['номер'] == choice_id1][0]
    print(location1)





global choice_id2
def weight_id():
    global choice_id2
    choice_id2 = int(input("Введите номер веса:\n"))
    location2 = [l for l in weight if l["номер"] == choice_id2][0]
    print(location2)


print('Добро пожаловать в Справочник для Исулинозависимых Больных! ')

while True:     # бесконечный цикл
    print("1. Выберите продукт")
    print("2. Выберите вес продукта ")
    print("3. Количество инсулина для выбранного веса продукта")
    print("4. Информация о физических нагрузках")
    print("5. Всё о лекарствах для диабетика")
    print("6. Выход")
    choice_menu = int(input("Выберите пункт меню:\n"))
    if choice_menu == 1:
        print('СПИСОК ПРОДУКТОВ,НЕ ТРЕБУЮЩИХ ВВЕДЕНИЯ ИНСУЛИНА!')
        for key in product_0XE:
         print(key)

        print('А ЭТИ ПРОДУКТЫ ПОД НОМЕРАМИ ТРЕБУЮТ ВВЕДЕНИЯ ИНСУЛИНА!')
        for value in product:
         print(value)


    elif choice_menu == 2:
          print("Выберите сначала пункт 1:")
          exit()

    elif choice_menu == 3:
          print("Выберите сначала пункт 1:")
          exit()
    elif choice_menu == 4:
         print('ЖМИ ССЫЛКУ НИЖЕ!')
         print('https://www.10gkb.by/informatsiya/stati/fizicheskie-nagruzki-u-bolnykh-sakharnym-diabetom')
         exit()
    elif choice_menu == 5:
        print('Ограничения в приёме лекарств!')
        print('Жми ссылку')
        print('https://www.katrenstyle.ru/goods_sales/diabet_ogranicheniya_v_prieme_ls?ysclid=lhtjw7n613956118890')
        exit()
    elif choice_menu == 6:
         print('ДО СВИДАНИЯ !')
         exit()

    product_id()


    choice_menu1 = int(input("Жмите пункт 2,чтоб посчитать количество:\n"))
    if choice_menu1 == 2:
            print(weight)
    else:
        print("Ошибка, нужно нажать : 2")
        exit()
    weight_id()

    choice_menu2 = int(input("Жмите 3, чтоб посчитать хлебные единицы и инсулин:\n"))
    if choice_menu2 == 3:
        print("Секундочку,подсчитываем:")
        print()


    if choice_id1 == 1 or 2 or 3 or 4:
        if choice_id2 == 1002:
          print('2 ХЛЕБНЫЕ ЕДИНИЦЫ')
          print()
          print('На завтрак: 4 ЕД.ИНСУЛИНА на 2 ХЕ')
          print('На обед: 3-3,5 ЕД.ИНСУЛИНА на 2 ХЕ')
          print('На ужин: 3—3,5 ЕД.ИНСУЛИНА  на 2 ХЕ')
          print()



    if choice_id2 == 1001:
       if choice_id1 == 1 or 2 or 3 or 4:
         print('  1 ХЛЕБНАЯ ЕДИНИЦА ')
         print()
         print('На завтрак: 2 ЕД.ИНСУЛИНА на 1 ХЕ')
         print('На обед: 1-1,5 ЕД.ИНСУЛИНА на 1 ХЕ')
         print('На ужин: 1—1,5 ЕД.ИНСУЛИНА  на 1 ХЕ')
         print()


    if choice_id1 == 1 or 2 or 3 or 4:
        if choice_id2 == 1003:
          print('3 ХЛЕБНЫЕ ЕДИНИЦЫ')
          print()
          print('На завтрак: 6 ЕД.ИНСУЛИНА на 3 ХЕ')
          print('На обед: 5-5,5 ЕД.ИНСУЛИНА на 3 ХЕ')
          print('На ужин: 5—5,5 ЕД.ИНСУЛИНА  на 3 ХЕ')
          print()






#https://codeby.net/threads/slovari-vyvod(input-tolko-znachenija-dlja-vvedennogo-kljucha-python.64243/?ysclid=lgo21we2uw397117089




#print(weight[0]["name"]) # Первым будет значение под 0 индексом






            #dict(filter(lambda item:   , d.items()))












#def choice_id_product():
    #choice_user = int(input("Выбери id продуктa "))
   # choice = [c for c in product if c["id"] == choice_user][0]
    #print(choice)


#OPTIONS = { 1:['Вывести список продукции',choice_id_product]}









