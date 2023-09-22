def ubah_huruf(sentence):
    pattern = ''
    for i in range(len(sentence)):
        karakter = sentence[i]
        if karakter==' ':
            pattern +=' '
        elif karakter.isupper:
            pattern +=chr((ord(karakter) + 10 - 65) % 26 + 65)
        elif karakter.islower():
            karakter += chr((ord(karakter) + 10 - 97) % 26 + 97)
        else:
            pattern +=karakter
    return pattern

if __name__ == '__main__':
    print(ubah_huruf("SEPULSA OKE")) # COZEVCK YUO
    print(ubah_huruf("ALTERRA ACADEMY")) # KVDOBBK KMKNOWI
    print(ubah_huruf("INDONESIA")) # SXNYXOCSK
    print(ubah_huruf("GOLANG")) # QYVKXQ
    print(ubah_huruf("PROGRAMMER")) # ZBYQBKWWOB
