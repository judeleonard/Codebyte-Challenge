def FindIntersection(strArr):
  ln = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
  val1, val2 = set(ln[0]), set(ln[1])

  # remove redundant char
  val1.split(", ")
  val2.split(", ")

  # convert all char to int
  val_1 = [int(i) for i in val1]
  val_2 = [int(i) for i in val2]
  strArr = [value for value in val_1 if value in val_2]

  # code goes here
  return strArr

# keep this function call here 
print(FindIntersection(input()))