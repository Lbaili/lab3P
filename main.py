
# Author: Chang Li cxl5844@psu.edu
# Collaborator: Daniel Mikita djm6907@psu.edu 
# Collaborator: John O’Toole jbo5232@psu.edu 
# Section: 1
# Breakout: 8

def sum_n(n):
  if  n <= 0 :
    return 0
  else :
    return sum_n(n-1)+n

def print_n(s, n):
  if n == 0 :
    return 

  else :
    print(s)
    print_n(s, n-1)
    

if __name__ =="__main__":
  a = int(input("Enter an int: "))
  print(f"sum is {sum_n(a)}.")
  b = input("Enter a string: ")
  print_n(b, a)
