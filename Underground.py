import sys,time, random

#function for defining typewriting text
def typingprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  
def typinginput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  return value  
#Making sure we put all the functions first so we can call them later

#This is the intro (Done by Everyone)

def start_game():
    typingprint("""
                \033[1;31;40m
  _______ _            _    _           _                                          _ 
 |__   __| |          | |  | |         | |                                        | |
    | |  | |__   ___  | |  | |_ __   __| | ___ _ __ __ _ _ __ ___  _   _ _ __   __| |
    | |  | '_ \ / _ \ | |  | | '_ \ / _` |/ _ \ '__/ _` | '__/ _ \| | | | '_ \ / _` |
    | |  | | | |  __/ | |__| | | | | (_| |  __/ | | (_| | | | (_) | |_| | | | | (_| |
    |_|  |_| |_|\___|  \____/|_| |_|\__,_|\___|_|  \__, |_|  \___/ \__,_|_| |_|\__,_|
                                                    __/ |                            
                                                   |___/  
                \033[1;31;40m\n""")
    print("")
    typingprint("Developed by Team 1\n")
    print("")
    game_start = input("\033[1;33;40mStart Game Y/N\n").lower()
    if game_start == "Y".lower():
        intro()
    elif game_start == "N".lower():
        typingprint("\033[1;33;40mOkay. thanks for trying")
        time.sleep(3)
        sys.exit()
    else:
        typingprint("\033[1;33;40mPlease use Y or N")
        start_game()

def intro():
    typingprint("\033[1;36;40mThe year is 20xx and global warming has started to cause disasters over the world. Capital cities have now been designated safe zones.\n")
    print("")
    typingprint("You, a civil servant living in London UK, are on your way home on the tube from London Council after a hard days work.\n")
    print("")
    typingprint("Suddenly the ground starts to rumble and then vilonetly shakes.\n")
    print("")
    typingprint("The train comes to a sudden stop which lunges you forward. You hit your head on a bar and blackout\n")
    print("")
    print("")
    typingprint("THE UNDERGROUND")
    print("")
    print("")
    typingprint("You start to come round your eyes still blurry. You hear a voice in the distance\n")
    print("")
    typingprint("\033[1;33;40m\"Hello can you hear me are you okay?\"\n")
    print("")
    typingprint("\033[1;34;40mYour eyes begin to focus and you see a man kneeling down looking over you.\n")
    print("")
    print("")
        
#Adds some easter eggs we've decided to put
    player_name = input("\033[1;33;40m\"Looks like nothings broken and your starting to come round. What's your name?\"""\n").lower() # asks the player to input their name
    if player_name == "Keira".lower():
        typingprint("\033[1;34;40mYou look around there are posters on the wall as one catches your eye it reads CN. But then you turn to look at the person overlooking you.\n")
        print("")
        typingprint(f"\033[1;33;40m\"Nice to meet you {player_name} I'm the conductor I'm gonna head to the front of the train to see if I can get it going again.\"\n")
        print("")
        print("\033[1;33;40m\"When you think you can STAND meet me up there.\"\n")
        stand_up()# moves to another function to further the game
    elif player_name == "Gordon".lower():
        typingprint("\033[1;33;40mTime to wake up then Mr Freeman. You have a lot of work to do.\"\n \033[1;34;40m You open your eyes and look at the person overlooking you.\n")
        print("")
        typingprint(f"\033[1;33;40m\"Nice to meet you {player_name} I'm the conductor I'm gonna head to the front of the train to see if I can get it going again.\n")
        print("")
        print("\033[1;33;40m\"When you think you can STAND meet me up there.\"\n")
        stand_up()# moves to another function to further the game
    else:
        typingprint(f"\033[1;33;40m\"Nice to meet you {player_name} I'm the conductor I'm gonna head to the front of the train to see if I can get it going again.\"\n")
        print("")
        print("\033[1;33;40m\"When you think you can STAND meet me up there.\"\n")
        stand_up()# moves to another function to further the game

#The player should now stand up
def stand_up():
    player_stand = input("\033[1;36;40m What do you want to do?\n").lower() # stores the player answer as a variable
    if player_stand == "STAND".lower(): # if the player inputs the correct text
        print("")
        typingprint("\033[1;34;40mYou stand up and brush off some dust as the train suddenly starts up again.\n")
        print("")
        typingprint("You head up to the front of the train and find the conductor there.\n")
        print("")
        typingprint("\033[1;33;40m\"Well managed to get it working again we're gonna continue along the line and stop at every platform see if we can find a way out.\"\n")
        area_1()
    else: # if the player answers anything else run this
        typingprint("\033[1;34;40mThe train starts up and keeps going suddenly it hits a blockage of rubble caused by the quake you lunge forward again and crack your neck.\n")
        print("")
        typingprint("Hint: Try typing stand next time to stand up\n")
        print("")
        typingprint("""
                    
                    """)
        game_over()

#Now we come to area one (Done by Christopher Benson)
def area_1():
    print("")
    typingprint("\n\033[1;32;40m\"First stop: White City\". \n")
    typingprint("\n\033[1;34;40mThe train stops and the doors open to the platform. You take a look around the entrance is blocked by rubble but there looks like someone injured on the floor.\n")
    print("")
    print("\n\033[1;36;40mChoose a number:")
    print("1) Get off")
    print("2) Stay on Train")
    player_answer_1_area_1 = input() # stores a variable 
    if player_answer_1_area_1 == "1":
        task_1() # moves to task 1
    elif player_answer_1_area_1 == "2":
        typingprint("\033[1;33;40m\"Not gonna help? \n\033[1;34;40mSays the conductor.\n\033[1;33;40m Okay I guess to each their own doesn't look like we can't get out here anyway lets move on then.\"\n")
        area_2()
    else:
        print("Please use 1 or 2")
        area_1() # repeats back to area 1 if the user inputs anything else

#Task 1

def task_1(): # the first task the player must face
    typingprint("\033[1;34;40mYou step out and head over to the injured person there on the floor holding their leg they look at you surprised to see another person and say:\n")
    print("")
    typingprint("\033[1;35;40m\"Oh thank goodness other people are down here. I was doing some matienence work and was heading out when the quake happened.\"\n")
    print("")
    typingprint("\033[1;35;40m\"Luckily there should be some first aid at the shop over there behind the counter with a splint in it\"\n")
    print("")
    player_answer1_task1 = input("\033[1;36;40mDo you head over to the shop? Y/N\n").lower() # asks the player a condition
    if player_answer1_task1 == "Y".lower(): # if the player responds with Y
        typingprint("You head over to the shop and open the doors. The counters in front of you as you head over to it. You search behind it and sure enough there's a splint there behind a first aid kit.\n")
        print("")
        typingprint("You take the splint and bring it back to the injured person.\n")
        print("")
        typingprint("\033[1;35;40m\"Oh great you found it pass it here and I can put it on myself.\"\033[1;34;40m The person says.\n")
        print("")
        typingprint("You give the splint to the person and they tie it over there leg.\n")
        print("")
        typingprint("\033[1;35;40m\"That's better give us a hand and we can head back to the train. Names Dave by the way and I'm an enginner\"\n")
        print("")
        typingprint("\033[1;34;40m\nYou help them up and head back into the train the door closes behind you.\n")
        print("")
        typingprint("\033[1;33;40m\"Looks like we found a survivor eh.\"\033[1;34;40m The Conductor comments.\n")
        print("")
        typingprint("\033[1;33;40m\"Right next stop here we come\"\n")
        area_2()
    elif player_answer1_task1 == "N".lower(): # if the player responds with N
        typingprint("Suddenly the rubble behind them starts to shake and collapses on both of you.\n")
        print("""\033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
                  """)
        game_over() # runs the game over function
    else:
        print("\033[1;36;40mPlease use Y or N")
        task_1() # re-runs task 1 again

#Scenario 2 (Done by Adam Zain)

#move to area 2
def area_2():
    typingprint("\n\033[1;31;40m\"Next stop: Shepherd's Bush.\n\033[1;33;40m\n Hey do you hear something?\"\n\033[1;34;40m \nAs the conductor opens the door and you step outside a bit but the platform is covered in rubble.\n")
    
    typingprint("\033[1;34;40m\nYou hear agonising screams of help. You look around and can see bits of the rubble move\n")
    player_answer_2 = input("\033[1;33;40m \n\033[1;36;40m Do you want to 'Help' or 'Continue' onto the next platform:\n").lower() # Giving the player the option to help or continue on
    if player_answer_2 == "Help".lower():
        chance_task2 = (random.randint(1,2)) # assigns an interger to 2 values
        if chance_task2 == 1: # if one value is this do this
            typingprint("\033[1;34;40m\nYou decide to remove the rubble with your hands. It takes hours until you make any progress. However you notice the foundation becomes unsteady...until it collapses on you.\n")
            print("""
            \033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
            
            """)
            game_over()
        elif chance_task2 == 2: # if the other value is this do this
            typingprint("\033[1;34;40mIt takes time but you are able to remove the rubble and free the victims from being trapped\n")
            print("")
            typingprint("\033[1;34;40mThey thank you and move onto the train as you move back into the drivers room with the conductor\n")
            print("")
            typingprint("\033[1;33;40m\n\"Right looks like that's everyone lets move on shall we.\"\n\033[1;34;40m\n As you start moving again.\n")
            area_3()
    elif player_answer_2 == "Continue".lower():
      print("\033[1;34;40mYou go back to the train.\n\033[1;33;40m\"To be honest I wouldn't have attempted that either feels a bad to leave them but I don't think there's anything we could've done.\"\033[1;34;40m\n As you continue on.\n")
      area_3()
    else:
      print("\033[1;36;40mPlease try again using 'Help' or 'Continue' ")
      area_2()

#Scenario 3 (Done By Connor Scott)

def area_3():
    print("")
    typingprint("\033[1;31;40m\"Stop number three : Notting Hill Gate.\"\033[1;33;40m\n\n Here we are woahhhhh\" \033[1;34;40m\n\nThe doors open as the conductor gasps as lots of people in need start to attempt to board the train.\n")
    print("")
    typingprint("\033[1;34;40mThe people look panicky as they rush in and you realise this could end up getting bad.\n")
    task_3()

def task_3():
    player_action = input("\033[1;36;40m\nDo you 'defend' yourself against the crowd or 'reason' with them?\n").lower()
    if player_action == ("defend"):
        typingprint("\033[1;34;40m\nThe crowd try to rush on but you instinctly hit the door close button closing the door and starting the train again.\n")
        print("")
        typingprint("\033[1;34;40m\nYou hang your head thinking about all those people the conductor puts his hand on your shoulder.\n")
        print("")
        typingprint("\033[1;33;40m\"Nothing you could've done that mad rush might've killed us both if they all tried to get on. Onto the next station\"\n")
        area_4()
    # Adds a 50/50 chance for the man to reason with you, or attack resulting in game over.
    elif player_action == ("reason"):
         chance_task3 = (random.randint(1,2))
         if chance_task3 == 1:
            typingprint ("\033[1;34;40mThe crowd rush on and keep piling on you get pushed to the floor and get crushed as the people move over you.\n")
            print("""
                  \033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
                  
                  """)
            game_over()
         elif chance_task3 == 2:
            typingprint("\033[1;34;40mYou calm the crowd down and explain to the crowd to calmly walk onto the train in an orderly fashion.\n")
            print("")
            typingprint("\033[1;33;40m\"Nicely done\"\n\033[1;34;40m Noted the conductor \033[1;33;40m\n\"We've saved some more people too but doesn't look like there's a way to get here either right then onto the next one\"\n")
            area_4()
    else:
        print ("\033[1;36;40mPlease choose 'defend' or 'reason'.")
        task_3()

# SCENARIO 4 - TURN POWER ON AT OXFORD CIRCUS STATION (Done By Scott White)

# Arrive at OXFORD CIRCUS Station from NOTTING HILL GATE via the Central Line.

def area_4():
    print("")
    typingprint("\033[1;35;40m\"Stop 4: Oxford Circus\"\n\033[1;34;40m\n Exclaims the conducter and opens the door.\n\033[1;34;\n40m Suddenly the power goes out and your in complete darkness.\n")
    typingprint("\033[1;34;40mYou hear a voice in the darkness\n \033[1;32;40m\"Hello? Is there anybody there?\" \033[1;34;40m\nYou step a bit forward and call out.\n")
    print("")
    typingprint("\n\033[1;34;40mA weak voice replies.\n \033[1;32;40m'The power tripped out, we can't find our way to the platform for Kings Cross. Without ventilators and lights, we'll all die.\n")
    print("")
# DECISION - do you want to Find Switch or Escape? - WORKS TO HERE
# LOOK FOR SWITCH
    player_decision = input("\033[1;36;40mDo you decide to help the lost voice (type 'Find switch') or find the quickest way to escape (type 'Escape')\n").lower()
    if player_decision == "Find switch".lower():
        chance_task4 = (random.randint(1,2))
        if chance_task4 == 1:
            print("")
            typingprint("\n\"Do you know where I can find the switch?\"', you ask. The voice replies,\n \"\033[1;32;40mIt's up some stairs in a small box next to an Emergency Stop button, Please hurry.\"\n")
            typingprint("\033[1;34;40mThe conductor stops you and hands you a lit torch as you look around for the stairs. Finding them you head up.\n")
            print("")
            typingprint("\033[1;34;40m\nWith your strength fading, you follow the wall for some distance, negotiating wide doorways and other obstacles.\n Suddenly, you reach a corner and stop to catch your breath in the thickening atmosphere.\n")
            print("")
            typingprint("\033[1;34;40m\nYou shine the light down and find a small box with a rubber button. You find another small box next to it you head to the box flip the cover and click the switch.'n The power comes on!\n")
            print("")
            typingprint("You head back to the train as the conductor states \n\"\033[1;33;40mGood job everything seems to be working now ,the folks who helped are also on the train, right lets head on\"\n")
            area_5() # MOVE TO SCENARIO 5
        elif chance_task4 == 2:
            print("")
            typingprint("\"Do you know where I can find the switch?\"',\n you ask. The voice replies, \"\033[1;32;40mIt's up some stairs in a small box next to an Emergency Stop button, Please hurry.\"\n")
            print("")
            typingprint("\033[1;34;40m\nThe conductor stops you and hands you a lit torch as you look around for the stairs. Finding them you head up.\n")
            print("")
            typingprint("\033[1;34;40\nmWith your strength fading, you follow the wall for some distance, negotiating wide doorways and other obstacles. Suddenly, you reach a corner and stop to catch your breath in the thickening atmosphere.\n")
            print("")
            typingprint("\033[1;34;40mNothing happens. \nYou frantically click the switch up and down. \nNothing.\n You slump down to the platform.")
            print("""\033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
                  
                  """)
            game_over()
    elif player_decision == "Escape".lower(): # Escape
        print("")
        typingprint("\033[1;34;40m\nYou decide to find the quickest way out, and after fifteen minutes, in the dark climb an escalator. The echo of your footsteps indicates you are in a large open space. You find a second escalator.\n")
        print("")
        typingprint("\033[1;34;40mThe air feels like its getting thick and difficult to breath.\n \033[1;36;40m\nDo you decide to go back and find the switch (Type 'Go Back') or carry on up the escalator (Type 'Carry On')?")
        print("")
        second_chance = input()
        if second_chance == "Go back".lower():
            print("")
            typingprint("\033[1;34;40m\nWith your strength fading, you follow the wall for some distance, negotiating wide doorways and other obstacles.\n Suddenly, you reach a corner and stop to catch your breath in the thickening atmosphere.\n Stretching your arms, you slowly edge up the wall and find a small box with a rubber button.\nYou find another small box next to it, flip the cover and click the switch.\n")
            print("...................")
            print("\nThe power comes back on!  \nWith your sight returned, run back towards the train and jump on")
            area_5()
        elif second_chance == "Carry On".lower():
            print("")  
            typingprint("\033[1;34;40m\nThe air gets hotter as you climb to the top of the escalator. You find a door handle, twist and slowly push open the door. Stepping inside, you reach out for a wall to guide you. As you touch the cold surface, the door clicks with a dull thud. You are now trapped.\n")
            print("")
            print("""\033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
                  """)
            game_over()
    else:
        print("Try 'find switch' or 'escape'")
        area_4()

#Scenario 5 (Done by Everyone)

def area_5():
    print("")
    typingprint("\033[1;34;40m\nHalfway towards the next station the train stops suddenly but the train shuts down.")
    print("")
    typingprint("\033[1;33;40m\nLooks like we're gonna get out and walk on the tracks from here because it looks like we can get onto the platform from the tracks.")
    print("")
    typingprint("\033[1;36;40m\nSo what do you want to do? Did I just see sparks on the track.\n")
    print("1: Get out and walk")
    print("2: Wait a bit")
    player_answer_area_5 = input("\n\033[1;36;40mPlease Choose 1 or 2\n")
    if player_answer_area_5 == "1":
        typingprint("\033[1;34;40m\nYou get out and walk on the track but as soon as you do you get electrocuted and die.\n")
        print("""
              \033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
              
              """)
        
        game_over()
    elif player_answer_area_5 == "2":
        typingprint("\033[1;34;40m\nYou look outside the train and see sparks, it's probably fatal to walk on the tracks.")
        print("")
        typingprint("\033[1;34;40m\nThe conductor mentions \"\033[1;33;40mI saw what looks like a power junction for the tracks on the way here back a bit\"\n")
        print("")
        typingprint("\"It should be within arms reach from the door right at the back of the train")
        task_5()
    else:
        print("\033[1;36;40mPlease use 1 or 2")
        area_5()
        
def task_5():
    player_answer_area_5_2 = input("\033[1;33;40m\n\"Do you want to head to the back of the train?\"\033[1;34;40m asks the conductor Y/N\n").lower()
    if player_answer_area_5_2 == "Y".lower():
        typingprint("\033[1;34;40m\nYou walk to the back of the train and see the power terminal. \033[1;36;40m\nDo you take a look?")
        task_5_1()
    elif player_answer_area_5_2 == "N".lower():
        typingprint ("\033[1;33;40m\n\"Are you sure?? what else are you gonna do stay here for ever?\"\033[1;34;40m sneers the conductor.\n")
        task_5()
    else:
        print("\033[1;36;40mPlease use Y/N")
        task_5()

def task_5_1():
    typingprint("\033[1;34;40m\nYou take a look around, the door is open. In view is a power box")
    print("")
    typingprint("\nYou see a breaker switch that says 'On or Off' Its currently in the On position")
    switch_off = input("Press Y to turn it off\n").lower()
    if switch_off == "Y".lower():
        typingprint("\nYou pull the handle, you hear the power shutting down")
        print("")
        typingprint("\nYou head back to the front of the train, the conductor mentions the tracks may be safe to walk on now.")
        print("")
        typingprint("\nYou throw a coin onto the tracks to check if theres still a current and nothing happens")
        ending()
    else:
        typingprint("\033[1;36;40mYou stare at the switch")
        task_5_1()

def ending():
    print("")
    typingprint("\033[1;33;40m\nRight looks like we can walk on the tracks now to the platform. I suggest we head out and make our way to the platform")
    print("")
    typingprint("\033[1;36;40m\nYou take a moment to think of your decision you can either walk on the tracks or stay in the train.")
    print("1: Get out and walk")
    print("2: Stay on the train")
    print("")
    player_answer_ending = input()
    if player_answer_ending == "1":
        typingprint("\033[1;34;40m\nYou walk down the tracks until the next station where there is a an exit.")
        print("")
        typingprint("\033[1;34;40m\nYou say that you'll take a look and step down from the train. You walk along the track and get to the platform")
        print("")
        typingprint("\033[1;34;40m\nYou haul your self up and take a look around you notice some light pouring in as you look up the stairway isn't blocked.")
        print("")
        typingprint("\nYou turn around and shout back to the conductor that the exit isn't blocked. He nods his head and gestures you to go.")
        print("")
        typingprint("\nYou turn around and head towards the stairs as the warm evening air comes into view. You take a deep breath as you smell the fresh air.")
        print("")
        typingprint("\033[1;34;40m\nYou have made it through all those troubles as you think back to the choices you make but then start to wonder how you get home.")
        print("")
        typingprint("\n\033[1;32;40m THANKS FOR PLAYING: THE UNDERGROUND")
        print("|┈┈┈┈┈┈▔╲")
        print("|┈┈┈┈┈┈▏▕")
        print("┈┈┈┈┈┈┈▏▕▂▂▂")
        print("▂▂▂▂▂▂╱┈▕▂▂▂")
        print("▉▉▉▉▉┈┈┈▕▂▂▂")
        print("▉▉▉▉▉┈┈┈▕▂▂▂")
        print("▔▔▔▔▔▔╲▂▕▂▂▂")
        time.sleep(3)
        sys.exit()
    elif player_answer_ending == "2":
        typingprint("\033[1;34;40m\nYou live out the rest of your life on the train. You always wonder what could've been down those tracks I guess we'll never know unless you play again.")
        print("""
              \033[1;31;40m
                                                                                                         
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : : 
                  
              
              """)
        game_over() # ends the game
    else:
        print("Please select 1 or 2")
        ending()

def game_over(): # if the player dies this program is run
    print("""\033[1;37;40m\n
▒▒▒░░░░░░░░░░▄▐░░░░
▒░░░░░░▄▄▄░░▄██▄░░░
░░░░░░▐▀█▀▌░░░░▀█▄░
░░░░░░▐█▄█▌░░░░░░▀█▄
░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
░░░░░▄▄▄██▀▀▀▀░░░░░
░░░░█▀▄▄▄█░▀▀░░░░░░
░░░░▌░▄▄▄▐▌▀▀▀░░░░░
░▄░▐░░░▄▄░█░▀▀░░░░░
░▀█▌░░░▄░▀█▀░▀░░░░░
░░░░░░░░▄▄▐▌▄▄░░░░░
░░░░░░░░▀███▀█░▄░░░
░░░░░░░▐▌▀▄▀▄▀▐▄░░░
░░░░░░░▐▀░░░░░░▐▌░░
░░░░░░░█░░░░░░░░█░░
░░░░░░▐▌░░░░░░░░░█░
    """)
    try_again = input("\033[1;36;40mWould you like to play again? Y or N").lower()
    if try_again == "Y".lower():
        intro() # goes back to the start
    elif try_again == "N".lower():
        print("\033[1;36;40mBetter luck next time") # ends the game
        time.sleep(3)
        sys.exit()
    else:
        print("\033[1;36;40mPlease use Y or N")
        game_over() # player should be using what's stated

start_game() # starts the game