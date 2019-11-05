# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}

for i in range(n):  
  l = list(input().rstrip().split())
  name = l[0]
  phoneNumber = int(l[1])
  phoneBook[name] = phoneNumber

for j in range(n):
  try:
    name = str(input())
  except EOFError:
    break
  
  if name in phoneBook:
    phoneNumber = phoneBook[name]
    print(name + '=' + str(phoneNumber))
  else:
    print("Not found")