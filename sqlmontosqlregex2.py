import re


def define_type(type_line):
    if type_line == 'PREPARE':
        vline_type = 'PREPARE'
    elif type_line == 'UPDATE':
        vline_type = 'UPDATE'
    elif type_line == 'INSERT':
        vline_type = 'INSERT'
    elif type_line == 'DELETE':
        vline_type = 'DELETE'
    elif type_line == 'SELECT':
        vline_type = 'SELECT'
    elif type_line == 'DATA IN':
        vline_type = 'DATA IN'
    elif type_line == 'DATA OUT':
        vline_type = 'DATA OUT'
    elif type_line == 'EXECUTE':
        vline_type = 'EXECUTE'
    else:
        vline_type = 'ETC'
    return vline_type

def split_lines(block_id, dir):
    line_dict = {}
    line_list = []
    with open(dir, 'r') as text_file:
        for line in text_file:
            regex_exec = re.search(r'(.*)\s{2}(\d{2}\:\d{2}\:\d{2})\s{2}(.*)\s{1}\-{1}\s{1}(.*)', line)
            if 'INSERT' in line or 'UPDATE' in line or 'SELECT' in line \
                or 'DELETE' in line or 'DATA IN' in line or 'DATA OUT' in line or \
                    'PREPARE' in line or 'EXECUTE' in line or 'Error' in line:
                line_dict['type'] = regex_exec.group(3)
            else:
                line_dict['type'] = 'ETC'
            line_dict['line']= regex_exec.group(1)
            line_dict['hour'] = regex_exec.group(2)
            line_dict['command'] = regex_exec.group(4)
            if '?' in line_dict['command']:
                count_letter = 0
                for letter in line_dict['command']:
                    if letter == '?':
                        count_letter += 1
                line_dict['count_param'] = count_letter
            else:
                line_dict['count_param'] = 'NULL'
            if line_dict['type'] == 'DATA IN':
                regex_param = re.search(r'\s\Data\s\=\s(.*)', line_dict['command'])
                line_dict['datain'] = regex_param.group(1)
            else:
                line_dict['datain'] = 'NULL'
            if line_dict['type'] == 'PREPARE':
                block_id += 1
            line_dict['block'] = block_id
            line_list.append(line_dict.copy())
            line_dict.clear()
    return line_list

def block_params(line_list):
    list_param = []
    param_detail = {}
    num_param = 0
    for line in line_list:
        if line['type'] == 'DATA IN':
            regex_type = re.search(r'(Type)\s\=\s(.*)\,\s(Precision)', line['command'])
            num_param += 1
            param_detail['param_num'] = num_param
            param_detail['param_type'] = regex_type.group(2)
            regex_param = re.search(r'\Data\s\=\s(.*)', line['command'])
            param_detail['param_param'] = regex_param.group(1)
            param_detail['param_block'] = line['block']
            list_param.append(param_detail.copy())
        param_detail.clear() 
    return(list_param)
            

block_id = 1
dir = 'C:\\Users\\guilherme.maas\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt'
file_read = split_lines(block_id, dir)
param_list = block_params(file_read)
for linha in file_read:
    print(linha['block'], linha['line'], linha['hour'], linha['type'], linha['command'], linha['count_param'], linha['datain'])

print('=' * 50)
print(param_list)
print(type(param_list))
print('=' * 50)

for param in param_list:
    print(param)
    print('\n')

file = open('filetest.txt', 'w')
for line in file_read:
    file.write(str(line['block']) + '|' + str(line['line']) + '|' + str(line['hour']) + '|' + str(line['command']) + '\n')
