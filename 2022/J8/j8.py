carte = []
with open('./input.txt', 'r') as forest:
    for ligne in forest:
        carte.append(ligne.replace('\n',''))

def isBorder(line_index, column_index):
    if line_index == 0 or line_index == 98:
        return True
    if column_index == 0 or column_index == 98:
        return True

    return False

def isBiggerOnHorizontal(line_index, column_index):
    print(line_index, column_index)
    current_line = [int(x) for x in list(carte[line_index])]

    left_side = current_line[slice(column_index)]
    right_side = current_line[slice(column_index+1, 99)]

    tested_tree_size = int(carte[line_index][column_index])

    max_left = max(left_side)
    max_right = max(right_side)

    return tested_tree_size > max_left or tested_tree_size > max_right

def isBiggerOnVertical(line_index, column_index):
    current_vertical = []
    for line in carte:
        tree = int(line[column_index])
        current_vertical.append(tree)

    upper_side = current_vertical[slice(line_index)]
    bellow_side = current_vertical[slice(line_index+1, 99)]

    tested_tree_size = int(carte[line_index][column_index])

    max_upper = max(upper_side)
    max_bellow = max(bellow_side)

    return tested_tree_size > max_upper or tested_tree_size > max_bellow

def isVisible(line_index, column_index):
    if isBorder(line_index, column_index):
        return True

    return isBiggerOnVertical(line_index, column_index) or isBiggerOnHorizontal(line_index, column_index)


n = len(carte)
compteur = 0
for line_index in range(n):
  for column_index in range(len(carte[line_index])):
    if isVisible(line_index, column_index):
      compteur += 1

# Affichage du résultat
print(compteur)