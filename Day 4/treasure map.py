
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
naksha = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")     #lets consider our input 23

row_num = int(position[1])
column_num = int(position[0])

selected_row = naksha[row_num - 1]
# col_selection = naksha[column_num - 1]
selected_row[column_num-1] = "X"                                #changing element in the nested array i.e. map[selected_row[selected colomn]]

print(f"{row1}\n{row2}\n{row3}")


