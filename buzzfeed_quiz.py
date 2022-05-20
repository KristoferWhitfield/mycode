#!/usr/bin/python3

# destiny what guardian are you
# user will take a quiz if they want speed=hunter strength=titan healing=warlock


guardian_question = ""
guardian_question_two = ""
powers = ["strength"," speed", "recovery"]
animal_powers = ["Do you roar like the mighty lion?",
                 "Are you as stealthy as a viper?",
                 "Do you soar like a phoenix?"]
yesno = ["yes", "no"]


while guardian_question not in powers:

    guardian_question = input("Want to know what guardian are you? Do you seek strength, speed or recovery?")


if guardian_question.lower() == "strength":
    while True:
        guardian_question_two = input("Choose yes or no. " + animal_powers[0])
        if guardian_question_two.lower() == "yes":
          print("You stand with the powerful titans")
          break
        elif guardian_question_two.lower() == "no":
            #guardian_question = input("Want to know what guardian are you? Do you seek strength, speed or recovery?")
            print("You're not worth of this guardian!")
            break
        elif guardian_question_two.lower() not in yesno:
            print("Choose yes or no. " + animal_powers[0])
    
if guardian_question.lower() == "speed":
    while True:
     guardian_question_two = input("Choose yes or no. " + animal_powers[1])
     if guardian_question_two.lower() == "yes":
      print("Fight from the shaddows with the devious hunters")
      break
     elif guardian_question_two.lower() == "no":           
       # guardian_question = input("Want to know what guardian are you? Do you seek strength, speed or recovery?")
       print("You're not worth of this guardian!")
    elif guardian_question_two.lower() not in yesno:
        print("Choose yes or no. " + animal_powers[1])

if guardian_question.lower() == "recovery":
    while True:
     guardian_question_two = input("Choose yes or no. " + animal_powers[2])
    if guardian_question_two.lower() == "yes":
     print("Blast your foes with the mystical warlocks")
     break
    elif guardian_question_two.lower() == "no":                       
       # guardian_question = input("Want to know what guardian are you? Do you seek strength, speed or recovery?")
       print("You're not worth of this guardian!")
    elif guardian_question_two.lower() not in yesno:
        print("Choose yes or no. " + animal_powers[2])


elif guardian_question.lower() not in powers:
                                # I tweaked this condition to check if the correct
                                # answer was in this list of correct answers or not
    guardian_question = input("Try only seeking strength, speed, or recovery")

    # looks good! you could reuse this code and ask a few more questions very easily!
    # try for three

