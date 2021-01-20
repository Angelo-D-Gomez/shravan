def read_input():
    # open file for reading
    in_file = open('word.in', 'r')
    # read m and n
    coords = in_file.readline().strip().split()
    m = int(coords[0])
    n = int(coords[1])

    # skip blank line
    in_file.readline()

    # read the grid of characters
    word_grid = []
    for _ in range(m):
        word_grid.append(list(map(lambda x: x[0], in_file.readline().rstrip().split())))

    # skip blank line
    in_file.readline()
    k = int(in_file.readline().strip())

    # read the list of words
    word_list = []
    for _ in range(k):
        word_list_item = in_file.readline().strip()
        word_list.append(word_list_item)
    
    # close the input file
    in_file.close()

    return word_grid, word_list

def main():
    # read input from file
    word_grid, word_list = read_input()

    #### do NOT change anything above this line ####
    #### make changes in this section only      ####

    # call word_search() using the word_grid and word_list parameters
    for word in word_list:
        word_coordinates = word_search(word_grid, word)
        print(str(word_coordinates[0]) + " " + str(word_coordinates[1]))


#  Input: word_grid is a 2-D list of characters
#         word_to_search is a SINGLE word to look for in the word_grid
#  Output: function RETURNS a TUPLE representing the
#          indices (row, col) of the first letter of the word_to_search
#          if word does not exist, return (-1, -1)
def word_search (word_grid, word_to_search):
    pass


if __name__ == "__main__":
    main()
