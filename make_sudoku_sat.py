# N (size of board)
# B (size of each block)
# 2 1 - 4 - - - 3 6
# 8 - - - - - - - 5
# - - 5 3 - 9 8 - -
# 6 - 4 9 - 7 1 - -
# - - - - 3 - - - -
# - - 7 5 - 4 6 - 2
# - - 6 2 - 3 5 - -
# 5 - - - - - - - 9
# 9 3 - - - 5 - 2 7


def three_blocks_cond():
    for i in range(N):
        if i%3 ==0:
            rlim = i+3
        elif i%3 == 1:
            rlim = i+2
        elif i%3 == 2:
            rlim = i+1

        for j in range(N):
            if j % 3 == 0:
                clim = j + 3
            elif j % 3 == 1:
                clim = j + 2
            elif j % 3 == 2:
                clim = j + 1

            # for same block
            for k in range(rlim-3, rlim):
                for l in range(clim-3, clim):
                    if k < i or (k <= i and l <= j):
                        continue
                    else:
                        for num in range(1, N+1):
                            print('~' + str(i) + '_' + str(j) + '_' + str(num)
                                  + ' ' + '~' + str(k) + '_' + str(l) + '_' + str(num))


def four_blocks_cond():
    for i in range(N):
        if i % 4 == 0:
            rlim = i + 4
        elif i % 4 == 1:
            rlim = i + 3
        elif i % 4 == 2:
            rlim = i + 2
        elif i % 4 == 3:
            rlim = i + 1

        for j in range(N):
            if j % 4 == 0:
                clim = j + 4
            elif j % 4 == 1:
                clim = j + 3
            elif j % 4 == 2:
                clim = j + 2
            elif j % 4 == 3:
                clim = j + 1

            # for same block
            for k in range(rlim-4, rlim):
                for l in range(clim-4, clim):
                    if k < i or (k <= i and l <= j):
                        continue
                    else:
                        for num in range(1, N+1):
                            print('~' + str(i) + '_' + str(j) + '_' + str(num)
                                  + ' ' + '~' + str(k) + '_' + str(l) + '_' + str(num))


if __name__ == '__main__':
    board = []
    N = int(input())
    B = int(input())

    for i in range(N):
        board.append(input().split(' '))
    for i, b in enumerate(board):
        board[i] = [int(elem) if elem != '-' else elem for elem in b]

    # value in [1...N]
    for row in range(N):
        for column in range(N):
            for num in range(1, N+1):
                print(str(row) + '_' + str(column) + '_' + str(num), end=' ')
            print()

            for a in range(1, N+1):
                for b in range(a+1, N+1):
                    print('~' + str(row) + '_' + str(column) + '_' + str(a)
                          + ' ' + '~' + str(row) + '_' + str(column) + '_' + str(b))

    # condition for row, column, block
    for i in range(N):
        for j in range(N):
            # for same row
            for l in range(j+1, N):
                for num in range(1, N+1):
                    print('~' + str(i) + '_' + str(j) + '_' + str(num)
                          + ' ' + '~' + str(i) + '_' + str(l) + '_' + str(num))

    for i in range(N):
        for j in range(N):
            # for same column
            for k in range(i+1, N):
                for num in range(1, N+1):
                    print('~' + str(i) + '_' + str(j) + '_' + str(num)
                          + ' ' + '~' + str(k) + '_' + str(j) + '_' + str(num))

    if B == 3:
        three_blocks_cond()
    elif B == 4:
        four_blocks_cond()

    # hint
    for i in range(N):
        for j in range(N):
            if isinstance(board[i][j], int):
                print(str(i) + '_' + str(j) + '_' + str(board[i][j]))
            else:
                continue
