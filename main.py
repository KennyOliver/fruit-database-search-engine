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
print("\nFruit Search")
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
  query = input("Enter query\n--> ").lower()
  file_search(query)