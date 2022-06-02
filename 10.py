from ctypes import Union
import json
import pathlib
import pickle
import json
import yaml
from pydantic import BaseModel




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
file_pickle = pathlib.Path('for_pickle.txt')
with file_pickle.open('wb') as fp:
    pickle.dump(cars, fp)

with file_pickle.open('rb') as fp:
    loaded_data = pickle.load(fp)
    print (loaded_data ['sedan'])

#3 JSON и YAML
#3.1 JSON "dumps"

i_am = {
    "firstName": 'Alexander',
    "lastName": 'Shotc',
    "Age": 27,
    "hobbies": ["programming", "crossfit", "travaling"]
}
my_wife = {
    "firstName": 'Darya',
    "lastName": 'Shmakova',
    "Age": 26,
    "hobbies": ["reading", "music", "travaling"]
}

a = json.dumps(i_am, indent= 4, sort_keys= True)
c = json.loads (a)
print (c)

#3.2 YAML "dump"
file_yaml = pathlib.Path('Ytest.yaml')
with file_yaml.open('w') as fy:
    yaml.dump (my_wife, fy)

with file_yaml.open('r') as fpy:
    print (fpy.read ())
    #print (yaml.load ())



#4 PYDANTIC
data = {
    "age" : 45,
    "name" : "Peter",
    "children" : [
        {
            "age_c" : 3,
            "name_c": "Alice"
        }
    ],
    "married" : True,
    "city" : "Minsk"
}

class Family(BaseModel):
    age : int
    name : str
    children : list = None
    married : bool
    city : str = None

f = Family (**data)

print (f)
