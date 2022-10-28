def transpose(matrix):
    size = len(matrix)
    trans_matrix = create_null_matrix(size)
    for i in range(size):
        for j in range(size):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def create_null_matrix(size):
    matrix = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        matrix.append(line)
    return matrix


def debug(matrix, title='DEBUG'):
    print('-' * 10, title, '-' * 10)
    for i in range(len(matrix)):
        print(*matrix[i], sep='\t')
    print('-' * (len(title) + 22))


def merge(matrix):
    size = len(matrix)
    for i in range(size):
        is_changed = False
        for j in range(size - 1):
            if matrix[i][j] == 0:
                continue
            if is_changed:
                is_changed = False
                continue
            if matrix[i][j] == matrix[i][j + 1]:
                matrix[i][j + 1] *= 2
                matrix[i][j] = 0
                is_changed = True
    return matrix


def reverse(matrix):
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
    return matrix


def compress(matrix):
    size = len(matrix)
    for _ in range(size):
        is_changed = False
        for i in range(size):
            for j in range(size - 2, -1, -1):
                if matrix[i][j + 1] != 0:
                    continue
                if matrix[i][j] != 0:
                    matrix[i][j + 1] = matrix[i][j]
                    matrix[i][j] = 0
                    is_changed = True
        if not is_changed:
            break
    return matrix


def right(matrix):
    matrix = full_step(matrix)
    return matrix


def left(matrix):
    matrix = reverse(matrix)
    matrix = full_step(matrix)
    matrix = reverse(matrix)
    return matrix


def up(matrix):
    matrix = transpose(matrix)
    matrix = reverse(matrix)
    matrix = full_step(matrix)
    matrix = reverse(matrix)
    matrix = transpose(matrix)
    return matrix


def down(matrix):
    matrix = transpose(matrix)
    matrix = full_step(matrix)
    matrix = transpose(matrix)
    return matrix


def full_step(matrix):
    matrix = compress(matrix)
    matrix = merge(matrix)
    matrix = compress(matrix)
    return matrix


if __name__ == '__main__':
    m = [[4, 4, 4, 2], [8, 8, 0, 2], [2, 0, 0, 0], [0, 0, 0, 0]]
    debug(m, 'START')
    # debug(compress(merge(compress(m))))
    # debug(compress(merge(compress(reverse(m)))))
    # right(m)
    # left(m)
    # up(m)
    # down(m)
