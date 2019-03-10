block_id = 0
def split_lines(block_id):
    line_dict = {}
    line_list = []
    with open('C:\\Users\\sword art\\Documents\\dev\\sqlmon-converter\\sqlmonexemplo.txt', 'r') as text_file:
        for line in text_file:
            split_line = line.split()
            if 'PREPARE' in split_line:
                vline_type = 'PREPARE'
            elif 'UPDATE' in split_line:
                vline_type = 'UPDATE'
            elif 'INSERT' in split_line:
                vline_type = 'INSERT'
            elif 'DELETE' in split_line:
                vline_type = 'DELETE'
            elif 'SELECT' in split_line:
                vline_type = 'SELECT'
            elif 'DATA IN' in line:
                vline_type = 'DATA IN'
            elif 'DATA OUT' in line:
                vline_type = 'DATA OUT'
            elif 'EXECUTE' in line:
                vline_type = 'EXECUTE'
            else:
                vline_type = 'ETC'
            line_dict['block_id'] = block_id
            print('linha: ')
            print(line[:1])
            print('\n=======================')
            line_dict['line_number'] = line[:1]
            print('line_hour:')
            print(line[8:16])
            print('\n=======================')
            line_dict['line_hour'] = line[8:16]
            print('line_type:')
            print(vline_type)
            print('\n=======================')
            line_dict['line_type'] = vline_type
            print('line_command:')
            print(split_line[28:])
            print(line[28:])
            print('\n=======================')
            line_dict['line_command'] = line[28:]
            block_id += 1
            line_list.append(line_dict.copy())
            line_dict.clear()

    return line_list


file_readed = split_lines(block_id)

for line in file_readed:
    print(line)