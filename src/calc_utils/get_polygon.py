from math import cos, sin, pi, sqrt

def get_hex(r):
    verts = []
    for i in range(6):
        a = r * cos(2 * pi * i / 6 + pi/2)
        b = r * sin(2 * pi * i / 6 + pi/2)
        verts.append((a,b))

    return verts, sqrt(3)/2*r

if __name__ == '__main__':
    print(get_hex(1,0,0))
