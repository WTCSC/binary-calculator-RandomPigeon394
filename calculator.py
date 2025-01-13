import math
def binary_calculator(bin1, bin2, operator):
    # your code here
#Bin1 
pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0
pos5 = 0
pos6 = 0
pos7 = 0
pos8 = 0
sum_1 = 0

if bin1[0] = "1":
    pos1 = 128
if bin1[1] = "1":
    pos2 = 64
if bin1[2] = "1":
    pos3 = 32
if bin1[3] = "1":
    pos4 = 16
if bin1[4] = "1":
    pos5 = 8
if bin1[5] = "1":
    pos6 = 4
if bin1[6] = "1":
    pos7 = 2
if bin1[7] = "1":
    pos8 = 1

#Bin2 
upos1 = 0
upos2 = 0
upos3 = 0
upos4 = 0
upos5 = 0
upos6 = 0
upos7 = 0
upos8 = 0
sum_2 = 0

if bin2[0] = "1":
    upos1 = 128
if bin2[1] = "1":
    upos2 = 64
if bin2[2] = "1":
    upos3 = 32
if bin2[3] = "1":
    upos4 = 16
if bin2[4] = "1":
    upos5 = 8
if bin2[5] = "1":
    upos6 = 4
if bin2[6] = "1":
    upos7 = 2
if bin2[7] = "1":
    upos8 = 1

    answer_num = 0


    print(answer_num)

    if any (char in "23456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+{}|:<>?-=[]\';,./`" for char in bin1[ :8])
         print("Error")
        else:
            if any (char in "23456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+{}|:<>?-=[]\';,./`" for char in bin2[ :8])
             print("Error")
             if sum_2 == 0:
                print("NaN")
                else:
                    if operator is == "+":
                      Answer_num = (sum_1 + sum_2)
                    if operator is == "-":
                      Answer_num = (sum_1 - sum_2)
                      if operator is == "*":
                      Answer_num = (sum_1 * sum_2)
                    if operator is == "/":
                        Answer_num = int(math.floor(sum_1 / sum_2))
                    if answer_num < 0:
                        print("Overflow")
                        return()
                    if answer_num > 256:
                        print("Overflow")
                        return()
                    else:
                        binary = ""
                        if answer_num >= 128:
                            binary = binary + '1'
                            answer_num -= 128
                        else:
                            binary += "0"
                        if answer_num >= 64:
                            binary = binary + '1'
                            answer_num -= 64
                        else:
                            binary += "0"
                        if answer_num >= 32:
                            binary = binary + '1'
                            answer_num -= 32
                        else:
                            binary += "0"
                        if answer_num >= 16:
                            binary = binary + '1'
                            answer_num -= 16
                        else:
                            binary += "0"
                        if answer_num >= 8:
                            binary = binary + '1'
                            answer_num -= 8
                        else:
                            binary += "0"
                        if answer_num >= 4:
                            binary = binary + '1'
                            answer_num -= 4
                        else:
                            binary += "0"
                        if answer_num >= 2:
                            binary = binary + '1'
                            answer_num -= 2
                        else:
                            binary += "0"
                        if answer_num >= 1:
                            binary = binary + '1'
                            answer_num -= 1
                        else:
                            binary += "0"

                        return binary
Binary_calculator("01111111", "10000000", "+")

