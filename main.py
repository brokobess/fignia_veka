def change_symbol(char, right):
    first, last, size = ['а', 'А', 'a', 'A', '0'], \
                        ['я', 'Я', 'z', 'Z', '9'], \
                        [33, 33, 26, 26, 10]
    special_symbol = True
    for i in range(len(first)):
        if first[i] <= char <= last[i]:
            special_symbol = False
            if right % size[i] == 0:
                return char
            if ord(char) + right > ord(last[i]):
                return chr(ord(first[i]) + ord(char) + right % size[i] - ord(last[i]) - 1)
    if special_symbol:
        return char
    return chr(ord(char) + right)
def encryption_shift(string, right):
    result = ''
    for char in string:
        result += change_symbol(char, right)
    return result
def decryption_shift(string):
    print('Возможные варианты расшиврования строки: ', string )
    variants = [string]
    answer = ''
    shift = 1
    while answer != variants[0]:
        answer = encryption_shift(string, shift)
        if answer != variants[0]:
            variants.append(answer)
        shift += 1
    for i in range(len(variants)):
        print(i + 1, variants[i])
string = input()
A = int(input())
string = encryption_shift(string, A)
decryption_shift(string)
print(string)