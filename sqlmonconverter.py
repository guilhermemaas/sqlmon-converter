"""
https://thispointer.com/python-how-to-remove-characters-from-a-string-by-index/
https://thispointer.com/python-how-to-remove-multiple-elements-from-list/
"""

f = open('C:\\Users\\guilherme.maas\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt', 'r')

dict = {}
update_count = 0
insert_count = 0
select_count = 0
delete_count = 0
palavaras_count = 0

for words in f.read().split():
    print(f'PALAVRA NÚMERO: {palavaras_count}')
    print(words)

    if 'UPDATE' in words:
        update_count +=1
    
    if 'INSERT' in words:
        insert_count += 1

    if 'DELETE' in words:
        delete_count += 1
    
    if 'SELECT' in words:
        select_count += 1

    palavaras_count += 1

print(f'\nForam realizados o total de {update_count} UPDATES neste log.')
print(f'\nForam realizados o total de {delete_count} DELETES neste log.')
print(f'\nForam realizados o total de {insert_count} INSERTS neste log.')
print(f'\nForam realizados o total de {select_count} SELECTS neste log.')

update_dict = {}

with open('C:\\Users\\guilherme.maas\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt', 'r') as f:
    for line in f:
        if 'UPDATE' in line:
            split_line = line.split()
            update_dict[split_line[0]] = split_line[1]
        else:
            pass

update_list = []
update_list2 = []

file_path = 'C:\\Users\\guilherme.maas\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt'

def open_file(file_text):
    file_text = file_text
    f = open(file_text, 'r')

    return f


def split_lines(text_file):
    text_file = text_file
    update_list = []
    delete_list = []
    insert_list = []
    select_list = []
    datain_list = []
    dataout_list = []
    etc_list = []
    for line in text_file:
        if 'UPDATE' in line:
            split_line = line.split()
            update_list.append(split_line)
        elif 'DELETE' in line:
            split_line = line.split()
            delete_list.append(split_line)
        elif 'INSERT' in line:
            split_line = line.split()
            insert_list.append(split_line)
        elif 'SELECT' in line:
            split_line = line.split()
            select_list.append(split_line)
        elif 'DATA IN' in line:
            split_line = line.split()
            datain_list.append(split_line)
        elif 'DATA OUT' in line:
            split_line = line.split()
            dataout_list.append(split_line)
        else:
            split_line = line.split()
            etc_list.append(split_line)

for line in update_list:
    print(f'{line}\n')

print('=' * 50)

for line in update_list2:
    print(f'{line}\n')

print('*' * 50)

print('Removendo...')

print('*' * 50)

print('Print, alterado.')
for line in update_list2:
    line = line [28:]
    print(line)
    print(type(line))

print('*' * 50)

print(update_dict)
print(update_dict['14'])
#print(f.read())
print(type(f))