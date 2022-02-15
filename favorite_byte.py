from pwn import *
# a = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
for i in range(256):
    potential_flag = str(xor(bytes.fromhex(data), i))
    if potential_flag[2] == 'c':
        print(potential_flag)
