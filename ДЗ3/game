import random

n, m = 0, 0
while n < 4 or m < 4:
    n = int(input("Введите высоту карты (не менее 4)>>>"))
    m = int(input("Введите ширину карты (не менее 4)>>>"))
    
map_view = [['*' for _ in range(m)] for _ in range(n)]
map_real = [['*' for _ in range(m)] for _ in range(n)]
hp = 100
inv = ['A_SWORD']

p_y, p_x = n - 1, m - 1
map_real[p_y][p_x] = 'portal'
c_y, c_x = n - 3, m - 1
map_real[c_y][c_x] = 'chest'
m_y, m_x = n - 1, m - 3
map_real[m_y][m_x] = 'monster'

traps = [[n - 2, m - 1], [n - 1, m - 2], [n - 4, m - 3], [n - 3, m - 2]]
for y, x in traps:
    map_real[y][x] = 'trap'

x, y = 0, 0
map_view[y][x] = 'X'

print('='*50)
print('Крестик "X" — ваше расположение на карте')
print('Точка "."  — места, где вы уже побывали')
print('Карта скрыта! Вы узнаете, что в клетке, только когда наступите')
print('Управление: W — вверх, A — влево, S — вниз, D — вправо')
print('Дополнительно: команда sort — сортировка вещей, команда reverse — развернуть инвентарь, команда drop — выбросить вещь')
print('='*50)
print('Итак, начнем наше приключение!')

while hp > 0:
    print('--- ТЕКУЩАЯ КАРТА ---')
    for row in map_view: 
        print(' '.join(row))
    print(f'Здоровье: {hp} HP')
    print(f'Инвентарь: {inv}')
    
    cmd = input('Куда шагнем или что сделаем?>>>').strip().lower()
    
    is_cmd = False
    
    if cmd == 'sort':
        inv.sort()
        print('Инвентарь успешно отсортирован по алфавиту')
        is_cmd = True
    elif cmd == 'reverse':
        inv.reverse()
        print('Инвентарь успешно перевернут задом наперед')
        is_cmd = True
    elif cmd == 'drop':
        item = input('Какой предмет вы хотите выбросить?>>>').strip()
        if item in inv:
            if item == 'A_KEY':
                print('Система безопасности: Запрещено выбрасывать истинный ключ A_KEY')
            elif item == 'A_SWORD':
                print('Система безопасности: Запрещено выбрасывать A_SWORD, пока монстр жив')
            else:
                inv.pop(inv.index(item))
                print(f'{item} успешно выброшен из инвентаря')
        else:
            print('Такого предмета нет в вашем инвентаре')
        is_cmd = True
        
    if not is_cmd:
        old_x, old_y = x, y
        move_ok = True
        
        if cmd == 'a': x -= 1
        elif cmd == 'd': x += 1
        elif cmd == 'w': y -= 1
        elif cmd == 's': y += 1
        else:
            print('Неверная команда. Используйте WASD для ходьбы или sort/reverse/drop для инвентаря')
            move_ok = False
            
        if move_ok:
            if x < 0 or x > m - 1 or y < 0 or y > n - 1:
                print('Там стена. Сюда пройти нельзя, пожалуйста, сделайте другой ход')
                x, y = old_x, old_y
            else:
                cell = map_real[y][x]
                step_ok = True
                
                if cell == 'trap':
                    if 'C_KIT' in inv:
                        print('Вы активировали скрытую ловушку')
                        print('Но у вас была походная аптечка C_KIT, вы использовали её и не потеряли здоровье')
                        inv.remove('C_KIT')
                    else:
                        hp -= 25
                        print('Вы наступили на скрытые стальные шипы. Потеряно 25 HP')
                        if hp <= 0:
                            print('Ваше здоровье упало до 0. Вы погибли, игра завершена')
                            break
                    map_view[y][x] = 'trap'
                    map_real[y][x] = '*'
                    
                elif cell == 'monster':
                        print('Вы наткнулись на монстра. Используя меч A_SWORD, вы побеждаете его.')
                        print('Меч A_SWORD сломался в процессе боя')
                        inv.remove('A_SWORD')
                        
                        inv.extend(['A_KEY', 'B_SWORD'])
                        inv.insert(0, 'A_SHIELD')
                        
                        print('Вы обыскали логово монстра и нашли: щит A_SHIELD, новый меч B_SWORD и истинный ключ A_KEY')
                        map_real[y][x] = '*'
                        
                elif cell == 'chest':
                    print('Вы нашли старинный сундук со сокровищами')
                    loot_pool = ['F_KEY', 'C_KIT', 'GOLD_COIN']
                    loot = loot_pool.pop(random.randint(0, 2))
                    inv.append(loot)
                    print(f'Вы открыли сундук и достали оттуда предмет: {loot}. Он добавлен в инвентарь')
                    map_real[y][x] = '*'
                    
                elif cell == 'portal':
                    print('Перед вами находится древний портал')
                    if 'A_KEY' in inv:
                        print('Вы использовали истинный ключ A_KEY для активации портала')
                        print('Портал успешно открылся, и вы сбежали. Победа')
                        break
                    elif 'F_KEY' in inv:
                        print('Вы пробуете применить F_KEY. Портал гудит, но этот ключ не подходит. Ищите другой')
                        map_view[y][x] = 'portal'
                        x, y = old_x, old_y
                        step_ok = False
                    else:
                        print('Портал закрыт. Чтобы его активировать, необходим подходящий ключ')
                        map_view[y][x] = 'portal'
                        x, y = old_x, old_y
                        step_ok = False
                        
                if step_ok:
                    map_view[old_y][old_x] = '.'
                    map_view[y][x] = 'X'

