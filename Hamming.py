"""
АЛГОРИМТ ГЕМІНГА
"""


from math import log2


def xor(bits):
    """Функції передається список бітів, над якими виконується операція xor"""
    bit = int(bits[0])
    for b in bits[1:]:
        bit ^= int(b)
    return str(bit)


def insert_controls(bit_string):
    length = len(bit_string) # довжина бітового рядка
    bits_list = list(bit_string) # перетворення в рядка в список
    control_bits = 0 # к-ть контрольних бітів
    # визначення к-ті контрольних бітів
    while control_bits < log2(control_bits+length+1):
        control_bits += 1
    # додавання контрольних бітів
    for i in range(control_bits):
        bits_list.insert(2 ** i - 1, None)
    # обрахування контрольних бітів
    for i in range(control_bits):
        bits_to_xor = []  # елементи для xor
        curr_byte = 2 ** i
        counter = 2 ** i - 1
        while curr_byte < len(bits_list):
            if counter > 0:
                bits_to_xor.append(bits_list[curr_byte])
                curr_byte += 1
                counter -= 1
            else:
                curr_byte += 2 ** i
                counter = 2 ** i

        # вставлення контрольного біта на позицію 2**i
        bits_list[2 ** i - 1] = xor(bits_to_xor)
    return ''.join(bits_list)


def mark_controls(bit_string):
    b = list(bit_string)
    i = 0
    for ind in range(len(b)):
        if ind == 2**i-1:
            b[ind] = '{'+b[ind]+'}'
            i += 1
    return ''.join(b)


def hamming_algorithm(bit_string):
    return mark_controls(insert_controls(bit_string))


if __name__ == '__main__':
    #bts = input('Введіть послідовність бітів: ')
    bts = '0010011001101011000101001101110010101101000001001111010111'
    cont = mark_controls(insert_controls(bts))
    print('БІТОВИЙ РЯДОК З КОНТРОЛЬНИМИ БІТАМИ\n'+cont)
