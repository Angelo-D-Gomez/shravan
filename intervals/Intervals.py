# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
  merge_tup = []
  while tuples_list:
    for x in range(1, len(tuples_list)):
      if tuples_list[0][0] > tuples_list[x][0]:
        if tuples_list[0][0] < tuples_list[x][1]:
          if tuples_list[0][1] > tuples_list[x][1]:
            # Make into tuples (with greatest/smallest interval)
            # Then remove tuple x, make new merged tuple tuples_list[0][0]
            # Then break
            pass
          else:
            pass

  return merge_tup

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
  pass


def main():
  # read the input data and create a list of tuples
  in_file = open('intervals.in.txt', 'r')
  interval_num = in_file.readline()
  intervals_list = []
  for x in range(int(interval_num)):
    interval = in_file.readline().split(" ")
    int_tup = (int(interval[0]), int(interval[1]))
    intervals_list.append(int_tup)
  in_file.close()

  # merge the list of tuples
  intervals_list = merge_tuples(intervals_list)
  # print the merged list

  # sort the list of tuples according to the size of the interval

  # print the sorted list


if __name__ == "__main__":
  main()
