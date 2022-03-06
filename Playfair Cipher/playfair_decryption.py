"""PlayFair Decryption"""

import string

def key_matrix_generation(key):
  atoz = string.ascii_lowercase.replace('j','.') #replace j->'.'
  key_matrix = ['' for i in range(5)]

  i = 0
  j = 0

  for c in key:
    if c in atoz:
      key_matrix[i] += c
      atoz = atoz.replace(c, '.')
      
      j += 1
      if j>4:
        i += 1
        j = 0

  for c in atoz:
    if c !='.':
      key_matrix[i] +=c

      j += 1
      if j>4:
        i += 1
        j = 0

  return key_matrix

key_matrix = key_matrix_generation('keyword') #key
print(key_matrix)


plaintext = 'thisballisunderthegreentable'
ciphertext = 'vflqcbizflnzugkdvfgndknuvrciwu'
plaintextpairs = []
ciphertextpairs = []

#Rule_1: If a pair is a repeated letter, insert filler like 'x'

i=0
while i < len(ciphertext):
  a = ciphertext[i]
  b = ciphertext[i + 1]
  
  ciphertextpairs.append(a + b)
  i += 2
    
print(ciphertextpairs)


for pair in ciphertextpairs:
  applied_rule = False

#Rule_2: If both letters fall in the same row, replace each with letter to right

  for row in key_matrix:
    if pair[0] in row and pair[1] in row:
      j0 = row.find(pair[0])
      j1 = row.find(pair[1])

      plaintextpair = row[(j0 + 4) %5] + row[(j1 + 4) %5]
      plaintextpairs.append(plaintextpair)
      applied_rule = True
  
  if applied_rule:
    continue

#Rule_3: If both letters fall in the same column, replace each with the letter
#below it (again wrapping to top from bottom)

  for j in range(5):
    col = "".join([key_matrix[i][j] for i in range(5)])
    if pair[0] in col and pair[1] in col:
      i0 = col.find(pair[0])
      i1 = col.find(pair[1])

      plaintextpair = col[(i0 + 4) %5] +col[(i1 +4) %5]
      plaintextpairs.append(plaintextpair)
      applied_rule = True

  if applied_rule:
    continue

#Rule_4: Otherwise each letter is replaced by the letter in the same row and
#in the column of the other letter of the pair

  i0 = 0
  i1 = 0
  j0 = 0
  j1 = 0

  for i in range(5):
    row = key_matrix[i]
    if pair[0] in row:
      i0 = i
      j0 = row.find(pair[0])

    if pair[1] in row:
      i1 = i
      j1 = row.find(pair[1])

  plaintextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
  plaintextpairs.append(plaintextpair)

print(plaintextpairs)

print("ciphertext:" + "".join(ciphertextpairs))
print("plaintext: " + plaintext)
print("plaintextpairs: " + "".join(plaintextpairs))
