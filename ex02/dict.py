data = [
    ['Caleb', 24],
    ['Calixte', 84],
    ['Calliste', 65],
    ['Calvin', 12],
    ['Cameron', 54],
    ['Camil', 32],
    ['Camille', 5],
    ['Can', 52],
    ['Caner', 56],
    ['Cantin', 4],
    ['Carl', 1],
    ['Carlito', 23],
    ['Carlo', 19],
    ['Carlos', 26],
    ['Carter', 54],
    ['Casey', 2]]

res = [{i[1]:i[0]} for i in data]
for i in res:
    for k, v in i.items():
        print(f'{k:<2} : {v}')
