def bin_to_ascii(bin: str):
    final_string = ''
    for word in bin.split(' '):
        if word == '00100000':
            final_string += ' '
        else:
            for translation in open('translations.txt', 'r').read().split('\n'):
                if word in translation:
                    final_string += translation.split(' ')[0]
    return final_string


def ascii_to_bin(ascii: str):
    final_string = ''
    for word in ascii:
        if word == ' ':
            final_string += '00100000' + ' '
        else:
            for translation in open('translations.txt', 'r').read().split('\n'):
                if word in translation:
                    final_string += translation.split(' ')[1] + ' '
    return final_string[:-1]



if __name__ == '__main__':
    print(ascii_to_bin('hello there'))
