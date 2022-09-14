#Задание 1
#p Показать владельца документа
def f_people (doc,n_document):
    name_='Вы ввели неправильный номер документа!'
    for dict_doc in doc:  
      str_=dict_doc.get("number")
      if n_document == str_:
        name_ = dict_doc.get("name")
    return  (name_)
#s - Показать полку на которой находится документ
def f_shelf(dir,n_document):
    name_shelf='Вы ввели неправильный номер документа!'
    for key_,list_doc in dir.items():  
      for n_doc in list_doc:
        if n_doc == n_document:
          name_shelf = key_+' полка'
    return  (name_shelf)
#l - Показать все документы
def f_list(doc):
    for dict_doc in doc:  
      str_=''
      str_=dict_doc.get("type")+' "'+dict_doc.get("number")+'" "'+ dict_doc.get("name")+'"'
      print (str_)
    return True
#ls- Показать расположение документов по полкам
def f_list_shelf(dir):
    for key_,val_ in dir.items():
      print (f'На полке {key_} документы: {val_}')
    return True
#a - Добавить документ, а также добавить его на полку
def f_add (doc, dir,type_new_,number_new_,name_new_,shelf_number_new_):
  dict_new={}      
  dict_new={"type":type_new_,"number":number_new_,"name":name_new_}
  if shelf_number_new_ not in dir.keys():
    print (f'Введен неправильный номер полки: {shelf_number_new_}')
    return False
  doc.append(dict_new)
  for key_,list_doc in dir.items():  
    if shelf_number_new_ == key_:
          list_doc.append (number_new_)       
  print (f'Документ {number_new_} успешно добавлен на полку {shelf_number_new_}')
  return True

if __name__ == '__main__':
    document = [
             {"type":"passport","number":"2207 876234",
             "name": "Василий Гуркин"},
             {"type":"invoice","number":"11-2",
             "name":"Геннадий Покемонов"},
             {"type": "insurance", "number": "10006",
             "name": "Аристарх Павлов"}
    ]
    directories = {
        '1': ['2207 876234','11-2','5455 028765'],
        '2': ['10006'],
        '3': []
    }
    print("""Набор команд:
     p - Показать владельца документа
     s - Показать полку на которой находится документ
     l - Показать все документы
     ls- Показать расположение документов по полкам
     a - Добавить документ, а также добавить его на полку
     q - Выйти из программы""")
    while True:
      command = input ('Введите команду (p,s,l,ls,a,q): ')
      if command == 'p' or command == 's':
          n_document = input ('Введите номер документа: ') 
      if command ==  'p':
          print(f_people (document,n_document))
      elif command ==  's':
          print (f_shelf(directories,n_document))
      elif command ==  'l':
          print (f_list(document))
      elif command ==  'ls':
          print (f_list_shelf(directories))
      elif command ==  'a':
          type_new = input ('Введите тип документа документа нового элемента: ')  
          number_new = input ('Введите номер документа нового элемента: ')
          name_new = input ('Введите имя и фамилию владельца нового элемента: ')
          shelf_number_new = input ('Введите номер полки для нового элемента: ')
          print (f_add(document,directories,type_new,number_new,name_new,shelf_number_new))
      elif command ==  'q':
          break
     
     