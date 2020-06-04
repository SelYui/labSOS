# -*- coding: utf-8 -*-
'''
Формирование массивов столбцов таблицы с ИД
Создание файла в docx и заполнение его для всех студентов
для рабораторной работы 1
'''
import random

from lib import module

#вид таблицы с исходными данными
mas_id = module.lab_read(1, 1)    #всего PP_mas_id пунктов, str_mas_id кодов сообщения

#подпись столбцов
label_column = module.lab_read(1, 4)
#возможные идентификаторы запроса
id_mas_zap = module.lab_read(1, 7)
id_mas_pre_zap = module.lab_read(1, 8)
id_mas_zap_post = module.lab_read(1, 9)
#Возможные идентификаторы ФПО
id_mas_fpo = module.lab_read(1, 12)
id_mas_pre_fpo = module.lab_read(1, 13)
id_mas_fpo_post = module.lab_read(1, 14)
#тип обмена
id_mas_type = module.lab_read(1, 17)

#всего PP_mas_id пунктов, str_mas_id кодов сообщения
PP_mas_id = len(mas_id)
str_mas_id =  sum(int(mas_id[i]) for i in range(PP_mas_id))

'''
лаба 1
массивы с возможными характеристиками таблицы.
всего 5 пунктов. Массив из пяти элементов. Каждый элемент показывает количество кодов сообщений в каждом пункте
Рандомно формируем количество кодов сообщений в каждом пункте
'''   
def id_lab1():
    random.seed()                   #настраиваем генератор случайных чисел
    '''
    создаем столбцы:
        code_mess - код сообщения
        fpo_req_id - идентификатор запроса ФПО
        micro_addr - адрес в микросхеме
        fpo_exch_id - идентификатор обмена для ФПО
        type_exch - тип обмена
    '''
    
    random.shuffle(mas_id)          #перемешиваем нашу таблицу
    code_mess = random.sample(range(499),str_mas_id) # создаем массив кодов сообщения с уникальными значениями (от 1 до 500)
    code_mess = [k+1  for k in code_mess]
    
    #формируем идентиф. запроса ФПО и заносим их в столбец(массив), пока он не будет уникальным
    while True:
        fpo_req_id = zap_fpo()
        #проверяем уникальность множеством
        set_f_req = set(fpo_req_id)
        if len(set_f_req) == len(fpo_req_id):
            break
        
    micro_addr = random.sample(range(255),str_mas_id)    #формируем массив адресов в микросхеме с уникальными значениями
    micro_addr = [hex(micro_addr[k]) for k in range(str_mas_id)]    #представляем их ввиде hex
    
    fpo_exch_id = comand_fpo()    #формируем массив идентификаторов обмена для ФПО
    
    type_exch = recv_send()     #формируем массив типеа обмена
    
    return (mas_id, code_mess, fpo_req_id, micro_addr, fpo_exch_id, type_exch)
    
        
#функция формирования рандомного идентификатора запроса ФПО
def zap_fpo():
    #сколько будет видов запросов ФПО
    cnt_fpo = PP_mas_id
    id_zap_fpo = []
    value_zap_fpo = []
    #формирование названий для переменных запроса ФПО
    for i in range(cnt_fpo):
        zap_fpo = random.choice(id_mas_zap)
        if(zap_fpo == 'Zap'):
            post = random.choice(id_mas_zap_post)
            #если число, то генерируем случайное число от 0 до 10
            if(post == 'numb'):
                post = str(random.randrange(0,10,1))
            #если _число, то генерируем случайное число от 20 до 50
            elif(post == '_numb'):
                post = '_' + str(random.randrange(20,50,1))
            zap_fpo = zap_fpo + str(post)
        else:
            zap_fpo = random.choice(id_mas_pre_zap) + zap_fpo
        id_zap_fpo.append(zap_fpo)  #получили массив всевозможных запросов
    
    #у кого какие биты выставлены
    index_fpo = random.randrange(0,PP_mas_id-1,1)     #определяем у какого пункта будет диапазон бит
    index_fpo2 = sum(int(mas_id[i]) for i in range(index_fpo))       #индекс в массиве id_zap_fpo
    #составляем массив значений запроса ФПО
    for i in range(str_mas_id):
        if ((i < index_fpo2) or (i > index_fpo2 + int(mas_id[index_fpo]) - 1)):
            value_zap_fpo.append(str(random.randrange(0,15,1)))
        else:
            ch_bit = random.randrange(3,4,1)    #определяем длинну и величину диапазона бит
            temp1 = random.randrange(0,16-ch_bit,1)    #определяем диапазон бит
            temp2 = random.randrange(1,2**ch_bit-1,1)    #определяем значение диапазона
            value_zap_fpo.append(str(str(temp1) + '\u2011' + str(temp1+3) + '(' + str(temp2) + ')'))    #с неразрывным тире
    
    #рандомно составляем столбец запросов ФПО
    return [(random.choice(id_zap_fpo) + '/' + value_zap_fpo[i]) for i in range(str_mas_id)] # создаем массив кодов сообщения

#функция формирования столбца с идентификатором команды для ФПО
def comand_fpo():
    #сколько будет видов команд для ФПО
    cnt_fpo = PP_mas_id
    
    temp2 = []
    id_com_fpo = []
    value_com_fpo = []
    #формирование названий для переменных команд для ФПО
    for i in range(cnt_fpo):
        com_fpo = random.choice(id_mas_fpo)
        pre = random.choice(id_mas_pre_fpo)
        #если не none, то добавляем префикс
        if(pre != 'none'):
            com_fpo = pre + com_fpo

        id_com_fpo.append(com_fpo)
        value_com_fpo.append(random.randrange(0,10,1))
        #заполняем столбец инкрементируя индекс идентификатора
        post = random.choice(id_mas_fpo_post)
        for j in range(int(mas_id[i])):
            #добавляем либо массив, либо число
            if(post == 'numb'):
                temp1 = str(value_com_fpo[i]*10 + j)
            elif(post == '_numb'):
                temp1 = '_' + str(value_com_fpo[i]*10 + j)
            else:   #добавляем массив
                temp1 = '[' + str(value_com_fpo[i] + j) + ']'
            temp2.append(id_com_fpo[i] + temp1)
            
    return temp2

#функция формирования рандомного тика обмена (с учетом того что должна быть как минимум одна выдача и один прием)
def recv_send():
    ind1 = ind2 = 1234
    while ((ind1 == 1234) or (ind2 == 1234)):
        temp1 = [random.choice(id_mas_type) for i in range(PP_mas_id)]  #определили тип передачи для каждого пункта
        try:
            ind1 = temp1.index('прием')
        except:
            ind1 = 1234
        try:
            ind2 = temp1.index('выдача')
        except:
            ind2 = 1234
    
    #составляем столбец для каждого запроса
    i = 0
    temp2 = []
    while i < PP_mas_id:
        for j in range(int(mas_id[i])):
            temp2.append(temp1[i])
        i += 1
    return temp2
