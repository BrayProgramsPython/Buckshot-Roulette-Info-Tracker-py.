#Program to keep track of information in BR

while True:
#Loops program for game ends/starts
    print("NEW GAME")
    numRounds = int(input("Enter num of rounds (1-3): "))
    currentRound = 1
    #Dictates when the program will loop back to "NEW GAME" based on user input

    setup_Left = int(input("Type 0 for player left or 1 to skip: "))
    setup_Right = int(input("Type 0 for player right or 1 to skip: "))
    setup_Across = int(input("Type 0 for player across or 1 to skip: "))
    #dictates what players will be displayed on info block and counted towards round endings bsaed on user input
    
    while currentRound <= numRounds:
        print("Round",currentRound,"/",numRounds)
        #loops the rounds based on when user health or enemy healths hit 0, dictates return to "NEW GAME"
        
        player_Left = 0
        player_Right = 0
        player_Across = 0
        self = 0
        maxHP = int(input("Enter max HP: "))
        self += maxHP
        if setup_Left == 0:
            player_Left += maxHP
        if setup_Right == 0:
            player_Right += maxHP
        if setup_Across == 0:
            player_Across += maxHP
            #tracks max hp for the current round for whatever players were entered above
            
        while True:
            rise = 1
            print("RELOAD")
            #loops questions for info based on shell count left, starts rise counter and enables burner question
            live = int(input("Enter num live: "))
            blank = int(input("Enter num blank: "))
            fall = live + blank
            ask_burner = True
            #enters number of lives and blanks, starts fall counter based on total shells
            while fall > 10 or fall < 1:
                print("Must be 1-10: ")
                live = int(input("Enter num live: "))
                blank = int(input("Enter num blank: "))
                fall = live + blank
                #error trap for previous block

            print("")
            print("--------------------")
            print("live:",live)
            print("blank:",blank)
            print("Shell # rising:",rise)
            print("Shell # falling:",fall)
            print("Max HP:",maxHP)
            if setup_Left != 1:
                print("Player left HP:",player_Left)
            if setup_Right != 1:
                print("Player right HP:",player_Right)
            if setup_Across != 1:
                print("Player across HP:",player_Across)
            print("Self HP:",self)
            print("--------------------")
            print("")
            #info block dispalying shell types, counts, numbers, and hps,

            while live != 0 or blank != 0:
                if fall < 1:
                    break
                    #loops questions for each players turn, based on shell counts

                leave = input("Did anyone leave? (left, right, across, no): ")
                if leave == 'left':
                    player_Left = 0
                    setup_Left = 1
                elif leave == 'right':
                    player_Right = 0
                    setup_Right = 1
                elif leave == 'across':
                    player_Across = 0
                    setup_Across = 1
                if player_Left == 0 and player_Right == 0 and player_Across == 0:
                    print("GAME END - NOT ENOUGH PLAYERS")
                    break
                    break
                    #Checks if anyone leaves, if so removes them from counters, ends game if all enemies leave
                
                racked = True
                while racked == True:
                    keep_healing = True
                    while keep_healing == True:
                        heal = input("Did anyone heal? (left, right, across, self, or no): ")
                        if heal == 'left' and setup_Left == 1:
                            print("No player left")
                        elif heal == 'left' and player_Left == maxHP:
                            print("Player left already max HP")
                        elif heal == 'left':
                            player_Left += 1
                        if heal == 'right' and setup_Right == 1:
                            print("No player right")
                        elif heal == 'right' and player_Right == maxHP:
                            print ("Player right already max HP")
                        elif heal == 'right':
                            player_Right += 1
                        if heal == 'across' and setup_Across == 1:
                            print("No player across")
                        elif heal == 'across' and player_Across == maxHP:
                            print("Player across already max HP")
                        elif heal == 'across':
                            player_Across += 1
                        elif heal == 'self' and self == maxHP:
                            print("You are already max HP")
                        elif heal == 'self':
                            self += 1
                        elif heal not in ['left', 'right', 'across', 'self', 'no']:
                            print("ENTER LEFT, RIGHT, ACROSS, SELF, OR NO")
                        elif heal == 'no':
                            keep_healing = False
                            #Loops healing incase someone heals multiple times, prevents heal input if player is full hp or not in the game, error traps bad input, and ends loop when "no"
                    if fall > 2:
                        if ask_burner:
                            burnNum = int(input("Enter burner shell num or 0 to skip: "))
                            if burnNum >=1 and burnNum <= 10:
                                burnShell = input("Enter burner shell type: ")
                                ask_burner = False
                                #enters burner number and type, registers for later info display
                            elif burnNum < 0 or burnNum > 10:
                                burnNum = int(input("Enter burner shell NUM or ZERO to skip: "))
                                burnShell = input("Enter burner shell type (live/blank): ")
                                ask_burner = False
                                #error trap for previous block
                        
                    fired_racked = input("Type f for fired or r for racked: ")
                    while True:
                        fire = input("enter shell fired/racked (live/blank): ")
                        if fire == 'live' and live == 0:
                            print("Live already zero, entering blank")
                            fire = 'blank'
                            break
                        elif fire == 'blank' and blank == 0:
                            print("Blank already zero, entering live")
                            fire = 'live'
                            break
                        elif fire in ['live', 'blank']:
                            break
                        elif fire not in ['live', 'blank']:
                            print("Enter LIVE or BLANK")
                        
                    if fire == 'live' and fired_racked == 'f':
                        racked = False
                        live -= 1
                        rise += 1
                        fall -= 1
                        live_inv = int(input("Type 1 for live inverted or 0 for no invert: "))
                        if live_inv == 0:
                            target = input("Enter targeted player (left, right, across, self): ")
                            if target == 'left' and player_Left == 0:
                                    print ("Player Left already dead")
                                    target = input("Enter targeted player (left, right, across, self): ")
                            elif target == 'right' and player_Right == 0:
                                    print ("Player Right already dead")
                                    target = input("Enter targeted player (left, right, across, self): ")
                            elif target == 'across' and player_Across == 0:
                                    print ("Player Across already dead")
                                    target = input("Enter targeted player (left, right, across, self): ")
                            damage = int(input("Type 1 for single damage. 2 for double damage: "))
                            if target == 'left':
                                player_Left -= damage
                            elif target == 'right':
                                player_Right -= damage
                            elif target == 'across':
                                player_Across -= damage
                            elif target == 'self':
                                self -= damage
                                #checks if fired or racked, ensures correct type is entered and error traps bad input, if live, adjusts counter and checks for invert. Then asks for target and damage, adjusts target health, and asks again if target already dead
                        elif live_inv == 1:
                            skip = input("Was blank shot at shooter? (y/n): ")
                            if skip == 'y' and live == 0 and blank == 0:
                                break
                                break
                            elif skip == 'y':
                                print("")
                                print("--------------------")
                                print("live:",live)
                                print("blank:",blank)
                                print("Shell # rising:",rise)
                                print("Shell # falling:",fall)
                                if burnNum == rise and burnNum == fall:
                                    print("Shell",burnNum,burnShell,"100%")
                                elif burnNum == rise or burnNum == fall:
                                    print("Shell",burnNum,burnShell,"50/50")
                                print("--------------------")
                                print("")
                                racked = True
                                #if live inverted, checks for turn skip and breaks loop if gun empty, then prints smaller info block because of no damage
                    elif fire == 'blank' and fired_racked == 'f':
                        racked = False
                        blank -= 1
                        rise += 1
                        fall -= 1
                        blank_inv = int(input("Type 1 for blank inverted or 0 for no invert: "))
                        if blank_inv == 1:
                            target = input("Enter targeted player (left, right, across, self): ")
                            damage = int(input("Type 1 for single damage or 2 for double damage: "))
                            if target == 'left':
                                player_Left -= damage
                            elif target == 'right':
                                player_Right -= damage
                            elif target == 'across':
                                player_Across -= damage
                            elif target == 'self':
                                self -= damage
                                #check if blank is fired, adjusts counters and check for inversion. If inverted, gets target and damage and adjusts health
                        elif blank_inv == 0:
                            skip = input("Was blank shot at shooter? (y/n): ")
                            if skip == 'y' and live == 0 and blank == 0:
                                break
                                break
                            elif skip == 'y':
                                print("")
                                print("--------------------")
                                print("live:",live)
                                print("blank:",blank)
                                print("Shell # rising:",rise)
                                print("Shell # falling:",fall)
                                if burnNum == rise and burnNum == fall:
                                    print("Shell",burnNum,burnShell,"100%")
                                elif burnNum == rise or burnNum == fall:
                                    print("Shell",burnNum,burnShell,"50/50")
                                print("--------------------")
                                print("")
                                racked = True
                                #checks if blank fired, asks if shot at shooter for turn skip, breaks loop to return to questions and prints small info block because of no damage
                    elif fire == 'live' and fired_racked == 'r':
                        live -= 1
                        rise += 1
                        fall -= 1
                        if blank <= 0 and live <= 0:
                            break
                        print("")
                        print("--------------------")
                        print("live:",live)
                        print("blank:",blank)
                        print("Shell # rising:",rise)
                        print("Shell # falling:",fall)
                        if burnNum == rise and burnNum == fall:
                            print("Shell",burnNum,burnShell,"100%")
                        elif burnNum == rise or burnNum == fall:
                            print("Shell",burnNum,burnShell,"50/50")
                        print("--------------------")
                        print("")
                        #checks if live racked, if so adjusts counters and prints small info block because no damage
                    elif fire == 'blank' and fired_racked == 'r':
                        blank -= 1
                        rise += 1
                        fall -= 1
                        if live <= 0 and blank <= 0:
                            break
                        print("")
                        print("--------------------")
                        print("live:",live)
                        print("blank:",blank)
                        print("Shell # rising:",rise)
                        print("Shell # falling:",fall)
                        if burnNum == rise and burnNum == fall:
                            print("Shell",burnNum,burnShell,"100%")
                        elif burnNum == rise or burnNum == fall:
                            print("Shell",burnNum,burnShell,"50/50")
                        print("--------------------")
                        print("")
                        #checks if blank and racked, if so adjusts counters and prints small info block because no damage

                print("")
                print("--------------------")
                if live > 0 or blank > 0:
                    print("live:",live)
                    print("blank:",blank)
                    print("Shell # rising:",rise)
                    print("Shell # falling:",fall)
                    if burnNum == rise and burnNum == fall:
                        print("Shell",burnNum,burnShell,"100%")
                    elif burnNum == rise or burnNum == fall:
                        print("Shell",burnNum,burnShell,"50/50")
                print("Max HP:",maxHP)
                if setup_Left != 1:
                    print("Player left HP:",player_Left)
                if setup_Right != 1:
                    print("Player right HP:",player_Right)
                if setup_Across != 1:
                    print("Player across HP:",player_Across)
                print("Self HP:",self)
                print("--------------------")
                print("")
                #full info block printed when someone takes damage. Displays shell count, type, number, burner info, and hps

                if self <= 0:
                    print("YOU DIED - ROUND OVER")
                    break
                    #checks if user dies to loop to next round
                if player_Left == 0 and player_Right == 0 and player_Across == 0:
                    print("ROUND WON")
                    break
                    #checks if enemies die to loop to next round
            if self == 0 or (player_Left == 0 and player_Right == 0 and player_Across == 0):
                currentRound += 1
                break
                #initiates the loop break for new rounds based on previous 2 blocks
