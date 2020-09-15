
# Author: Chang Li cxl5844@psu.edu
# Collaborator: Daniel Mikita djm6907@psu.edu
# Collaborator: John O’Toole jbo5232@psu.edu
# Section: 1
# Breakout: 8

def sum_n(n):
  if  n-1 == 0 :
    return 1
  else :
    return sum_n(n-1)+n

def print_n(s, n):
  if n-1 <= 0 :
    return print(s)

  else :
    print_n(s, n-1)
    print(s)
    return 
    
    



if __name__ =="__main__":
  a=int(input("Enter an int: "))
  print(f"sum is {sum_n(4)}")
  b=input("Enter a string: ")
  print(print_n(b, a))
