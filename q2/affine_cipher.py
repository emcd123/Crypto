from cs402 import AffineCipher
from cs402 import isEnglish

C = AffineCipher
C.setAlphabet("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;: \n")

def one_block(C):
  for a in range(0,68):
    for b in range(0,68):
     C.setDecipherKey([a,b]) 
     txt = C.decipher("cipher_short.txt")
     if isEnglish(txt): print(txt); print([a,b])
  # key = [53,67]
one_block(C)


def two_block(C):
  pass

two_block(C)
