import ui 
import working_on_a_file as file


def running():
    
    if file.is_new_file():
            file.create_columns()
    set_films = file.create_set_films()
    
    while True:
        mode = ui.main_menu()
        if mode == '1':
            ui.print_all_serals()
            answer = ui.end_menu()
            
            if answer == '1':
                if file.is_content():
                    
                    id = ui.get_id_series()
                    name = file.delete_series(id) 
                
                    print(f'Сериал "{name}" удалён!')
                else:
                    print('Вы не можете удалить сериал, так как список пуст!')
                ans = ui.print_back_main()
                if ans in ('да',''):
                    continue
                if ans == 'нет':
                    break
            elif answer == '2':
                continue
                  
        elif mode == '2':    
            mode_write = ui.select_mode()
    
            while True:
                
                film, grade = ui.input_series(set_films,mode_write)
                file.is_series_in_data(set_films,film)
                answer = input('Добавить следющий сериал?')
                
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
    