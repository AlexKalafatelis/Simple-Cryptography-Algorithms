% CAESAR  Caesar's cipher encryption algorithm
%
% code = caesar(vector, shift), returns the encypted text of the given
% character vector.


function output = caesar(vector, i)
   % The shift amount is a value between 0 and 94
   for i = 1:25;
   i = i - 95 * fix(i/95);

   % Convert string to double
   code = double(vector);
   secret = code;
   
   % Find the size of the given character vector
   a = size(vector, 2);

   for i = 1:a
       % Check if the new ASCII value is out of limits
       % If ASCII value goes below 32

       if code(i) + i < 32 
           secret(i) = 126 - 31 + code(i) + i;

       % If ASCII value goes beyond 126

       elseif code(i) + i > 126
           secret(i) = 32 + code(i) + i - 127;

       % Normal condition

       else
           secret(i) = code(i) + i;
       end
   end
   
   output = char(secret);

   end
end
