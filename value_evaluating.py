import sqlite3
import datetime
import random

conn = sqlite3.connect('venv/test1.db')
cur = conn.cursor()

def add_value(user_id, value, date, tablename):
    data = (user_id, value, date)
    cur.execute("INSERT INTO {} VALUES(?,?,?);".format(tablename), data)
    conn.commit()
    pass

def check_last_msg(tablename, user_id,):
    cur.execute("""SELECT value, date FROM {} 
                WHERE user_id = {} 
                ORDER BY rowid DESC;""".format(tablename, user_id))
    one_result = cur.fetchone()
    last_value = one_result[0]
    last_date_str = one_result[1]
    last_date = datetime.datetime.strptime(last_date_str, '%Y-%m-%d').date()
    return (last_value, last_date)

def randomate_value(min, max, random_type = 'gauss', median = 13, sko = 15):
    if random_type == 'gauss':
        value = round(random.gauss(median, sko))
        if value < min and value > -(max/2):
            value += max/2
        elif value < -(max/2):
            value = value*(-1)

        if value > max:
            value = max - random.randint(0, round(max/8))
    elif random_type == 'random':
        value = random.randint(min,max)

    return value

def get_value(user_id, tablename, min, max, random_type):
    today = datetime.date.today()
    try:
        last_value, last_date = check_last_msg(tablename, user_id)
        delta_date = today - last_date
        if delta_date.days !=0:
            today_value = randomate_value(min, max, random_type)
            print(today)
            add_value(user_id, today_value, today, tablename)
        else:
            today_value = last_value
        return today_value
    except(TypeError):
        today_value = randomate_value(min, max, random_type)
        add_value(user_id, today_value, today, tablename)
        return today_value

def depr_evaluate(user_id):
    depr_value = get_value(user_id, tablename='user_depression', min=0, max=63, random_type='gauss')
    result = 'My depression value is: {} \n'.format(depr_value)
    if depr_value < 14:
        result += 'Я здоров \U0001F60C'
    elif depr_value < 20:
        result += 'Cлегка приуныл \U0001F972'
    elif depr_value < 29:
        result += 'Умеренная депрессия \U0001F643'
    elif depr_value == 63:
        result += 'Обыкновенный россиянин \U0001F1F7'
    else:
        result += 'Тяжёлая депря, пора пить таблетки \U0001F92F'
    return(result)

def cock_evaluate(user_id):
    cock_value = get_value(user_id, tablename='user_cock', min=0, max=60, random_type='random')
    result = 'My cock size is {} cm'.format(cock_value)
    if cock_value < 5:
        result += '\U0001F62D'
    elif cock_value < 11:
        result += '\U0001F630'
    elif cock_value < 15:
        result += '\U0001F97A'
    elif cock_value < 23:
        result += '\U0001F601'
    elif cock_value < 34:
        result += '\U0001F60F'
    elif cock_value < 45:
        result += '\U0001F60E'
    else:
        result += '\U0001F631'
    return(result)

def gay_rate_evaluate(user_id):
    gay_rate = get_value(user_id, tablename='user_gay_rate', min=0, max=100, random_type='random')
    result = '\U0001F308 I am {}% gay!\U0001F308'.format(gay_rate)
    return(result)
