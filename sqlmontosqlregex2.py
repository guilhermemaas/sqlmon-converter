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


def split_lines(block_id):
    line_dict = {}
    line_list = []
    with open('C:\\Users\\sword art\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt', 'r') as text_file:
        for line in text_file:
            regex_exec = re.search(r'(.*)\s{2}(\d{2}\:\d{2}\:\d{2})\s{2}(.*)\s{1}\-{1}\s{1}(.*)', line)
            if 'INSERT' in line or 'UPDATE' in line or 'SELECT' in line \
                or 'DELETE' in line or 'DATA IN' in line or 'DATA OUT' in line or \
                    'PREPARE' in line or 'EXECUTE' in line:
                line_dict['type'] = regex_exec.group(3)
            else:
                line_dict['type'] = 'ETC'
            line_dict['line']= regex_exec.group(1)
            line_dict['hour'] = regex_exec.group(2)
            line_dict['command'] = regex_exec.group(4)
            if '?' in line_dict['command'] and line_dict['type'] in ('INSERT' or 'UPDATE' or 'DELETE'):
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

block_id = 1
file_readed = split_lines(block_id)

for linha in file_readed:
    print(linha['block'], linha['line'], linha['hour'], linha['type'], linha['command'], linha['count_param'], linha['datain'])