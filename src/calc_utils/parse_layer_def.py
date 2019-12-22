# layer definition can be written as
# for example: 120120
# or: 20120
# or: 20;6,2;12 (which is translated to 2022222212)
# or: 11;6,r;11 (r stands for random number)
# or: ;15,1; (translates to 111111111111111)
# or: ;6,r;1;5,r; (6 random numbers, 1 and 5 random)

from random import randint


def parse_layer_def(layer_def, random_range=2):
    parsed_layer = []
    subdefs = layer_def.split(';')

    for subdef in subdefs:
        subdef = subdef.strip()
        if ',' in subdef:
            n, l = subdef.split(',')
            subdef = l.strip()*int(n.strip())

        for c in subdef:
            if c == ' ':
                continue
            if c.lower() == 'r':
                r = randint(0,random_range)
            else:
                r = int(c)

            parsed_layer.append(r)

    return parsed_layer


if __name__ == '__main__':
    print(parse_layer_def(input('layer def: ')))
