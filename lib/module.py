# -*- coding: utf-8 -*-
'''
Модули для записи и чтения системных файлов
А также некоторые служебные модули
'''
import os, datetime

#запись в лог файл сбоев + даты сбоя
def log_info(msg):
    ''' пример вызова
    module.log_info("date: %s" % date)
    '''
    #получаем время сбоя
    log_time = datetime.datetime.now()
    #записываем сбой в файл
    f = open("lib/setting.log", "a", encoding = 'utf-8')
    f.write(msg + "            " + str(log_time) + "\n")
    f.close()

#запись списка студентов в файл
def write_student_list(ListStudent, enter_const):
    #удаляем лишние пробелы
    ListStudent = del_space(ListStudent)
    #если список не пустой и не имеет строки "Введите список группы"
    if (ListStudent != '') and (ListStudent != ' ') and (ListStudent.find(enter_const) == -1):
        #сохраняем весь список строк в файл
        try:
            save_f = open('lib/list_student.txt', 'w', encoding = 'utf-8')
            save_f.writelines(ListStudent)
        except Exception as e:
            log_info("write_student_list: не удалось записать в файл (%s)"% e)
        finally:
            save_f.close()

#считываем из файла сохраненный ранее сипсок группы (если он есть)
def read_student_list():
    #читаем файл построчно и возвращаем 22 строку
    try:
        read_f = open('lib/list_student.txt', 'r', encoding = 'utf-8')
    except:
        return 1                #файла нет, ничего не делаем
    with read_f:
        try:
            list = read_f.read()
            return list
        except:
            return 1            #файл есть, но не читается

#удаление списка группы, если он существует
def delite_student_list():
    if os.path.exists('lib/list_student.txt'):
        os.remove('lib/list_student.txt')

#считываем из файла заданной строки
def lab_read(num_lab, num_setting):
    #обнуляем переменную
    date = '' #не выставлен
    #делаем 10 попыток чтения
    for cnt_read in range(10):
        #читаем файл построчно и возвращаем 22 строку
        f = open('lib/lab'+str(num_lab)+'_setting.ini', 'r', encoding = 'utf-8')
        with f:
            lines = f.readlines()
            try:
                date = lines[num_setting]
                break
            except:
                log_info("lab_read: не считалась строка: %s %s %d раз" % (num_lab, num_setting, cnt_read+1))
    else:
        log_info("lab_read: не удалось считать строку: %s %s" % (num_lab, num_setting))
    #удаляем пробелы и преобразуем в массив разделяя точкой с запятой
    date = date.replace('; ',';')
    date = date.split(';')
    #без символа переноса строки, возвращаем тип srt
    return date[:-1]

#удаляем лишние пропуски в списке
def del_space(ListStudent):
    while ("Введите список группы" in ListStudent):
        ListStudent= ListStudent.replace("Введите список группы", "")
    while ("  " in ListStudent):
        ListStudent= ListStudent.replace("  ", " ")
    while (" \n" in ListStudent):
        ListStudent= ListStudent.replace(" \n", "\n")
    while ("\n\n" in ListStudent):
        ListStudent= ListStudent.replace("\n\n", "\n")
    while True:
        if (len(ListStudent) > 0) and (ListStudent[-1] == ' '):
            ListStudent = ListStudent[:-1]
        elif (len(ListStudent) > 0) and (ListStudent[-1] == '\n'):
            ListStudent = ListStudent[:-1]
        elif (len(ListStudent) > 0) and (ListStudent[0] == ' '):
            ListStudent = ListStudent[1:]
        elif (len(ListStudent) > 0) and (ListStudent[0] == '\n'):
            ListStudent = ListStudent[1:]
        else:
            break

    return ListStudent