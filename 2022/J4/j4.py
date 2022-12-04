from classes import Pair

total_in = 0
total_overlaps = 0


with open('./input.txt', 'r') as affectations:

    for pair in affectations:
        current_pair = Pair(pair.replace('\n', ''))

        if(current_pair.isTotallyIn()):
            total_in += 1

        if(current_pair.isOverlap()):
            total_overlaps += 1


print("Total in is {}, total overlaps is {}".format(total_in,total_overlaps))