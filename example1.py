def matrix_mult(m1, m2):
    if len(m1[0]) != len(m2):
        return None
    result = []
    for i in range(len(m1)):
        result.append([])
        for j in range(len(m2[0])):
            result[i].append(0)
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result