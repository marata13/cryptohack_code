import numpy

a = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]]


def gram_schmidt(v):
    u = []
    for i in range(len(v)):
        temp = v[i]
        for y in u:
            m = numpy.dot(v[i], y) / numpy.dot(y, y)
            temp = numpy.subtract(temp, numpy.multiply(m, y))
        u.append(temp)
    return u


t = gram_schmidt(a)
print(t[3][1])
