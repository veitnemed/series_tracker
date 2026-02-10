import csv
from datetime import datetime


def is_new_file():
    '''Проверка есть ли вообше файл'''
    
    try:
        file = open('films.csv','r', encoding='utf-8') 
        file.close()
        return False  
    except:
        return True

def create_columns():
    '''Создание заголовков'''
    
    columns = ['ID','Name','Grade','created_at','status']
    with open('films.csv','w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)

def get_max_id():
    with open('films.csv','r', encoding='utf-8', newline='') as file:
        list_csv = list(csv.reader(file))
        if len(list_csv) == 1:
            return 0
        return int(max(list_csv[1:], key = lambda lst:lst[0])[0])


def add_film(name,grade,status):
    '''Добавить один сериал в конец'''
    
   
    id = get_max_id()+1
    created_at = datetime.today().strftime('%Y-%m-%d')      
    with open('films.csv','a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([id,name,grade,created_at,status])

def create_set_films():
    '''Создание множества названий сериалов '''
    
    set_films = set() 
    with open('films.csv', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        for row in reader:
            if row[1] == 'Name':
                continue
    
            set_films.add(row[1].replace(' ','').lower())
    return set_films

def crated_list_csv():
    with open('films.csv', encoding='utf-8') as file:
        csv_list = list(csv.reader(file))
        
        return csv_list

def clean_csv_file():
    create_columns()

def delete_series(id):
   
    with open('films.csv','r', encoding='utf-8') as file:
        list_csv = list(csv.reader(file))
        for idx, line in enumerate(list_csv[1:]):
            if line[0] == id:
                del_idx = idx
                name = line[1]
    del list_csv[del_idx+1]

    with open('films.csv','w', encoding='utf-8',newline='') as file:
    
       writer = csv.writer(file)
       writer.writerows(list_csv) 
    return name

def is_id_in_file(id):
    with open('films.csv','r', encoding='utf-8',newline='') as file:
        csv_list = list(csv.reader(file))
        if len(csv_list) == 1:
            return False
        for line in csv_list[1:]:
            if line[0] == id:
                return True
        return False
        
def is_content():
    with open('films.csv','r', encoding='utf-8',newline='') as file:
        csv_list = list(csv.reader(file))
        if len(csv_list) == 1:
            return False
    return True
                    
        
        
        
        
        


    