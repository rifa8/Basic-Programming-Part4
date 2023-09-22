def play_with_asterisk(n):
    pattern =''
    for i in range(n):
        pattern +=' '*(n-i-1)
        for j in range(i + 1):
            pattern +='* '
        pattern+='\n'
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
