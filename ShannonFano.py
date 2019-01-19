"""
АЛГОРИТМ КОДУВАННЯ ШЕННОНА-ФОНО
"""

from TheoryOfInformation.Efficiency import efficiency_rate


def encode_symbols(frequencies, start, end):
    """
    Розділення впорядкованого списку частот на групи з приблизно рівними сумами, додавання 0/1 до кодів
    Symbols data: [[символ],[частота появи],[код]]
    """
    global symbols_info
    if len(frequencies) > 1:
        # останнього елемента найбільшого пошук елемента, при якому суми частот будуть приблизно рівними
        end_index = 0
        freq_sum = 0
        # знайдена сума: перевищує або дорівнює половині
        while freq_sum < sum(frequencies) // 2:
            freq_sum += frequencies[end_index]
            end_index += 1

        # знаходимо оптимальнішу суму
        diff1 = abs(sum(frequencies[:end_index])-sum(frequencies[end_index:]))
        diff2 = abs(sum(frequencies[:end_index-1]) - sum(frequencies[end_index-1:]))
        if diff2 < diff1:
            end_index -= 1

        # додавання "0" до коду всіх символів, що належать 1й групі
        for i in range(start, start + end_index):
            symbols_info[i][2] += '0'
        # додавання "1" до коду всіх символів, що належать 2й групі
        for i in range(start + end_index, end):
            symbols_info[i][2] += '1'
        # прохід по групах
        encode_symbols(frequencies[:end_index], start, start + end_index)
        encode_symbols(frequencies[end_index:], start + end_index, end)


def create_dictionary():
    global symbols_info
    return {sym[0]: sym[2] for sym in symbols_info}


def encode_data(data_to_encode, dictionary):
    """Повертає список закодованих символів"""
    return [dictionary[sym] for sym in data_to_encode]


def show_encoding_table():
    global symbols_info
    table = '''
     ТАБЛИЦЯ КОДУВАННЯ СИМВОЛІВ     
------------------------------------
 Символ | Частота появи | Кодування 
------------------------------------
'''
    for sym_set in symbols_info:
        table += sym_set[0].center(8) + '|' + str(sym_set[1]).center(15) + '|' \
                 + sym_set[2].ljust(len(symbols_info[-1][2])).center(11) + '\n'
    table += '------------------------------------\n'
    return table


def shannon_fano_coding(input_data):
    """Виконання розрахунків та повернення зашифрованого рядка (список) зі словником"""
    global symbols_info  # список, що містить дані про кожен символ (0 - символ, 1 - частота появи, 2 - /код/)
    symbols_info = [[i, input_data.count(str(i)), ''] for i in list(set(input_data))]
    symbols_info.sort(key=lambda sym_set: sym_set[1], reverse=True)
    # кодування символів
    encode_symbols([data[1] for data in symbols_info], 0, len(symbols_info))
    # результати
    dictionary = create_dictionary()
    return encode_data(input_data, dictionary),\
           dictionary,\
           show_encoding_table(),\
           efficiency_rate([sym_set[1] for sym_set in symbols_info],
                           [len(sym_set[2]) for sym_set in symbols_info])


def s_f_all(input_data):
    """Виводиться сформована інформація про результати кодування"""
    enc_list, dictionary, table, efficiency = shannon_fano_coding(input_data)
    print('\nРЕЗУЛЬТАТ: {}'.format(''.join(enc_list)))
    print(table)
    print('ЕФЕКТИВНІСТЬ КОДУВАННЯ')
    print(efficiency)
    return enc_list



if __name__ == '__main__':
    # дані для кодування
    input_data = input('Введіть дані, які треба закодувати: ')
    s_f_all(input_data)
    inp, dict = shannon_fano_coding(input_data)[:2]
    print(decode(''.join(inp), dict))
