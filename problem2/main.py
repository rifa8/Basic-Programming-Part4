def draw_xyz(N):
    pattern = ''
    for i in range(1, N+1):
        for j in range(1, N+1):
            hasil = (i-1)*N + j
            if hasil % 3 == 0:
                pattern +='X '
            elif hasil % 2 == 0:
                pattern +='Z '
            else:
                pattern +='Y '
        pattern+='\n'
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """
