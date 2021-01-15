def my_encoder(en_string: str):
    cipher = bytes(' '.join(format(ord(i), 'b') for i in en_string), 'ascii')
    return cipher

def my_decoder(de_bytes: bytes):
    decoded = ''.join([chr(int(i, 2)) for i in de_bytes.split()])
    return decoded

main_txt = input('enter: ')

temp = my_encoder(main_txt)

print(temp.decode('ascii'))

print(my_decoder(temp))
