# I put the routes inside the while loops to handle in case the user put something else.
# for Showing Creativity and Exceeding Requirements, If you choose "ACCEPT", "CRAFT", "KEEP", "TRUST", "LIE/GIVE" route, you can go to other no linear points on the route map
# (the logic is on line 50 - 60) allowing the user to have until 5 levels of scenarios (just on that route), it is hard to explain in text, but if you look my canva whiteboard you can see it clearly: 
# https://www.canva.com/design/DAGSg4bR-pQ/RCO_FGLyRmc62qYAnV7nXg/edit?utm_content=DAGSg4bR-pQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
# (Focus on the "CRAFT" route)

# Try "ACCEPT", "CRAFT", "KEEP", "TRUST", "LIE/GIVE" to see it

chose = -1

print("\n   You are a citizen of a small village, and your younger sister is gravely ill. Desperate for money to pay the healers, you hear about an ancient Nordic artifact that the king is offering 4,000 gold coins for, which is enough not only to cure your sister but also to live comfortably for the rest of your life.\n\n\
   A close friend of yours tells you about where the artifact is, but he can't accompany you because he must care for his own sick mother. He needs part of the reward to pay for her treatment, just as you do for your sister. However, he offers to watch over your sister while you're away on the quest, promising to split the reward when you return. \n\n\
   You pause for a moment, considering whether to ACCEPT or REJECT his offer.\n")

while chose != 0:    
    chose = input(">> ").upper()

    if chose == "ACCEPT":
        print("\n   You decide to accept his offer. After preparing yourself, you set out on the journey. Days pass, and you finally arrive at a very dark cave. Now, what do you wanna do? CRAFT a torch to light your way, or PROCEED into the darkness, trusting only your hearing?\n")

        while chose != 0:
            if chose != "PROCEED":
                chose = input(">> ").upper()

            if chose == "PROCEED":
                print("\n   You decide to proceed into the darkness. As you carefully navigate the cave, you hear a voice resonate from the shadows. It tells you that it knows your heart and deems you worthy. Moments later, the ancient artifact appears before you, glowing faintly. The voice explains that the artifact holds the power to heal any illness.\n\n   Now, you're faced with a difficult decision: should you LIE to your friend and use the artifact to heal your sister directly, or GIVE the artifact to the king and use the reward to pay for the treatments for both your sister and your friend's mother?\n")

                while chose != 0:
                    chose = input(">> ").upper()

                    if chose == "LIE":
                        print("\n   You decide to return home, but when you meet your friend, you lie, telling him that you couldn't find the artifact. Your friend, though very sad, accepts this and returns home in disappointment. Once alone, you use the artifact to heal your sister, and almost instantly, she is restored to perfect health. Though you feel guilt for deceiving your friend, seeing your sister so full of life makes you question if it matters anymore.")
                        chose = 0
                    
                    elif chose == "GIVE":
                        print("\n   You decide to return home and give the artifact to the king. When he sees it, the king is overjoyed because his wife is gravely ill, too, and he had been searching for a way to save her. In gratitude, he rewards you with 4,000 gold coins, just as promised. You return to the village, split the money with your friend, and pay the healer. Both your sister and your friend's mother fully recover, and peace returns to your lives.")
                        chose = 0

                    else:
                        print("your chose is not valid, try again\n")

            elif chose == "CRAFT":
                print("\n   You take some materials and craft a touch, and then you entered the cave. After searching the cave for what feels like hours, you come up empty-handed. Frustration starts to set in. Now, you have to decide: do you RETURN to the village and give up, or KEEP searching, hoping the artifact is hidden somewhere deeper?\n")

                while chose != 0 and chose != "PROCEED":
                    if chose != "RETURN":
                        chose = input(">> ").upper()

                    if chose == "KEEP":
                        print("\n   Exhausted and starving, you push yourself to keep searching for the artifact. After what feels like an eternity, you found some ancient writings on the cave wall that says, 'Trust in the dark.', under the message, you notice a small pool of water. Doubt fills your mind, can you really TRUST this message? Or should you abandon the quest and RETURN home before it's too late?\n")


                        while chose != 0 and chose != "PROCEED" and chose != "RETURN":
                            chose = input(">> ").upper()

                            if chose == "TRUST":
                                chose = "PROCEED"

                            elif chose == "RETURN":
                                chose

                            else:
                                print("your chose is not valid, try again\n")
                    
                    elif chose == "RETURN":
                        print("\n   You return home empty-handed, a deep sadness comes to you as you see your sister and your friend waiting for you. Time passes, and despite your best efforts, your sister’s condition worsens day by day. Eventually, the illness overcomes her, and she quietly passes away, leaving a void in your heart that nothing could fill.")
                        chose = 0
                    
                    else:
                        print("your chose is not valid, try again\n")

            else:
                print("your chose is not valid, try again\n")

    elif chose == "REJECT":
        print("\n   You decide the journey is too risky and choose to stay with your sister. One day, a healer visits the village, but you don't have the money to pay for his services. Now, you face a difficult choice: will you BEG him for help or THREATEN him to heal your sister?\n")

        while chose != 0:
            chose = input(">> ").upper()

            if chose == "BEG":
                print('\n   You beg the healer for help, but he refuses to assist without something in return. "I have my own needs to take care of," he says. "What do you have to offer me?" You pause, thinking carefully. The only thing of value you possess is a necklace passed down from your grandmother, and it is super precious for both you and your sister. The decision weighs heavily on you.\n\n   Now, you must choose: do you offer the NECKLACE to him, say you have NOTHING and continue begging for mercy, or offer YOURSELF as his helper in exchange for his services?\n')
                
                while chose != 0:
                    chose = input(">> ").upper()

                    if chose == "YOURSELF":
                        print("\n   Desperate to save your sister, you offer yourself in exchange for her treatment. The healer agrees, and after casting a series of powerful spells, your sister is restored to full health. As promised, you begin following the healer, serving as his apprentice. Over the months, he teaches you the art of healing, and under his guidance, your skills flourish. In time, you become a renowned healer yourself, standing proudly by the side of your master.")
                        chose = 0

                    elif chose == "NOTHING":
                        print("\n   You tell the healer that you have nothing of value to offer him. Tears falls down your face as you beg, pleading for him to help your sister. Moved by your sincerity and desperation, the healer's expression softens. He decides to help and after casting a series of powerful spells, your sister is restored to full health. You and your sister thank him from the bottom of your hearts, overwhelmed with gratitude for his compassion and kindness.")
                        chose = 0

                    elif chose == "NECKLACE":
                        print("\n   After a moment of hesitation, you decide to offer the healer your grandmother's necklace. It carries deep sentimental value for you and your sister, but saving her life matters more than anything. The healer examines the necklace and, after a pause, agrees to the exchange.\n\n   After casting a series of powerful spells, your sister is restored to full health. Although you feel the weight of losing it, you're grateful that your sister is alive. Both of you thank the healer, but a part of you can't help but mourn the loss of something so meaningful.")
                        chose = 0

                    else:
                        print("your chose is not valid, try again\n")
            
            elif chose == "THREATEN":
                print('\n   Frustrated and desperate, you grab a knife and demand that the healer treat your sister. "If you do not help her, I will make sure you regret it" you threaten. The healer hesitates but reluctantly agrees to avoid conflict. After casting powerful spells, your sister is restored to health, but the healer looks at you with resentment, leaving you with an uneasy feeling. You achieved your goal, but at what cost? Guilt overwhelms you as you consider how to repair the damage: will you offer to WORK for the healer to pay off your debt or just APOLOGIZE  for your actions and seek to mend the relationship?\n')

                while chose != 0:
                    chose = input(">> ").upper()

                    if chose == "WORK":
                        print("\n   As promised, you begin following the healer, serving as his apprentice for a while, but over the time, he starts teaching you the art of healing, and under his guidance, your skills flourish. In time, you become a renowned healer yourself, standing proudly by the side of your master.")
                        chose = 0

                    elif chose == "APOLOGIZE":
                        print('\n   You decide to apologize to the healer and explain your story. He listens intently, and after you finish, he responds with understanding. "You could have just told me everything," he says. "I would have helped you." You feel a mix of guilt for your earlier actions and relief that your sister is healthy again.')
                        chose = 0
                    
                    else:
                        print("your chose is not valid, try again\n")
            
            else:
                print("your chose is not valid, try again\n")

    else:
        print("your chose is not valid, try again\n")

print("\nTHE END\n")