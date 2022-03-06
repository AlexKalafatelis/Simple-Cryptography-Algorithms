clc, clear

[e_val, n_val, d_val] = generateKey();

message_value = input('Please insert a small secret number/message: ');

encrypted_value = encrypt(message_value, e_val, n_val);

disp('Encrypted message:')
disp(encrypted_value)

pause(2)

disp('The algorithm will now decrypt the messageS!')
decrypt_value = decrypt(encrypted_value, d_val, n_val);
disp('The result is:')
disp(decrypt_value)