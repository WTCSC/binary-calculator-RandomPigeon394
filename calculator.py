import math
def binary_calculator(bin1, bin2, operator):
    # your code here
    #first I created a function called sum1 to act as a base for the binary calculator
    sum_1 = 0
    #Then I had to create bins for the calculator so that it knows there are 8 digits and if there is a 1 in the first slot I would set that = to 128 so that it would add 128 if there is a 1 in the first slot and so on for the other digits 
    if bin1[0] == "1":
        sum_1 += 128
    if bin1[1] == "1":
        sum_1 += 64
    if bin1[2] == "1":
        sum_1 += 32
    if bin1[3] == "1":
        sum_1 += 16
    if bin1[4] == "1":
        sum_1 += 8
    if bin1[5] == "1":
        sum_1 += 4
    if bin1[6] == "1":
        sum_1 += 2
    if bin1[7] == "1":
        sum_1 += 1

    #Then I created the 2nd sum and 2nd bin numbers that I will be adding or subtracting from
    sum_2 = 0

    if bin2[0] == "1":
        sum_2 += 128
    if bin2[1] == "1":
        sum_2 += 64
    if bin2[2] == "1":
        sum_2 += 32
    if bin2[3] == "1":
        sum_2 += 16
    if bin2[4] == "1":
        sum_2 += 8
    if bin2[5] == "1":
        sum_2 += 4
    if bin2[6] == "1":
        sum_2 += 2
    if bin2[7] == "1":
        sum_2 += 1
    #Next I created a answer number function as the asnwer to both sums
    answer_num = 0
    #Then I just tell it if there is any other characters besides 1 and 0 then there is a error and it cant calculate that 
    if any (char in "23456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+{}|:<>?-=[]\';,./`" for char in bin1[ :8]):
         print("Error")
    else:
        if any (char in "23456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+{}|:<>?-=[]\';,./`" for char in bin2[ :8]):
            print("Error")
        if sum_2 == 0:
            print("NaN")
        else:
            #Next I tell it that if the operator is addition (+) then to add sum1 and sum2 
            if operator == "+":
                    answer_num = (sum_1 + sum_2)
            #Here I tell it to minus 
            if operator == "-":
                    answer_num = (sum_1 - sum_2)
            #Then this would be multiplacation
            if operator == "*":
                    answer_num = (sum_1 * sum_2)
            #And this is division
            if operator == "/":
                    answer_num = int(math.floor(sum_1 / sum_2))
            if answer_num < 0:
                    return("Overflow")
            if answer_num > 256:
                    return("Overflow")
            else:
            #Next if the answer is above or equal to 128 then it will put a 1 in the first slot
                    binary = ""
                    if answer_num >= 128:
                        binary = binary + '1'
                        answer_num -= 128
                    else:
                        #Next if the answer is above or equal to 64 then it will put a 1 in the second slot
                        binary += "0"
                    if answer_num >= 64:
                        binary = binary + '1'
                        answer_num -= 64
                    else:
                        #Next if the answer is above or equal to 32 then it will put a 1 in the third slot
                        binary += "0"
                    if answer_num >= 32:
                        binary = binary + '1'
                        answer_num -= 32
                    else:
                        #Next if the answer is above or equal to 16 then it will put a 1 in the fourth slot
                        binary += "0"
                    if answer_num >= 16:
                        binary = binary + '1'
                        answer_num -= 16
                    else:
                        #Next if the answer is above or equal to 8 then it will put a 1 in the fifth slot
                        binary += "0"
                    if answer_num >= 8:
                        binary = binary + '1'
                        answer_num -= 8
                    else:
                        #Next if the answer is above or equal to 4 then it will put a 1 in the sixth slot
                        binary += "0"
                    if answer_num >= 4:
                        binary = binary + '1'
                        answer_num -= 4
                    else:
                        #Next if the answer is above or equal to 2 then it will put a 1 in the seventh slot
                        binary += "0"
                    if answer_num >= 2:
                        binary = binary + '1'
                        answer_num -= 2
                    else:
                        #And lastly if the answer is above or equal to 1 then it will put a 1 in the eighth slot
                        binary += "0"
                    if answer_num >= 1:
                        binary = binary + '1'
                        answer_num -= 1
                    else:
                        binary += "0"

                    return binary
print (binary_calculator("00000011", "00000010", "*"))

