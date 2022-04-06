#ask user for new password
newpwd = input("Enter your new password: ")
#initialise some boolean variables which can then be set when we find things we are looking for
isLongEnough = False
containsUpper = False
containsLower = False

#check the length of the password is greater than or equal to 8
if len(newpwd) >= 8:
  isLongEnough = True # set boolean var to True

#loop through each letter in the password
for char in newpwd:
  #check is there is a lower case letter, by turning it to lowercase and seeing if its equal to itself
  #also have to check its not a number
  if char.lower() == char and not char.isdigit():
    containsLower = True # set boolean var to True
  #do the same with upper case
  if char.upper() == char and not char.isdigit():
    containsUpper = True # set boolean var to True

#check if all 3 booleans are True
if isLongEnough and containsUpper and containsLower:
  print("password accepted")
  pwdcheck = input("Please re-enter new password ")
  #keep asking until they can re type new password correctly
  while pwdcheck != newpwd:
    pwdcheck = input("passwords don't match! Please re-enter new pwd ")
  print("Congratulations you have changed your password")
else:
  print("Your new password is not strong enough. Please ensure is is 8 characters of more in length and contains both upper and lower case")
  # An improvement would be to tell user which of the tests the password failed on...