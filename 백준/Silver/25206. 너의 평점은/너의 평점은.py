grade_table = []
weight_table = []
result = float(0)
subject_num = 20
score_sum = 0
iVal = ""

for i in range(0, subject_num):
    iVal = input()
    length = len(iVal)
    if iVal[length-1: length] != "P":
        weight_table.append(iVal[length-6: length-3])
        grade_table.append(iVal[length-2: length])
    
for i in range(0, len(grade_table)):
    if grade_table[i] == "A+":
        result += 4.5 * float(weight_table[i])
    elif grade_table[i] == "A0":
        result += 4.0 * float(weight_table[i])
    elif grade_table[i] == "B+":
        result += 3.5 * float(weight_table[i])
    elif grade_table[i] == "B0":
        result += 3.0 * float(weight_table[i])
    elif grade_table[i] == "C+":
        result += 2.5 * float(weight_table[i])
    elif grade_table[i] == "C0":
        result += 2.0 * float(weight_table[i])
    elif grade_table[i] == "D+":
        result += 1.5 * float(weight_table[i])
    elif grade_table[i] == "D0":
        result += 1.0 * float(weight_table[i])
    elif grade_table[i] == "F":
        result += 0.0 * float(weight_table[i])
    # elif grade_table[i] == "P":
    #     result += 0.0 * float(weight_table[i])
    #     score_sum += 0.0
    score_sum += float(weight_table[i])
if score_sum == 0:
    score_sum = 1
print(result / score_sum)