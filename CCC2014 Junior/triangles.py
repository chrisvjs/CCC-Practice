side_one = int(input())
side_two = int(input())
side_three = int(input())

if side_one + side_two + side_three == 180:
  if side_one == side_two == side_three:
    print("Equilateral")
  elif side_one != side_two != side_three != side_one:
    print("Scalene")
  else:
    print("Isosceles")
else:
  print("Error")