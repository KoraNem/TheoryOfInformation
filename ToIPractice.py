"""
ІНДИВІДУАЛЬНА РОБОТА №1
1. Фраза з 5+ слів
2. код Шеннона-Фоно (+ефективність)
3. код Гафмана (+ефективність)
4. алгоритм Гемінга
5. LZ77
6. LZ78
"""

from TheoryOfInformation.ShannonFano import s_f_all
from TheoryOfInformation.Huffman import huff_all
from TheoryOfInformation.Hamming import hamming_algorithm
from TheoryOfInformation.LZ77 import lz77, show_buffer
from TheoryOfInformation.LZ78 import lz78


# фраза для кодування
#input_data = input('Введіть рядок, що складається з 5 та більше слів: ')
input_data = 'ВОДОВІЗ ВІЗ ВОДУ З ВОДОПРОВОДУ'
#window = int(input('Розмір плинного вікна для алгоритму LZ-77: '))
window = 4

print('\nВВЕДЕНИЙ РЯДОК: {}'.format(input_data))

# кодування алгоритмом Шеннона-Фоно
print('''
================
КОД ШЕННОНА-ФОНО
================''')
encodedSF = ''.join(s_f_all(input_data))

# кодування алгоритмом Гафмана
print('''

===========
КОД ГАФМАНА
===========''')
encodedH = ''.join(huff_all(input_data))

# алгоритм Гемінга
print('''

===========================
ДОДАВАННЯ КОНТРОЛЬНИХ БІТІВ
===========================''')
print("""
Для першого агоритму кодування: {}
Для другого агоритму кодування: {}
""".format(hamming_algorithm(encodedSF), hamming_algorithm(encodedH)), end='\n\n\n')




for i in range(180):
    print('-', end='')
print('\nВВЕДЕНИЙ РЯДОК: {}'.format(input_data))
# lz77
print('''
=====
LZ-77
=====
''')
print(show_buffer(lz77(input_data, window)), end='\n\n\n')

for i in range(180):
    print('-', end='')
print('\nВВЕДЕНИЙ РЯДОК: {}'.format(input_data))
# lz78
print('''
=====
LZ-78
=====
''')
encodedLZ, buff, encoding_table = lz78(input_data)
print('РЕЗУЛЬТАТ: {}\n'.format(encodedLZ))
print(buff)
print('         Кодування Гаффмана')
print(encoding_table)
