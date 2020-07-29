# -*- coding: utf-8 -*-
'''
Класс для создания ИД в отдельном потоке
'''
import time

from PyQt5.QtCore import QThread, pyqtSignal
from lib import id_lab1, id_lab2, work_docx

#потоковая задача с созданием ИД
class ThreadCreateID(QThread):
    
    finished_create = pyqtSignal()      #сигнал окончания потока
    messageSignal = pyqtSignal(str)     #сигнал ошибки создания ИД
    progressValue = pyqtSignal(int)     #сигнал с прогрессом создания файла 
    
    def __init__(self, ThreadValue):
        super().__init__()
        self.ThreadValue = ThreadValue
        
    #self.ThreadValue = список группы; путь файла для первой лабы; путь файла для второй лабы; номер создаваемой лабы
    def run(self, *args, **kwargs):
        #получаем список группы
        list_student = self.ThreadValue[0]
        F_Name_lab1 = self.ThreadValue[1]
        F_Name_lab2 = self.ThreadValue[2]
        #Num_lab = 1                             #сначала пытаемся создать ИД для первой лабы
        #значение на которое увеличиваем прогрессбар
        count = 50/(len(list_student))
        #создаем файл с ИД для первой лабы
        if (F_Name_lab1 != 'none'):
            #создаем файл с таблицей и ИД
            doc = work_docx.create_docx(1, 2, 2, 2, 2)
            #в цикле для каждого студента формируем массивы
            for i in range(len(list_student)):
                #выдаем сигнал в прогрессбар
                self.progressValue.emit(count*i)
                #составляем массивы для таблицы для каждлго студента
                table_lab1 = id_lab1.id_lab1()
                #запись полученных массивов в docx
                work_docx.work_docx_from_lab1(i, doc, list_student, table_lab1[0], table_lab1[1], table_lab1[2], table_lab1[3], table_lab1[4], table_lab1[5])
            try:
                #сохраняем docx файл
                work_docx.save_docx(doc, F_Name_lab1)
            except Exception as e:
                self.messageSignal.emit('Не удалось создать файл!\n\nException = %s'% e)
        
        #Num_lab = 2                             #теперь пытаемся создать ИД для второй лабы        
        #создаем файл с ИД для второй лабы
        if (F_Name_lab2 != 'none'):
            #создаем файл с таблицей и ИД
            doc = work_docx.create_docx(2, 2, 2, 2, 2)
            #для каждого студента 
            for i in range(len(list_student)):
                #выдаем сигнал в прогрессбар
                self.progressValue.emit(50 + count*i)
                #составляем массивы для таблицы для каждлго студента
                table_lab2 = id_lab2.id_lab2()
                #запись полученных массивов в docx
                work_docx.work_docx_from_lab2(i, doc, list_student, table_lab2[0], table_lab2[1], table_lab2[2], table_lab2[3], table_lab2[4], table_lab2[5], table_lab2[6], table_lab2[7], table_lab2[8])
            try:
                #сохраняем docx файл
                work_docx.save_docx(doc, F_Name_lab2)
            except Exception as e:
                self.messageSignal.emit('Не удалось создать файл!\n\nException = %s'% e)
        self.progressValue.emit(100)
        time.sleep(1)                               #что бы не сразу пропадала шкала
        self.finished_create.emit()
