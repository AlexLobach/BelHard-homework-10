


fruits = [
    'orange \n',
    'apple \n',
    'kiwi \n'   
]

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
    

