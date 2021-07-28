def binary_search(list_b,key):
  low=0
  high=len(list_b)-1
  mid=(high+low)//2
  while low <= high:
    mid=(high+low)//2
    if key>list_b[mid]:
      low=mid+1
    elif key<list_b[mid]:
      high=mid-1
    else:
      return mid
  return -1

  # print(len(list_b))
  # print('low is',low)
  # print('high is', high)
  # print('mid is',mid)
  # if key==list_b[mid]:
  #   return mid
  # elif key<list_b[mid]:
  #   return binary_search(list_b,key)
  # # elif key<list_b[mid]:
  #   high=mid-1
  # else:
  #   return mid
print(binary_search([4, 8, 15, 16, 23, 42], 15))
print(binary_search([-131, -82, 0, 27, 42, 68, 179], 42))
print(binary_search([11, 22, 33, 44, 55, 66, 77], 90))
print(binary_search([1, 2, 3, 5, 6, 7], 4))
print(binary_search([4], 4))
