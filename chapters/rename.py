import os

abc = "abcdefghiklmnopqrstuvwxyz"

for i in range(1, 13):
    os.rename(f'{abc[i]}.rst', f'{abc[i-1]}-{i}.rst')
