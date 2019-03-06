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

print(update_dict)
#print(f.read())
print(type(f))