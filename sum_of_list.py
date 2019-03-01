number_list = []

def sum_of_list(list):
    return sum(list)

if __name__ == '__main__':
    while True:
        number = input('輸入清單數字,輸入完請按q離開： ')
        if number == 'q':
            break
        else:
            number_list.append(int(number))
    print(sum_of_list(number_list))