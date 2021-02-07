
def split_elem_line(line):
    tmp_list = line.replace(' ', '').split('=')
    res = {'name': tmp_list[0]}
    elem_list = tmp_list[1].split(',')
    for i in elem_list:
        splitted_elem = i.split(':')
        res[splitted_elem[0]] = splitted_elem[1]
    return res

def create_elem_cell(elem):
    res = ""
    res += f"<td style=\"{style}\">" + '\n'
    res += f"<h4>{elem['name']}</h4>" + '\n'
    res += f"<ul padding-left: 0;>" + '\n'
    res += f"<li>No.{elem['number']}</li>" + '\n'
    res += f"<li>{elem['small']}</li>" + '\n'
    res += f"<li>{elem['molar']}</li>" + '\n'
    res += f"<li>{elem['electron']} electron</li>" + '\n'
    res += f"</ul>" + '\n'
    res += f"</td>" + '\n'
    return res


def create_none_cell():
    res = "<td></td>\n"
    return res

style="border: 1px solid black; min-width: 150px"

try:
    file = open('./periodic_table.txt', 'r', encoding='UTF-8')
    file_txt = file.read()
    txt_list = file_txt.split('\n')
    elements = []
    for i in txt_list:
        elements.append(split_elem_line(i))
    res = ""
    elem_index = 0
    res += "<table>"
    while(elem_index < len(elements)):
        res += "<tr>"
        for i in range(18):
            if(int(elements[elem_index]['position']) == i):
                res += create_elem_cell(elements[elem_index])
                elem_index += 1
            else:
                res += create_none_cell()
        res += "</tr>"
    res += "</table>"
    res_file = open('./periodic_table.html','w')
    res_file.write(res)

except Exception as e:
    print(e)
    exit()
