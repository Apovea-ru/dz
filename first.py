seconds=input('Введите количество секунд:')
#1 подзадача
print(seconds,'сек')

#2 подзадача
minutes=int(seconds)//60
seconds_in_time=int(seconds)-60*minutes

print(minutes, 'мин', seconds_in_time, 'сек')

#3 подзадача, тут количество секунд только до суток:P
hours=int(seconds)//3600
minutes=int(seconds)//60-hours*60
seconds_in_time=int(seconds)-60*minutes-3600*hours

if hours==1:
    print(hours, 'час', minutes, 'мин', seconds_in_time, 'сек')
elif hours==2 or hours==3 or hours==4 or hours==22 or hours==23 or hours==24:
    print(hours, 'часа', minutes, 'мин', seconds_in_time, 'сек')
else:
    print(hours, 'часов', minutes, 'мин', seconds_in_time, 'сек')

#4 подзадача, тут количество до месяца.
days=int(seconds)//86400
hours=int(seconds)//3600-days*24
minutes=int(seconds)//60-hours*60-days*1440
seconds_in_time=int(seconds)-60*minutes-3600*hours-days*86400

if days==1 or days==21 or days==31:
    if hours == 1:
        print(days,'день', hours, 'час', minutes, 'мин', seconds_in_time, 'сек')
    elif hours == 2 or hours == 3 or hours == 4 or hours == 22 or hours == 23 or hours == 24:
        print(days,'день', hours, 'часа', minutes, 'мин', seconds_in_time, 'сек')
    else:
        print(days,'день', hours, 'часов', minutes, 'мин', seconds_in_time, 'сек')
elif days==2 or days==3 or days==4 or days==22 or days==23:
    if hours == 1:
        print(days,'дня', hours, 'час', minutes, 'мин', seconds_in_time, 'сек')
    elif hours == 2 or hours == 3 or hours == 4 or hours == 22 or hours == 23 or hours == 24:
        print(days,'дня', hours, 'часа', minutes, 'мин', seconds_in_time, 'сек')
    else:
        print(days,'дня', hours, 'часов', minutes, 'мин', seconds_in_time, 'сек')
else:
    if hours == 1:
        print(days,'дней', hours, 'час', minutes, 'мин', seconds_in_time, 'сек')
    elif hours == 2 or hours == 3 or hours == 4 or hours == 22 or hours == 23 or hours == 24:
        print(days,'дней', hours, 'часа', minutes, 'мин', seconds_in_time, 'сек')
    else:
        print(days,'дней', hours, 'часов', minutes, 'мин', seconds_in_time, 'сек')