import working_on_a_file as file
import valid as vd
import os

def print_emty_rows(amount):
    '''Выводи n пустых строк'''

    print('\n'*amount, end='')
    

def clean_terminal():
    os.system('cls')

def ask_main_menu():
    '''Отображает главное меню'''

    print('1. Показать все сериалы')
    print('2. Добавить сериалы')
    print('3. Отчистить csv-файл')
    print('4. Выход','\n')
    
    while True:
        answer = input('>> ').strip()
        if vd.is_valid_mode(answer,4):
            break
        print('Некорректный ввод')
    return answer        


def ask_del_or_back():
    '''Конечное подменю '''

    print('1. Удалить сериал')
    print('2. Главное меню','\n')
    while True:
        answer = input().strip()
        if vd.is_valid_mode(answer,2):
            print_emty_rows(2)
            return answer
        print('Некоректный ввод')
        continue



def ask_id_series():
    '''Удаление сериала по ID (delete_series)'''

    print('Введите ID сериала:', end = ' ') 
    while True:
        id = input().strip()
        if file.is_id_in_file(id) is False:
            print('Такого ID нет!')
            continue
        if vd.is_id_correct(id) is False:
            print('Некорректный ввод')
            continue
        print_emty_rows(1)
        return id
    


def ask_mode_selections():
    '''Вторая ветка, подменю'''

    print('Какие сериалы записать?')
    print('1. Просмотренные')
    print('2. Запланировать просмотр','\n')
    
    while True:
        answer = input().strip()
        if vd.is_valid_mode(answer,2):
            if answer == '1':
                return 'completed'
            else:
                return 'planned'
        print('Некоректный ввод','\n')
        continue
    

def ask_series(set_series):
    '''Ввод названия сериала'''

     # Ввод названия сериала, провера на уникиальность и коррктность
    while True:
        series_name = input('Введите название сериала: ')
        
        if vd.is_valid_name(series_name) is False:
            print('Некорректный ввод','\n')
            continue
        if series_name.replace(' ', '').lower() in set_series:
            print('Сериал уже есть в списке!')
            continue
        break
    return series_name   

def ask_gread():
    while True:
        grade = input('Введиете оценку сериала от 0 до 10: ')
        if vd.is_correct_grade(grade) is False:
            print('Некорректный ввод')
            continue
        break
    return grade

def ask_next_series():
    answer = input('Добавить следющий сериал? ')
                
    if answer.lower() == 'нет':
        return False
    return True    




def input_films(set_films,status):
    '''Ввод названия сериала и оценки'''
    
    # Ввод названия сериала, провера на уникиальность и коррктность
    while True:
        film = input('Введите название сериала: ')
        
        if vd.is_valid_name(film) is False:
            print('Некорректный ввод','\n')
            continue
        if film.replace(' ', '').lower() in set_films:
            print('Сериал уже есть в списке!')
            continue
        set_films.add(film.replace(' ', '').lower())
        break
    
    while True:
        grade = input('Введиете оценку сериала от 0 до 10: ')
        if vd.is_correct_grade(grade) is False:
            print('Некорректный ввод')
            continue
        break
    
    file.add_film(film,grade,status)


def show_all_serals():
    '''Вывод всех сериалов из csv'''

    csv_list = file.crated_list_csv()
    print('\n','------------------')
    if len(csv_list) == 1:
        print('Записанных сериалов нет!')

    
    for id, name, grade, created_at , status in csv_list[1:]:
        
        if status == 'completed':
            status = 'Посмотренно'
        else:
            status = 'Запланированно'

        print(f'{id}: "{name}" {grade}/10 {status}')
    print_emty_rows(2)


def print_back_main():
    '''Возврат в начальную точку'''
    print('Вернуться в главное меню? ')
    while True:
        ans = input().strip().lower()
        if ans in ('да','нет',''):
            return ans  
        print('Некорректный ввод')




      