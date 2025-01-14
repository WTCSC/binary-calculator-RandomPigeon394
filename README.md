[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17648227)
# Binary Calculator

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file.
- The solution must be implemented as a function called `binary_calculator()` with three parameters:
    - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
    - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
    - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
- Do not use Python's built-in `bin()` function.
- Implement your own binary-to-decimal and decimal-to-binary conversion logic.
- All binary inputs and outputs should be strings.
- Handle division by zero by returning `"NaN"`
- Handle decimal numbers by rounding down to the nearest whole number (flooring).
- Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`)
- Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits).
- Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` .

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

 -->

 This is a binary calculator and is coded to do addition, subtraction, multiplacation and division. 
 The calculator works by when you import a string of 8 digits of 0 and 1s like 01010101 it puts it in numbers like 1st digit is 128 2nd 64 third 32 fourth 16 fifth 8 sixth 4 seventh 2 and eighth is 1 so because I did 01010101 it would say 0 for 1 so its not equal to or above 128 but it will look at the 2nd number and see a 1 so it knows it is at least 64 so it will look at the rest and see it equals 85 so when you get another string like just 00000001 and subtract it, it will just do 84 and return that into binary as 01010100
 The calculator when dividing with zero will indeed print Nan (Non active number)
 Also if there is an overflow of numbers it will print Overflow
 Also with random characters like "w" it will print error as it is only meant to work with 8 digits of 0 and 1s

