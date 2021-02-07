try:
    file = open('./numbers.txt', 'r', encoding='UTF-8')
    file_txt = file.read()
    txt_list = file_txt.split('\n')
    for i in txt_list:
        res = i.replace(',', '')
        print(res)

except Exception as e:
    print(e)
    exit()
