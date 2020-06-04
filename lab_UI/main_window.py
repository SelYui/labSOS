# -*- coding: utf-8 -*-
'''
Главное окно программы
'''
import os, sys, time, datetime

from PyQt5.QtWidgets import (QMainWindow, QWidget, QDesktopWidget, QPushButton, QLineEdit, QMessageBox, QStatusBar,
    QFileDialog, QApplication, QCheckBox, QTextEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QProgressBar)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt

from lib import module, work_docx
from lab_UI import sec_stream

#создаем окно наших настроек
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # инициализация GUI
        self.initUI()
        
    def initUI(self):
        #Создаем само окно
        self.resize(500, 500)                                           # Устанавливаем начальные размеры окна
        self.MainWidget = QWidget()                                     # создаем виджет с нашим наполнением
        self.setCentralWidget(self.MainWidget)                          # помещаем виджет в центр
        self.setWindowTitle("Системное БПО")                            # Устанавливаем заголовок окна
        self.setWindowIcon(QIcon('mars.jpg'))                           # Устанавливаем иконку
        self.center()                                                   # помещаем окно в центр экрана
        
    #константы для нашего окна
        self.enter_const = 'Введите список группы'
        
    #Виджеты для пути к папке (лаба1)
        self.le_lab1 = QLineEdit(self)                                  #создаем строку для ввода пути к файлу
        self.le_lab1.setText(os.getcwd()+'\lab1_' + str(datetime.datetime.now().year) + '.docx')#пишем путь текущей директории + lab2_+текущий год
        
        self.btn_lab1 = QPushButton('Выбрать', self)                    #создаем кнопку для изменения расположения файла
        self.btn_lab1.clicked.connect(self.getdir_lab1)                 #действие по нажатию
        self.btn_lab1.setAutoDefault(True)                              # click on <Enter>
        
        self.ch_lab1 = QCheckBox('Лабораторная работа №1', self)        #создаем checkbox для выбора создания ИД для лабы1
        #self.ch_lab1.setFont(QFont('Roboto', 12))                       #Шрифт
        self.ch_lab1.stateChanged.connect(self.sector_lab1)             #действие по нажатию
        self.ch_lab1.setChecked(True)                                   #выставляем
        
    #Виджеты для пути к папке (лаба2)
        self.le_lab2 = QLineEdit(self)                                  #создаем строку для ввода пути к файлу
        self.le_lab2.setText(os.getcwd()+'\lab2_' + str(datetime.datetime.now().year) + '.docx')#пишем путь текущей директории + lab2_+текущий год
        
        self.btn_lab2 = QPushButton('Выбрать', self)                    #создаем кнопку для изменения расположения файла
        self.btn_lab2.clicked.connect(self.getdir_lab2)                 #действие по нажатию
        self.btn_lab2.setAutoDefault(True)                              # click on <Enter>
        
        self.ch_lab2 = QCheckBox('Лабораторная работа №2', self)        #создаем checkbox для выбора создания ИД для лабы1
        #self.ch_lab2.setFont(QFont('Roboto', 12))                       #Шрифт
        self.ch_lab2.stateChanged.connect(self.sector_lab2)             #действие по нажатию
        self.ch_lab2.setChecked(True)                                   #выставляем
        
    #создаем список студентов с кнопкой
        self.nam_stud = TextEdit(self)
        #self.nam_stud.setFont(QFont('Arial', 14))                        #Шрифт
        self.nam_stud.append(self.read_list_student())  #(self.enter_const)
        self.nam_stud.clicked.connect(self.add_student)
        
        self.btn_stud = QPushButton('Импорт', self)                     #создаем кнопку для импорта списка из файла
        self.btn_stud.clicked.connect(self.getfile)                     #действие по нажатию
        self.btn_stud.setAutoDefault(True)                              # click on <Enter>
        
        self.btn_clear = QPushButton('Очистить', self)                  #создаем кнопку для очистки списка группы
        self.btn_clear.clicked.connect(self.clear_nam_stud)             #действие по нажатию
        self.btn_clear.setAutoDefault(True)                             # click on <Enter>
        
    #кнопка для создания файлов
        self.btn_create = QPushButton('Создать', self)                    #создаем кнопку для изменения расположения файла
        self.btn_create.clicked.connect(self.create_docx)                 #действие по нажатию
        self.btn_create.setAutoDefault(True)                              # click on <Enter>
        self.pb_create = QProgressBar()                                 #шкала прогресса создания ИД
        self.pb_create.setValue(0)
    
    #создаем подсказки
        self.tool_tip()
        
    #раскладываем виджеты в главном окне
        self.layout_in_main()
    
    #Функция для центрирования окна в экране пользователя
    def center(self):
        qr = self.frameGeometry()                                       # получаем прямоугольник, точно определяющий форму главного окна.
        cp = QDesktopWidget().availableGeometry().center()              # выясняем разрешение экрана нашего монитора. Из этого разрешения, мы получаем центральную точку.
        qr.moveCenter(cp)                                               # устанавливаем центр прямоугольника в центр экрана. Размер прямоугольника не изменяется.
        self.move(qr.topLeft())                                         # перемещаем верхнюю левую точку окна приложения в верхнюю левую точку прямоугольника qr, таким образом центрируя окно на нашем экране.

    #Функция для расположения виджетов в окне
    def layout_in_main(self):
    #создаем слои и сетки
        self.h_box_ch_lab1 = QHBoxLayout()                              #галочка для лабы 1
        self.h_box_ch_lab1.addWidget(self.ch_lab1)

        self.grid_lab1 = QGridLayout()                                  #сетка для пути к файлу с лабой 1
        self.grid_lab1.addWidget(self.le_lab1, 1, 0, 1, 4)
        self.grid_lab1.addWidget(self.btn_lab1, 1, 5)
        
        self.h_box_ch_lab2 = QHBoxLayout()                              #галочка для лабы 2
        self.h_box_ch_lab2.addWidget(self.ch_lab2)
        
        self.grid_lab2 = QGridLayout()                                  #сетка для пути к файлу с лабой 2
        self.grid_lab2.addWidget(self.le_lab2, 1, 0, 1, 4) 
        self.grid_lab2.addWidget(self.btn_lab2, 1, 5)
        
        #сетка для всего остального
        self.grid_other = QGridLayout()                                 #сетка для списка студентов
        #параметры сетки: начальная строка, начальный столбец, сколько строк занимает, сколько столбцев занимает
        self.grid_other.addWidget(self.nam_stud, 1, 0, 6, 4) 
        self.grid_other.addWidget(self.btn_stud, 3, 4)
        self.grid_other.addWidget(self.btn_clear, 4, 4)
        self.grid_other.addWidget(self.btn_create, 7, 0, 1, 1)
        self.grid_other.addWidget(self.pb_create, 7, 1, 1, 4)
        
        #заносим все в горисонтальный слой
        self.v_box = QVBoxLayout(self.MainWidget)
        self.v_box.addLayout(self.h_box_ch_lab1)
        self.v_box.addLayout(self.grid_lab1)
        self.v_box.addLayout(self.h_box_ch_lab2)
        self.v_box.addLayout(self.grid_lab2)
        self.v_box.addLayout(self.grid_other)
        
        #помещаем на страницу
        self.setLayout(self.v_box)
    
    #создаем подсказки
    def tool_tip(self):
        #self.setToolTip('Программа формирования ИД для\nлабораторных работ по курсу\nсистемное БПО')
        self.le_lab1.setToolTip('Введите путь и имя итого файла\nс ИД для лабораторной №1')
        self.le_lab2.setToolTip('Введите путь и имя итого файла\nc ИД для лабораторной №2')
        self.btn_lab1.setToolTip('Выберите каталог для итогового файла\nс ИД для лабораторной работы №1')
        self.btn_lab2.setToolTip('Выберите каталог для итогового файла\nс ИД для лабораторной работы №2')
        self.ch_lab1.setToolTip('Создать ИД\nдля лабораторной работы №1')
        self.ch_lab2.setToolTip('Создать ИД\nдля лабораторной работы №2')
        self.nam_stud.setToolTip('Список студентов\nдля которых необходимо сформировать ИД')
        self.btn_stud.setToolTip('Импортировать список студентов из файла')
        self.btn_clear.setToolTip('Очистить окно со списком студентов')
        self.btn_create.setToolTip('Сформировать ИД\nдля выбранных лабораторных работ')
        self.pb_create.setToolTip('Шкала прогресса формирования ИФ')
    
    # действие по нажатию на кнопку 'X'
    def closeEvent(self, event):
        #получаем список группы
        list_student = self.nam_stud.toPlainText()
        list_student = module.del_space(list_student)       #удаляем лишние пробелы
        #проверка на пустоту
        if list_student != '':
            #Сохранить список группы?
            reply = QMessageBox.question(self, 'Сообщение', "Сохранить список группы?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            # если нажато "Да", сохраняем файл
            if reply == QMessageBox.Yes:
                self.save_list_student(list_student)
            # если "Нет", удаляем файл   
            else:
                module.delite_student_list()
        event.accept()                          #закрываем программу

    #активация галочек для лабы 1 и 2
    def sector_lab1(self, state):
        #если chekbox устанавили
        if state == Qt.Checked:
            self.le_lab1.setEnabled(True)
            self.btn_lab1.setEnabled(True)
            self.lab1 = True
        else:
            self.le_lab1.setEnabled(False)
            self.btn_lab1.setEnabled(False)
            self.lab1 = False
            
    def sector_lab2(self, state):
        #если chekbox устанавили
        if state == Qt.Checked:
            self.le_lab2.setEnabled(True)
            self.btn_lab2.setEnabled(True)
            self.lab2 = True
        else:
            self.le_lab2.setEnabled(False)
            self.btn_lab2.setEnabled(False)
            self.lab2 = False
    
    #выбор директории для лабы 1 и 2
    def getdir_lab1(self):
        dir_path1 = self.le_lab1.text()  #os.getcwd()
        dir_path2 = self.le_lab2.text()
        name_lab1 = os.path.basename(dir_path1)
        name_lab2 = os.path.basename(dir_path2)
        dir_lab1 = QFileDialog.getExistingDirectory(self, 'Выберать путь для файла лабораторной работы №1', dir_path1)
        #записываем путь директории с именем файла
        self.le_lab1.setText(dir_lab1 + '/' + name_lab1)
        if self.lab2 == True:
            self.le_lab2.setText(dir_lab1 +'/' + name_lab2)
    
    def getdir_lab2(self):
        dir_path = self.le_lab2.text()  #os.getcwd()
        name_lab = os.path.basename(dir_path)
        dir_lab2 = QFileDialog.getExistingDirectory(self, 'Выберать путь для файла лабораторной работы №2', dir_path)
        #записываем путь директории с именем файла
        self.le_lab2.setText(dir_lab2 +'/' + name_lab)
        
    # выбор файла для импорта списка групп
    def getfile(self):
        dir_path = os.getcwd()
        filter = 'Все (*);;Текстовые файлы (*.txt);;Документ (*.odt *.docx);;Электронная таблица (*.ods *.xls *.xlsx)'
        fname = QFileDialog.getOpenFileName(self, 'Выбрать файл со списком группы', dir_path, filter)
        NameStudent = fname[0]                                      #получили файл со списком студентов
        #читаем файл и записываем результат в наш TexstEdit
        if NameStudent != '':
            try:
                #читаем файл попутно удаляя мусор
                list = work_docx.read_student_list(NameStudent)
                if list == False:
                    QMessageBox.warning(self, 'Предупреждение','Выбранное расширение файла не поддерживается!\nПроверьте список поддерживаемых файлов и повторите попытку')
                elif list == '':
                    QMessageBox.warning(self, 'Предупреждение','Не удалось считать список группы из файла!\nПопробуйте скопировать список группы из файла и вставить в поле')
                else:
                    self.nam_stud.setPlainText(module.del_space(list))
            except Exception as e:
                if str(e) == '0':
                    QMessageBox.warning(self, 'Предупреждение','Ошибка чтения файла!\nВозможно, файл пустой')
                else:
                    QMessageBox.warning(self, 'Предупреждение','Ошибка чтения файла!\n\nException = %s'% e)
    
    #по клику удаляем текст в нашем Edit, если там нет списка        
    def add_student(self):
        if (self.nam_stud.toPlainText() == self.enter_const):
            self.clear_nam_stud()
    
    #очистка списка группы
    def clear_nam_stud(self):
        self.nam_stud.clear()
    
    #сохраняем список из Edit в файл    
    def save_list_student(self, list_student):
        module.write_student_list(list_student, self.enter_const)
    
    #вставляем список в Edit из файла
    def read_list_student(self):
        list_student = module.read_student_list()
        if list_student == 1:
            list_student = self.enter_const
        return list_student
#методы для создания потока формирования ИД и обработки сигналов этого потока
    #Создаем наши ИД для студентов
    def create_docx(self):
        #начальные состояния параметров для потоков
        self.ThreadValue = []
        
        #получаем список группы
        list_student = (self.nam_stud.toPlainText())
        list_student = module.del_space(list_student)               #удаляем лишние пробелы
        #проверка на пустоту
        if list_student == '':
            self.Th_Message('Список студентов пуст')
        else:
            list_student = list_student.split('\n')                 #формируем массив студентов
            
            self.ThreadValue.append(list_student)                 #готовим список группы в Thread
            self.ThreadValue = self.Th_Value(self.ThreadValue)  #готовим путь к файлам для потока ИД
            self.ThreadValue.append(1)                            #номер лабораторной для которой вначале будет создаваться ИД
            #self.ThreadValue_2.append(1)                            #номер лабораторной для которой вначале будет создаваться ИД

            self.setDisabled(True)
            self.pb_create.setValue(0)                                              #начальное состояние прогресса
            #создаем потоки внутри формы
            self.thread_create = sec_stream.ThreadCreateID(self.ThreadValue)           #создаем поток создания ИД
            self.thread_create.messageSignal.connect(self.Th_Message)               #обработка сигнала ошибки
            self.thread_create.progressValue.connect(self.Th_Progress)              #обработка сигнала прогресса
            self.thread_create.finished_create.connect(self.end_create)             #обработка сигнала конца работы потока создания ИД
        
            self.thread_create.start()                                              #запускаем поток с отображение прогресса пересчета

    #заносим в массив для потока пути к файлу в зависимости от выбранных флагов
    def Th_Value(self, ThreadValue):
        if (self.lab1 == False) and (self.lab2 == False):
            self.Th_Message('Ни одна лабораторная работа не выбрана!\nПожалуйста установите соответствующие флаги и повторите попытку')
        else:
            if (self.lab1 == True):
                ThreadValue.append(self.le_lab1.text())
            else:
                ThreadValue.append('none')
            
            if (self.lab2 == True):
                ThreadValue.append(self.le_lab2.text())
            else:
                ThreadValue.append('none')
        
        return ThreadValue
    
    #обработка сигнала из потока с сообщением
    def Th_Message(self, str):
        QMessageBox.warning(self, 'Предупреждение', str)
    
    #обработка сигнала прогресса создания ИД
    def Th_Progress(self, value):
        if value <= 100:
            self.pb_create.setValue(value)
                
    #оброботка сигнала конца потока 
    def end_create(self):
        if self.ThreadValue[3] == 1:          #первая лаба составлена, составляем вторую
            self.ThreadValue[3] = 2           #готовимся к записи второй лабораторной
            #запускаем потоки на запись ИД для второй лабы
            self.thread_create.start()
        else:                                   #обе лабы составлены
            self.pb_create.setValue(0)       #обнуление шкалы, что бы не раздражала
            self.setEnabled(True)               #разблокируем окно
  
#класс для поля со списком студентов, перехыватывающий клик левой кнопки мыши
class TextEdit(QTextEdit):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self,event):
        self.clicked.emit()

#открываем наше окно
def app_main():
#if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    #ex.thread.start()
    ex.show()
    sys.exit(app.exec_())
