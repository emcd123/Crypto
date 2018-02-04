from cs402 import AffineCipher
from cs402 import isEnglish

C = AffineCipher
C.setAlphabet("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;: \n")

def one_block(C):
  for a in range(0,68):
    for b in range(0,68):
      C.setDecipherKey([a,b]) 
      txt = C.decipher("cipher_short.txt")
      if isEnglish(txt):
        print(txt)
        print([a,b])
        return [a,b]


def two_block(C):
  pass
two_block(C)

def invert_key(C):
  key = one_block(C)
  for a_inverse in range(0,68):
    if(((key[0] * a_inverse) % 68) == 1):
      return a_inverse
#  for b_inverse in range(0,68):
#    if(((key[1] * b_inverse) % 68) == 1):
#      inverse_key.append( b_inverse)

def encipher_one_block(C):
  inverse = [invert_key(C),9]
  print(inverse)
  C.setEncipherKey(inverse)
  enc = C.encipher("question2.txt")
  enc_file = open("enc_q2.txt", "w+")
  enc_file.write(enc)
  print(enc)
encipher_one_block(C)

def one_block_redecipher(C):
  C.setDecipherKey([53,67])
  print(C.decipher("enc_q2.txt"))

one_block_redecipher(C)
