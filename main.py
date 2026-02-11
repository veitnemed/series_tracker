import ui 
import working_on_a_file as file


def add_set(set_films,film):
    return set_films.add(film.replace(' ', '').lower())


def capter_delete_series():
    '''Ветка удаления сериала'''

    if file.is_content():
        id_series = ui.ask_id_series()
        name = file.delete_series(id=id_series)
        print(f'Сериал "{name}" удалён!')
    else:
        print('Вы не можете удалить сериал, так как список пуст!')

def show_serials() -> bool:
    '''Выводим всё содержимое csv файла '''
          
    
    answer = ui.ask_del_or_back()

            
    if answer == '1':
        capter_delete_series()
        ans = ui.print_back_main()
                
        if ans in ('да',''):
            return True
        if ans == 'нет':
            return False
    elif answer == '2':
        return True


def add_series(set_series)-> bool:
    '''Вводим название сериала, оценку и проверяем на уникальность '''

    mode_write = ui.ask_mode_selection()
    


    while True:
        series = ui.ask_series(set_series)
        gread = ui.ask_gread()
        next_read = ui.ask_next_series()
        if next_read is True:
            continue
        break


def clean_file()-> bool:
    '''Отчищаем файл и перезаписываем заголовки '''
    
    file.clean_csv_file()
    answer = ui.print_back_main()
    
    if answer == 'нет':
        return False
    return True
    

def running():
    
    if file.is_new_file():
            file.create_columns()
    set_films = file.create_set_films()
    
    while True:
        mode = ui.ask_main_menu()

        if mode == '1':
            ui.print_emty_rows(50)
            next_step = show_serials()
            if next_step is False:
                break
            
                  
        elif mode == '2': 
            ui.clean_terminal()
            next_step = add_series(set_films)
            if next_step is False:
                break
            
        elif mode == '3':
            ui.clean_terminal()
            next_step = clean_file()
            if next_step is False:
                break
        elif mode == '4':
            break
            
            
        
if __name__ == '__main__':
    running()
    