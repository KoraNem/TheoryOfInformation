"""
АЛГОРИТМ КОДУВАННЯ ГАФФМАНА
"""


from TheoryOfInformation.Efficiency import efficiency_rate


def min_sum(sums):
    """
    :param sums: список, що містить числа, з яких треба знайти пару з найменшою сумою
    :return: індекси елементів, сума яких є найменшою
    ПРИЗНАЧЕННЯ: використовується для знаходження мінімальної суми для побудови бінарного дерева в кодуванні Гафмана
    АЛГОРИТМ: почергово знаходяться 2 найменші елементи
    """
    sums.reverse() # віддзеркалення списку, щоб найменші елементи опинилися попереду
    mn1 = min(sums)
    i1 = sums.index(mn1)
    i2 = i1 + 1 if i1 != len(sums) - 1 else i1 - 1
    mn2 = sums[i2]
    for i in range(len(sums)):
        if i != i1 and mn1 <= sums[i] < mn2:
            mn2, i2 = sums[i], i
    return len(sums)-i1-1, len(sums)-i2-1


def reverse_code(code):
    code[2] = code[2][::-1]
    return code


def encode_symbols():
    global symbols_info # список сталого розміру з усіма необхідними даними про символи
    # список сум (вузлів, коренів дерева) разом з індексами початкового списку, які належать нащадкам цих вузлів
    info = [[freq[1], [index]] for index, freq in enumerate(symbols_info)]
    # операції над списком виконуються поки в ньому не залишиться 1 елемент
    while len(info) > 1:
        # якщо 2+ елементи - пошук індексів елементів з найменшою сумою, якщо 2 - беруться обидва елементи
        if len(info) > 2:
            i1, i2 = min_sum([sym[0] for sym in info])
        else:
            i1, i2 = 0, 1
        # додавання відповідних цифр до кодів символів, які є нащадками
        for i in info[i1][1]:
            symbols_info[i][2] += '1'
        for i in info[i2][1]:
            symbols_info[i][2] += '0'
        # злиття списків частот та індексів (новий список займає місце 1го)
        info[i1][0] += info[i2][0]
        info[i1][1] += info[i2][1]
        info.pop(i2) # видалення 2го списку
    # віддзеркалення кодів у готовому списку
    symbols_info = list(map(reverse_code, symbols_info))


def create_dictionary():
    global symbols_info
    return {sym[0]: sym[2] for sym in symbols_info}


def encode_data(data_to_encode, dictionary):
    """Повертає список закодованих символів"""
    return [dictionary[sym] for sym in data_to_encode]


def show_encoding_table():
    global symbols_info
    table = '''     ТАБЛИЦЯ КОДУВАННЯ СИМВОЛІВ     
------------------------------------
 Символ | Частота появи | Кодування 
------------------------------------
'''
    for sym_set in symbols_info:
        table += sym_set[0].center(8) + '|' + str(sym_set[1]).center(15) + '|' \
                 + sym_set[2].ljust(len(symbols_info[-1][2])).center(11) + '\n'
    table += '------------------------------------'
    return table


def huffman_coding(input_data):
    """Виконання розрахунків та повернення зашифрованого рядка (список) зі словником"""
    global symbols_info  # список, що містить дані про кожен символ (0 - символ, 1 - частота появи, 2 - /код/)
    symbols_info = [[i, input_data.count(str(i)), ''] for i in list(set(input_data))]
    symbols_info.sort(key=lambda sym_set: sym_set[1], reverse=True)
    # кодування символів
    encode_symbols()
    # результати
    dictionary = create_dictionary()
    return encode_data(input_data, dictionary),\
           dictionary,\
           show_encoding_table(), \
           efficiency_rate([sym_set[1] for sym_set in symbols_info], [len(sym_set[2]) for sym_set in symbols_info])


def huffman_encrypted_table(input_data):
    enc_list, dictionary, table, efficiency = huffman_coding(input_data)
    return enc_list, table


def huff_all(input_data):
    """Виводиться сформована інформація про результати кодування"""
    enc_list, dictionary, table, efficiency = huffman_coding(input_data)
    print('\nРЕЗУЛЬТАТ: {}\n'.format(''.join(enc_list)))
    print(table)
    print('\nЕФЕКТИВНІСТЬ КОДУВАННЯ')
    print(efficiency)
    return enc_list


def decode(input, dictionary):
    dict = [[], []]
    for word in dictionary:
        dict[1].append(word)
        dict[0].append(dictionary[word])
    output = ''
    start_index = 0
    end_index = 0
    while end_index < len(input):
        if input[start_index:end_index+1] in dict[0] and end_index < len(input):
            output += dict[1][dict[0].index(input[start_index:end_index+1])]
            start_index = end_index+1
            end_index = start_index
        else:
            end_index += 1
    return output


if __name__ == '__main__':
    # дані для кодування
    input_data = input('Введіть дані, які треба закодувати: ')
    huff_all(input_data)
