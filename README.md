# Buckshot-Roulette-Info-Tracker-py.
A program that helps you keep track of all the information you need to in buckshot roulette. If you have bad short term memory, this is for you!

This is a program that will help you track the following:
1. how many shells are left
2. What type of shells are left
3. which shell number rising and falling you are on (for burner phone)
4. Max HP and player HP's (for when someone is skipped and you need to know wether to double damage them or not)

This is the earliest release of this program. It has been in testing for quite some time and now I need other players to tell me what they think of it. You can run it either directly through python or through your computer's terminal, however you will need to download the code as well as install python for it to work.

Development Roadmap for BRIT
5/31/26 - Earliest Release for playtesting
?/?/? - Improvments made based on player feedback
?/?/? - Program altered to functions for quicker and simplier use (will do if this gets popular enough)

How to use:
For best use, have 2 monitors or have buckshot roullete windowed and allowing room for the program.
Each prompt will give examples of what to type, but I will break it down here aswell. CASE SENSITIVE!
1. enter the number of rounds (1-3) as a number, not spelled
2. register players in your game in this order: left, right, across (press 0 to register, 1 to skip if no one is there)
3. 1st round starts, enter max HP, as a number
4. enter the number of live shells, as a number
5. enter the number of blank shells, as a number
6. Info block prints
7. Enter if anyone left the game, based on positions ("left", "right", "across", or "no" if no one left)
8. enter if anyone healed (same inputs as previous, but including "self") this question is asked until you say "no" incase someone heals more than once
9. enter burner shell number (if you use burner, enter the shell number as a number, or press 0 if no burner)
10. enter burner shell type (only asked if you entered anything but 0, type "live" or "blank")
11. enter if gun was fired or racked ("f" for fired, "r" for racked)
12. no matter of fired or racked, enter shell type ("live" or "blank")
13. if fired, enter if inverted ("1" for invert, "0" for no invert)
14. if live or inverted blank, enter targeted player ("left", "right", "across", "self")
15. enter amount of damage ("1" or "2")
16. for racked shells, the shell type you enter should be whatever the gun was originally, so keep track of inverts
17. info block prints differently depending on if fired or racked
18. Everything above will cycle until the gun is empty, then returns to the shell amount entering
19. after your hp or everyone else's hp hits zero, advances to next round and returns to max hp entering
20. after your hp or everyone else's hp hits zero AND the round counter is maxed, program ends
