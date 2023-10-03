#counter = 0
#while counter < 10 :
 #   counter += 1 #инкремент
    #print (counter, 'итерация')
  #  continue
#    break
name = 'Илья Муромец'


way_left = False
way_center = False
way_right = False
while way_left == False and way_center == False and way_right == False:
    print (name, 'приехал к камню, на нем надпись :')
    print ('Налево поехать - убитым быть,')
    print ('Прямо поехать - женатым быть,')
    print ('Направо поехать - богатым быть.')

    way = input ('В какую сторону поехать? ')
    if way == 'налево' :
        if way_left == False :
        elif way_left == True :
                print(name, 'уже был на левой дороге')
            print (name, 'вышел на разбойников')
            choose = input ('Что делать? биться или бежать? ')
            if choose == 'биться':
                print (name, 'раскидал всех разбойников и стал их предводителем')
            elif choose == 'бежать':
                print (name, 'убежал от разбойников назад')
                way_left == True
                continue
            way_left == True 
    elif way == 'направо':
        if way_right == False :
            print (name, 'богат')
            way_right == True
    elif way == 'прямо':
        if way_center == False :
            print (name, 'женат')
            way_center == True
    break
print ('Игра окончена')





