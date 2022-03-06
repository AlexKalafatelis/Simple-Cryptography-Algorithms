function answer = powermods(base, exponent, m)


base = mod(base, m);
answer = 1;

for k=1:exponent
    answer = answer * base;
    answer = mod(answer, m);
    
end 