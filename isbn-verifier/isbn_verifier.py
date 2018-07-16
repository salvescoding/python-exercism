def verify(isbn):
  isbn = ''.join(i for i in isbn if i.isdigit() or i == 'X')
  total_num = list(range(10, 0, -1))
  if len(isbn) is not 10 or ('X' in isbn and 'X' is not isbn[-1]):
      return False
  for index, element in enumerate(isbn):
      if element == 'X':
          total_num[index] *= 10
      else:
          total_num[index] *= int(element)
  return sum(total_num) % 11 == 0
