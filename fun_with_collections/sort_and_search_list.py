#def make_list():
  #  """function will ask the user until the counter reaches 3
  #     it will call the get_input function where the user enters
  #     their values and returns it back to the make_list function
  #     and then finally the list will be printed"""
   # count = 3
   # list = []
  #  while count > 0:
 #       print("Please enter an item you want in the list. ")
  #      list.append(get_input())
   #     count -= 1
   # print(list)
   # return list

def sort_list():
    """new function will ask the user for input three times. The list will be stored into the variable 'list
       and then the list will be sorted and stored into the 'new_list' variable"""
    count = 3
    list = []
    while count > 0:
        print("Please enter an item you want in the list. ")
        list.append(get_input())
        new_list = sorted(list)
        count -= 1
    print(new_list)
    #no return is being used since we can print the new list in the function

def search_list():
    count = 3
    list = []
    while count > 0:
        print("Please enter an item you want in the list. ")
        list.append(get_input())
        count -= 1

    new_list = list.index(1)
    print(new_list)






def get_input():
    user_input = input()
    return user_input

if __name__ == '__main__':
  #  make_list()
    sort_list()
    search_list()
