import ui 
import working_on_a_file as file





def capter_delete_series():
    '''Ветка удаления сериала'''

    if file.is_content():
        id_series = ui.get_id_series()
        name = file.delete_series(id=id_series)
        print(f'Сериал "{name}" удалён!')
    else:
        print('Вы не можете удалить сериал, так как список пуст!')

def branch_1() -> bool:
    '''Ветка 1'''
          
    ui.show_all_serals()
    answer = ui.select_del_or_main()

            
    if answer == '1':
        capter_delete_series()
        ans = ui.print_back_main()
                
        if ans in ('да',''):
            return True
        if ans == 'нет':
            return False
    elif answer == '2':
        return True

def running():
    
    if file.is_new_file():
            file.create_columns()
    set_films = file.create_set_films()
    
    while True:
        mode = ui.select_main_menu()

        if mode == '1':
            next_step = branch_1()
            if next_step is True:
                continue
            break
                  
        elif mode == '2':    
            mode_write = ui.mode_selections()
    
            while True:
        
                ui.input_films(set_films,mode_write)
                answer = input('Добавить следющий сериал? ')
                
                if answer.lower() == 'нет':
                    break
            
            ans = ui.print_back_main()
            if ans in ('да',''):
                continue
            if ans == 'нет':
                break
            
        elif mode == '3':
            file.clean_csv_file()
            ans = ui.print_back_main()
            if ans in ('да',''):
                continue
            if ans == 'нет':
                break
        elif mode == '4':
            break
            
            
        
if __name__ == '__main__':
    running()
    