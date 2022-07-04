import random
def did_prisoners_escape():
    number_list = []
    prisoner_dict = {}
    box_dict = {}
    number_of_prisoners = 100 #! Edit this number to change number of prisoners

    #initialize number_list and prisoner_dict
    for i in range(1,number_of_prisoners-1):
        number_list.append(i)
        prisoner_dict[i] = None

    #assign numbers to each box
    for i in range(1,number_of_prisoners-1):
        random_box =  number_list.pop(random.randrange(len(number_list)))     
        box_dict[i] = random_box

    #execute loop algorithm
    for i in range(1,number_of_prisoners-1):
        loop_size = 1
        next_box_number = i
        while box_dict[next_box_number] != i and loop_size < number_of_prisoners/2+1: #open up to half the boxes
            next_box_number = box_dict[next_box_number]
            loop_size += 1

        prisoner_dict[i] = loop_size
        
    #loop_size of number_of_prisoners/2+1 indicates half the boxes were opened but prisoner number was not found
    if number_of_prisoners/2+1 in prisoner_dict.values(): return False
    else: return True


# Run algorithm multiple times and calculate overall probability of escape
escaped = 0
attempts = 1000 #! Increase this number for better accuracy
for i in range (attempts):
    if did_prisoners_escape(): escaped += 1

overall_escape_probability = escaped/attempts
print(overall_escape_probability)


