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


block_id = 0
def split_lines(block_id):
    """
    Leitura linha-a-linha.
    """
    line_dict = {}
    line_list = []
    with open('C:\\Users\sword art\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt', 'r') as text_file:
        for line in text_file:
            split_line = line.split()

            regex_exec = re.search(r'\d{2}\:\d{2}\:\d{2}\s{2}(.*)\s{1}\-', line)
            print(f'tipo_comando regex: {regex_exec.group(1)}')
            line_dict['type_line'] = define_type(regex_exec.group(1))

            regex_exec = re.search(r'(.*)\s{2}\d{2}\:', line)
            print(f'linha regex: {regex_exec.group(1)}')
            linha = regex_exec.group(1)
            line_dict['linha'] = linha
            
            regex_exec = re.search(r'(\d{2}\:\d{2}\:\d{2})', line)
            print(f'hora regex: {regex_exec.group(1)}')
            hora = regex_exec.group(1)
            line_dict['hora'] = hora

            regex_exec = re.search(r'\s{1}-\s{1}(.*)', line)
            print(f'comando regex: {regex_exec.group(1)}')
            comando = regex_exec.group(1)
            line_dict['command'] = comando

            #regex_exec = re.search(r'(\d*)\s{2}\d{2}\:\d{2}\:\d{2}', line)
            regex_exec = re.search(r'(.*)\s{2}(\d{2}\:\d{2}\:\d{2})\s{2}(.*)\s{1}\-{1}\s{1}(.*)', line)
            regex_full_linha = regex_exec.group(1)
            regex_full_hora = regex_exec.group(2)
            regex_full_tipo = regex_exec.group(3)
            regex_full_comando = regex_exec.group(4)
            print('*'*20)
            print(f'Regex FULL\nLinha: {regex_full_linha} | Hora: {regex_full_hora} | Tipo: {regex_full_tipo} | Comando: {regex_full_comando}\n' + '*' * 20)
            
            print(block_id)
            line_dict['block'] = block_id
            block_id += 1
            
            line_list.append(line_dict.copy())
            line_dict.clear()

            print('\n'+'='*20+'\n'+'='*20+'\n')

    return line_list


file_readed = split_lines(block_id)

for line in file_readed:
    print(line)