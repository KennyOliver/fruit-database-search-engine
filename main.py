def file_search(to_search):
  file = open("fruits.txt",'r')
  
  print("<-- Results -->")
  
  for record in file:
    if to_search in record:
      print(record)
  
  print("=" * 20)
  
  file.close()
#=====
def get_all():
  file = open("fruits.txt",'r')
  
  print("<-- Print All -->")
  
  for record in file:
    print(record)
  
  file.close()
#=====
def letter_search(letter):
  file = open("stuff.txt",'r')
  
  print(f"<-- {letter} -->".format(letter))
  
  for record in file:
    if record.startswith(letter):
      print(record)
  
  file.close()


# MAIN PROGRAM
print("Fruit Search")
print("\t[*] Retrieve all\n","\t[%] Letter category\n","\t[!] Normal search")
option = input("Enter option symbol\n--> ")
while option not in ['*','%','!']:
  option = input("Enter option symbol\n--> ")

if option == '*':
  get_all()
elif option == '%':
  chosen_letter = input("Enter letter\n--> ").upper()
  letter_search(chosen_letter)
else:
  query = input("Enter query\n--> ").title()
  file_search(query)