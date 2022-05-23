import pathlib
import pickle



fruits = [
    'orange \n',
    'apple \n',
    'kiwi \n'   
    ]

cars = {
    'hatchback': ["Kia cee'd","VW golf", "Opel astra" ],
    'sedan' : ["VW jetta", "Toyota camry", "Mazda 6"]
    }

#1 Записать в файл строку, потом её считать
with open('draft.txt', 'w') as file:
    file.writelines (fruits)
    file.write('Hello, everyone \n')
    file.write('Hello, everyone \n')
    file.write('Hello, everyone \n')

with open('draft.txt', 'r') as fileread:
    print (fileread.readline())
    print (fileread.readline())
    print (fileread.readline())
    print (fileread.readline())
    print (fileread.readline())
    print (fileread.readline())




#2 Сериализовать объект простого класса, загрузить его и запустить метод, использующий аттрибут объекта, при помощи pickle
file_picle = pathlib.Path('for_pickle.txt')
with file_picle.open('wb') as fp:
    pickle.dump(cars, fp)

with file_picle.open('rb') as fp:
    loaded_data = pickle.load(fp)
    print (loaded_data ['sedan'])


