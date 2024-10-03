import random
from vocabulary_lists import existing_lists
from vocabulary_lists import frutas_fruits

def test_voc_español_english():
  number_items = len(frutas_fruits)
  
  chosen_item = random.randint(0, (number_items - 1))
  
  chosen_word_español = frutas_fruits[chosen_item]['español']
  chosen_word_english = frutas_fruits[chosen_item]['english']
  
  print(chosen_word_español)
  user_answer = input("Translate to English: ").lower()
  
  if str(chosen_word_english) == str(user_answer):
    print("  ✅")
  else:
    print("  Wrong answer...")

def test_voc_english_español():
  number_items = len(frutas_fruits)
  
  chosen_item = random.randint(0, (number_items - 1))
  
  chosen_word_español = frutas_fruits[chosen_item]['español']
  chosen_word_english = frutas_fruits[chosen_item]['english']
  
  print(chosen_word_english)
  user_answer = input("Traduzca al español: ").lower()
  
  if str(chosen_word_español) == str(user_answer):
    print("  Correcto!")
  else:
    print("  Respuesta incorrecta...")

def test_user():
  if user_continue == '+':
    direction = random.randint(0,1)

    for i in range(0,11):
      if direction == 0:
        test_voc_english_español()
        
      elif direction == 1:
        test_voc_español_english()

#The actual code starts here 

print("Hi! Let's get some vocabulary practice")
#print("Chose a theme from the list below:")
#print(existing_lists)

practice_is_over = False

while practice_is_over == False:
  user_continue = input("¿Continuar? / Continue? (+ | /) : ")

  if user_continue == '+':
    test_user()

  elif user_continue == '/':
    print("Ok. Adiós! Bye!")
    practice_is_over = True
  else:
    print(f"Continuar / Continue = + \nTerminar / Finish = / \n  Please enter a valid answer...")