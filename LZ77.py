"""
АЛГОРИТМ LZ77
"""


def show_buffer(buffer):
    half = len(buffer)//2 if len(buffer)%2 == 0 else len(buffer)//2 + 1
    buff = 'БУФЕР ЛЕМПЕЛЯ\n-------------\n'
    for i in range(half):
        if i+half != len(buffer):
            buff += '\'{}\' - {} \t\'{}\' - {}\n'.format(buffer[i][0], buffer[i][1],
                                                          buffer[i+half][0], buffer[i+half][1])
        else:
            buff += '\'{}\' - {}\n'.format(buffer[i][0], buffer[i][1])
    return buff


def lz77(input_data, window):
    # додавання початкових даних до буфера Лемпеля (рядок + індекс)
    buffer = [[], []]
    index = 0
    while index < len(input_data) - window + 1:
        # якщо таки рядок є в буфері, робиться зсув на розмір плинного вікна, додається індекс попереднього входження
        if input_data[index:index + window] in buffer[0]:
            buffer[0].append(input_data[index:index + window])
            buffer[1].append(buffer[1][buffer[0].index(input_data[index:index + window])])
            index += 4
        # інакше додається поточний індекс і робиться зсув на 1
        else:
            buffer[0].append(input_data[index:index + window])
            buffer[1].append(index)
            index += 1
    # фоормування буфера
    return [(buffer[0][idx], (buffer[1][idx], window)) for idx in range(len(buffer[0]))]


if __name__ == '__main__':
    input_data = input('Введіть дані, які треба стиснути: ')
    floating_window = int(input('Введіть значення плинного вікна: '))
    buffer = lz77(input_data, floating_window)
    print(show_buffer(buffer))
