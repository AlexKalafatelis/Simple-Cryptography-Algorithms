% CAESAR  Caesar's cipher encryption algorithm

function coded = caesar3(plaintext,key)
n=key - 95 * fix(key/95);
v=double(plaintext)+n;
v(v<65)=90-(64-v(v<65));
v(v>90)=65+(-91+v(v>90));
coded=char(v);
end