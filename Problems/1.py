from pathlib import Path
import os


def find_max_cals(input):

    cals_elf = 0
    max_cals_elf = 0

    for i in range(len(input)):
        if input[i] == '':
            max_cals_elf = max(max_cals_elf, cals_elf)
            cals_elf = 0
        
        else:
            cals_elf += int(input[i])
        
    print(f'The elf carrying the most has {max_cals_elf} calories \n')


def top_three_elfs(input):
    cals_elf = 0
    cals_list = []

    for i in range(len(input)):
        if input[i] == '':
            cals_list.append(cals_elf)
            cals_elf = 0
        
        else:
            cals_elf += int(input[i])

    cals_list.sort(reverse=True)

    print(f'The top three elfs have {sum(cals_list[:3])} calorie \n')

def main():
    #print(Path(__file__).parents[1])
    #print(os.path.dirname(__file__))
    #os.chdir('..')
    #print(os.path.join(os.getcwd(), "/Data/input_p1.txt"))

    data_path = '/Users/luisrodri/Documents/GitHub/Advent-of-code-2022/Data/day_1_input.txt'

    file = open(data_path)
    input = file.readlines()
    input = [i.rstrip() for i in input]

    print('*PROBLEM 1*')
    find_max_cals(input)

    print('*PROBLEM 2*')
    top_three_elfs(input)



if __name__ == "__main__":
    main()
