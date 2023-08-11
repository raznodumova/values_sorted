import os

names = {}
textes1 = []
textes2 = []
textes3 = []

with open('1.txt', 'rt', encoding='utf-8') as file1:
    count = 0
    name1 = os.path.basename(r'C:\Users\фвьшт\Desktop\domashka\1.txt')
    # print(name1)
    for line1 in file1.readlines():
        count += 1
        data1 = count
        sum_line1 = [data1, line1]
        str1 = f'Строка {count} файла {name1}'
        textes1.append(line1)
        names[name1] = textes1

with open('2.txt', 'rt', encoding='utf-8') as file2:
    count = 0
    name2 = os.path.basename(r'C:\Users\фвьшт\Desktop\domashka\2.txt')
    for line2 in file2.readlines():
        count += 1
        data2 = count
        sum_line2 = [data2, line2]
        str2 = f'Строка {count} файла {name2}'
        textes2.append(line2)
        names[name2] = textes2

with open('3.txt', 'rt', encoding='utf-8') as file3:
    name3 = os.path.basename(r'C:\Users\фвьшт\Desktop\domashka\3.txt')
    count = 0
    for line3 in file3.readlines():
        count += 1
        data3 = count
        sum_line3 = [data3, line3]
        str3 = f'Строка {count} файла {name3}'
        textes3.append(line3)
        names[name3] = textes3

sorted_values = dict(sorted(names.items(), key=lambda item: len(item[1])))
print(sorted_values)

with open('result.txt', 'w', encoding = 'utf-8') as file:
    file.write(str(sorted_values.values()))
    # file.write(f'Строка номер {sorted_values.value()} файла {name_value}: ')