def calculate_love_score(name1, name2):
    list1 = ["T","R","U","E"]
    list2 = ["L","O","V","E"]

    total = 0
    total_1 = 0
    total_2 = 0
    total_3 = 0
    name1 = name1.upper().replace(" ","")
    name2 = name2.upper().replace(" ","")

    for i in range(len(name1)):
        if name1[i] in list1:
            total+=1

        if name1[i] in list2:
            total_1+=1

    for j in range(len(name2)):
        if name2[j] in list1:
            total_2+=1

        if name2[j] in list2:
            total_3+=1

    total_true = total + total_2
    total_love = total_1 + total_3

    str(total_love)
    str(total_true)

    print(f"Your love score is {total_true}{total_love}")

calculate_love_score("Angela Yu", "Jack Bauer")

