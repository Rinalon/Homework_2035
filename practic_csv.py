import csv

column=('id', 'name', 'lastname', 'age', 'height', 'weight')
data=[
    (1, 'Ivan', 'Ivanov', 14, 160, 50),
    (2, 'Sasha', 'Sidorov', 15, 210, 40),
    (3, 'Masha', 'Poradina', 30, 178, 70),
    (4, 'Timur', 'Korolev', 44, 160, 120)
]


def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(column)+'\n')
        for line in data:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')

def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((int(line[0]), line[1], line[2], int(line[3]), int(line[4]), int(line[5])))
    return columns, data

def plus_to_file (filename):
    with open (filename, 'a') as file:
        newline = ()
        newline = input("Введите номер по порядку, имя, фамилию, возраст, рост, вес").split(', ')
        writer = csv.writer(file)
        writer.writerow(newline)

def print_DataFrame (filename):
    u=15
    i=-1
    while i<5:
        i+=1
        print (column[i].ljust(u), end=' ')
    for line in data:
        for j in line:
            print(str(j).ljust(u), end=' ')
        print()


write_to_file ("C:\pop\data.csv")
plus_to_file ("C:\pop\data.csv")
print_DataFrame ("C:\pop\data.csv")
