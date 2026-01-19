try:
  age=int(input("Enter your age:"))
  if age>=18:
    print("You are eligible for voting.")
  else:
    print("You are not eligible for voting.")
except ValueError:
  print("Please enter your age in integer!")
