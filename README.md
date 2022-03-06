# Simple Cryptography Algorithms

Analysis of basic cryptographic algoritms for a university course. 
The code is written mainly in MATLAB and in python.

## A. Ceasar's Cipher 

The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials. 

Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter of the text has been moved down. 
The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as. 

E_n(x)=(x+n)mod\ 26   
(Encryption Phase with shift n)

D_n(x)=(x-n)mod\ 26   
(Decryption Phase with shift n)

![image](https://user-images.githubusercontent.com/47864776/150894642-fc447eba-024b-424c-961f-85514cd00931.png)

https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/


## B. Playfair Cipher

The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet.

It was used for tactical purposes by British forces in the Second Boer War and in World War I and for the same purpose by the Australians during World War II. This was because Playfair is reasonably fast to use and requires no special equipment.

https://www.geeksforgeeks.org/playfair-cipher-with-examples/

Specifically, the Playfair cipher uses a 5x5 table containing a key word or phrase. 

To generate the key table, one would first fill in the spaces in the table with the letters of the keyword, then fill the remaining spaces with the rest of the letters of the alphabet in order. The keyword together with the conventions for filling in the 5 by 5 table constitute the cipher key.

Then, to encrypt a message, one would break the message into digrams (groups of 2 letters). These digrams will be substituted using the key table. Since encryption requires pairs of letters, messages with an odd number of characters usually append an uncommon letter, such as "X", to complete the final digram. To perform the substitution, the following 4 rules need to be applied in order this specific order, to each pair of letters in the plaintext:

A. If both letters are the same (or only one letter is left), add an "X" after the first letter. Encrypt the new pair and continue. Some variants of Playfair use "Q" instead of "X", but any letter, itself uncommon as a repeated pair, will do.

B. If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively (wrapping around to the left side of the row if a letter in the original pair was on the right side of the row).

C. If the letters appear on the same column of your table, replace them with the letters immediately below respectively (wrapping around to the top side of the column if a letter in the original pair was on the bottom side of the column).

D. If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.

Additionally, in order to decrypt the plaintext, the inverse of the last 3 rules is conducted, while the 1st rule is left as-is.

For additional info, please read this: https://en.wikipedia.org/wiki/Playfair_cipher
