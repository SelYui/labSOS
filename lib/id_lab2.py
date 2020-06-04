# -*- coding: utf-8 -*-
'''
Формирование массивов столбцов таблицы с ИД
для рабораторной работы 2
'''
import random

from lib import module

id_system = module.lab_read(2, 4)
id_system_en = module.lab_read(2, 5)
id_pre_zap = module.lab_read(2, 8)
id_word_data = module.lab_read(2, 11)
id_szo = module.lab_read(2, 14)

def id_lab2():
    random.seed()                   #настраиваем генератор случайных чисел
    '''
    создаем столбцы:
        system_mass - система
        exch_mass - обмен
        mumb_ou - номер ОУ
        form_mass - Формат
        sub_addr - подадрес
        num_dats - число слов данных
        fpo_req - запрос ФПО
        id_data - иднтификатор слов данных
        szo_mass - СЗО
    '''
    #два рандомных числа, обозначающих системы
    sys = random.sample(range(len(id_system)),2)
    
    #формируем массивы систем
    system_mass = [id_system[i] for i in sys]   #массив систем
    mass_zap = []
    exch_mass = []
    form_mass = []
    temp1 = [id_system_en[i] for i in sys]
    
    for k in range(2*len(sys)):
        mass_zap.append(str(temp1[k // 2]))     #массив систем_en
        #формируем массив обменов и формат
        form_mass.append(2 - (k%2))             #массив форматов
        #формируем массив обменов
        if int(form_mass[k]) == 2:
            exch_mass.append('Прием')
        elif int(form_mass[k]) == 1:
            exch_mass.append('Выдача')
    
    mumb_ou = random.sample(range(32),len(sys))    #формируем рандомный столбец с номером ОУ от 0 до 31
    
    sub_addr = random.sample(range(32),2*len(sys))   #формируем рандомный столбец с подадресом от 0 до 31
    
    num_dats = [random.randrange(3,33,1) for k in range(2*len(sys))]   #формируем рандомный столбец с числом слов от 3 до 32
    
    fpo_req = zap_fpo(sys, mass_zap)       #формируем идентиф. запроса ФПО и заносим их в столбец(массив)
    
    id_data = id_data_fpo(sys, mass_zap, num_dats)      #формируем массив идентификаторов слов данных для ФПО
    
    szo_mass = [('szo'+mass_zap[k]+str(id_szo[k%2])) for k in range(len(mass_zap))]
    
    return (system_mass, exch_mass, mumb_ou, form_mass, sub_addr, num_dats, fpo_req, id_data, szo_mass)

#функция формирования идентиф. запроса ФПО с заносим их в столбец(массив)
def zap_fpo(sys, mass_zap):
    temp3 = [random.choice(id_pre_zap) for i in range(len(sys))]  #формируем префиксы
    zap_pre = []
    value_zap_fpo = []
    unic_bit = random.sample(range(16),len(sys))    #формируем уникальные биты для второй системы
    
    ch_bit = 3    #определяем длинну и величину диапазона бит
    temp1 = random.randrange(0,16-ch_bit,1)    #определяем диапазон бит
    for i in range(2*len(sys)):
        #заполняем массив префиксов
        zap_pre.append(temp3[i // 2])
        #формируем выставление битов
        if i < len(sys):
            temp2 = random.randrange(1,2**ch_bit-1,1)    #определяем значение диапазона
            value_zap_fpo.append(str(str(temp1) + '\u2011' + str(temp1+3) + '(' + str(temp2) + ')'))    #с неразрывным тире
        else:
            value_zap_fpo.append(str(unic_bit[i - len(sys)]))
    #рандомно составляем столбец запросов ФПО
    return [(zap_pre[i] + mass_zap[i] + '/' + value_zap_fpo[i]) for i in range(2*len(sys))] # создаем массив кодов сообщения

#функция формирования столбца идентификаторов слов данных ФПО
def id_data_fpo(sys, mass_zap, num_dats):
    id_data = []
   
    for i in range(2*len(sys)):
        id_data.append(id_word_data[i%2]+mass_zap[i])
    return [(id_data[i]+'[0\u2011'+ str(num_dats[i]-2) +']') for i in range(len(id_data))]
