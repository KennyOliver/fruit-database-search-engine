def file_search(to_search):
  file = open("fruits.txt",'r')
  print("<-- RESULTS -->")
  for record in file:
    if to_search in record.lower():
      print(record)
  print("=" * 20)
  file.close()
#====================
def get_all():
  file = open("fruits.txt",'r')
  print("<-- RESULTS: Print All -->")
  for record in file:
    print(record)
  print("=" * 20)
  file.close()
#====================
def letter_search(letter):
  file = open("stuff.txt",'r')
  print(f"<-- RESULTS for {letter} -->".format(letter))
  for record in file:
    if record.startswith(letter):
      print(record)
  print("=" * 20)
  file.close()
#====================
# MAIN PROGRAM
print("\n!Fruit Database Search Engine!")
print("\t[!] Normal search\n","\t[%] Letter category\n","\t[*] Retrieve all")
option = input("Enter option symbol\n--> ")
while option not in ['*','%','!']:
  option = input("Enter option symbol\n--> ")

if option == '*':
  print("\n")
  get_all()
elif option == '%':
  chosen_letter = input("Enter letter\n--> ").upper()
  print("\n")
  letter_search(chosen_letter)
else:
  query = input("Enter query\n--> ").lower()
  print("\n")
  file_search(query)