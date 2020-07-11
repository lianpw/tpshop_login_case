
def read_txt(filename):
    filepath = '../data/' + filename
    with open(filepath, 'r', encoding='utf-8') as f:
         return f.readlines()


if __name__ == '__main__':
    datas = read_txt('login.txt')
    arrs = []
    for data in datas:
        arrs.append(tuple(data.strip().split(',')))
    print(arrs)