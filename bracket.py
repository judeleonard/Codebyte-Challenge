"""Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, 
and return the number of valid combinations that can be formed with num pairs of parentheses. 
For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). 
There are 5 total combinations when the input is 3, so your program should return 5."""

def BracketCombinations(num):
  output = (fact(2*num) /(fact(num+1)*fact(num)))
  #return int(output)

  # code goes here
  return int(output)

def fact(x):
  if x ==0:
    return 1
  else:
    return x * fact(x-1)
  

# keep this function call here 
print(BracketCombinations(input()))