function[e, n, d] = generateKey()

p = 11;
q = 13;

n = p * q;

phi=(p-1)*(q-1);

for e = 2:phi-1
    if gcd(e,phi)== 1
        %if that's the case, then it's good
        break
    end
end

for d=2:phi-1
    if mod(e*d,phi) == 1
        %if that's the case, then it's good
        break
    end
end