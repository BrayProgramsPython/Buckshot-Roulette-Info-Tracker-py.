while True:
    print("NEW GAME")
    numRounds = int(input("Enter num of rounds (1-3): "))
    currentRound = 1

    setup_Left = int(input("Type 0 for player left or 1 to skip: "))
    setup_Right = int(input("Type 0 for player right or 1 to skip: "))
    setup_Across = int(input("Type 0 for player across or 1 to skip: "))
    
    while currentRound <= numRounds:
        print("Round",currentRound,"/",numRounds)
        
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
            
        while True:
            rise = 1
            ask_burner = True
            print("RELOAD")
            live = int(input("Enter num live: "))
            blank = int(input("Enter num blank: "))
            fall = live + blank
            while fall > 10 or fall < 1:
                print("Must be 1-10: ")
                live = int(input("Enter num live: "))
                blank = int(input("Enter num blank: "))
                fall = live + blank

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

            while live != 0 or blank != 0:
                if fall < 1:
                    break

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
                
                racked = True
                while racked == True:
                    keep_healing = True
                    while keep_healing == True:
                        heal = input("Did anyone heal? (left, right, across, self, or no): ")
                        if heal == 'left':
                            player_Left += 1
                        elif heal == 'right':
                            player_Right += 1
                        elif heal == 'across':
                            player_Across += 1
                        elif heal == 'self':
                            self += 1
                        elif heal == 'no':
                            keep_healing = False
                    
                    if ask_burner:
                        burnNum = int(input("Enter burner shell num or 0 to skip: "))
                        if burnNum >=1 and burnNum <= 10:
                            burnShell = input("Enter burner shell type: ")
                            ask_burner = False
                        elif burnNum < 0 or burnNum > 10:
                            burnNum = int(input("Enter burner shell NUM or ZERO to skip: "))
                            burnShell = input("Enter burner shell type (live/blank): ")
                            ask_burner = False
                        
                    fired_racked = input("Type f for fired or r for racked: ")
                    fire = input("enter shell fired/racked (live/blank): ")
                    if fire == 'live' and fired_racked == 'f':
                        racked = False
                        live -= 1
                        rise += 1
                        fall -= 1
                        live_inv = int(input("Type 1 for live inverted or 0 for no invert: "))
                        if live_inv == 0:
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
                                print("--------------------")
                                print("")
                                racked = True
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
                                print("--------------------")
                                print("")
                                racked = True
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
                        print("--------------------")
                        print("")
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
                        print("--------------------")
                        print("")

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

                if self <= 0:
                    print("YOU DIED - ROUND OVER")
                    break
                if player_Left == 0 and player_Right == 0 and player_Across == 0:
                    print("ROUND WON")
                    break
            if self == 0 or (player_Left == 0 and player_Right == 0 and player_Across == 0):
                currentRound += 1
                break
