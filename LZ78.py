"""
АЛГОРИТМ LZ77
"""

from TheoryOfInformation.Huffman import huffman_encrypted_table


def show_buffer(buffer):
    half = len(buffer)//2 if len(buffer)%2 == 0 else len(buffer)//2 + 1
    buff = 'БУФЕР ЛЕМПЕЛЯ\n-------------\n'
    for i in range(half):
        if i+half != len(buffer):
            buff += '{}|\'{}\' \t{}|\'{}\'\n'.format(buffer[i][0], buffer[i][1],
                                                          buffer[i+half][0], buffer[i+half][1])
        else:
            buff += '\'{}\' - {}\n'.format(buffer[i][0], buffer[i][1])
    return buff


def insert_numbers_encodings(plain_code, numbers):
    # додавання чисел у двійковому форматі перед кожним закодованим символом
    max_bin_len = len(bin(max(numbers))[2:]) # довжина найбільшого числа у двійковому вигляді
    str_nums = list(map(lambda num: '0'*(max_bin_len-len(bin(num)[2:]))+bin(num)[2:], numbers))
    if len(str_nums) > len(plain_code): # у випадку, якщо останній елемент із символів - None, додається порожній рядок
        plain_code.append('')
    return ''.join([''.join([str_nums[i], plain_code[i]]) for i in range(len(numbers))])


def lz78(input_data):
    # додавання початкових даних до буфера Лемпеля (рядок + індекс)
    buffer = [[], [], []]  # [string], [number/index], [+value]
    index = 0
    while index < len(input_data):
        window = 1 # розмір плинного вікна
        num_of_string = 0 # число, що вказує або на те, що символа нема в буфері, або номер рядка, в якому він був
        while input_data[index:index + window] in buffer[0] and index + window <= len(input_data):
            num_of_string = buffer[0].index(input_data[index:index + window]) + 1
            window += 1
        buffer[2].append( # символ, який додається
            None if input_data[index:index + window] in buffer[0] else input_data[index:index + window][-1])
        buffer[0].append(input_data[index:index + window]) # рядок
        buffer[1].append(num_of_string) # порядквий номер рядка
        index += window # збільшення значення поточного індексу на розмір вікна (довжина рядка, що додався до буфера)
    encoded_without_nums, code_tbl = huffman_encrypted_table(buffer[2][:-1] if buffer[2][-1] is None else buffer[2])
    buff = show_buffer([(buffer[1][i], buffer[2][i]) for i in range(len(buffer[0]))])
    return insert_numbers_encodings(encoded_without_nums, buffer[1]), buff, code_tbl


if __name__ == '__main__':
    # input_data = input('Введіть дані, які треба стиснути: ')
    encoded, buffer, tbl = lz78('водовіз віз воду з водопроводу')
    print(buffer)
    print(tbl)
    print(encoded)
