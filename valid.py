import string 


def is_valid_mode(answer,amount):
    options = list(map(str, list(range(1,amount+1))))
    if answer in options:
        return True
    return False

def is_valid_name(name):
    symbols = list(string.punctuation) + list('0123456789')
    if len(name) <= 2:
        return False
        
    for s in symbols:
        if s in name:
            return False
    return True

def is_correct_grade(grade: str) -> bool:
    try:
        n = float(grade)
        if 0 <= n <= 10:
            return True
        return False
    except:
       return False 

def is_id_correct(id: str) -> bool:
    if id.isdigit():
        return True
    return False

def is_correct_answer(answer: str) -> bool:
    if answer.lower() in ('да','нет',''):
        return True
    return False
