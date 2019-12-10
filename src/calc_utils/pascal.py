# module resposible for calculating the pascal triangle scructure

def calc_next_layer(top_layer):
    next_layer = []
    for i in range(len(top_layer)-1):
        a = top_layer[i]
        b = top_layer[i+1]
        next_layer.append(-(a+b)%3)

    return next_layer


def pascal(top_layer):
    layers = [top_layer]
    while len(top_layer) > 1:
        top_layer = calc_next_layer(top_layer)
        layers.append(top_layer)

    return layers


if __name__ == '__main__':
    print(pascal([1,1,2,2]))
