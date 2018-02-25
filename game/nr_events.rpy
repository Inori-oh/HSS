label nr_talk(event=False):
    if event == 'nr_intro':
        $ hacker_3 = False
        "You decide to call [nr] to see if he's free to hang out"
        fp "Hey, [nr]"
        nr "Hey [fp]! What's up?"
        fp "Well... I have a couple things to run by you, was wondering if you could drop by? If not tonight, then tomorrow?"
        $ text = "Sure. {0}".format("I can be there in 15" if int(current_time[:2]) > 20 else "It's a bit late, but I can drop by tomorrow? Say around 19:00?")
        nr "[text]"
        fp "Cool. I'll be in the garage, so just meet me there"
        $ text = "Okay. See you {0}".format('soon' if int(current_time[:2]) > 20 else 'tomorrow')
        nr "[text]"
        $ hacker_4 = True
        call change_loc(current_location)

    if event == 'nr_first_visit':
        if current_location != 'garage':
            call change_loc('garage',sec_call='nr_first_talk')
        label nr_first_talk(True):
            nr "Hey, [fp]!"
            fp "Hey!"
            fp "{i}You're trying to figure out how to tell [nr] about the hacker, or whatever it is going on at school, preferably without dragging [fsName.yourformal] into it...{/i}"
            nr "Hey, how's [fsName.Name] doing?"
            fp "{i}Oh, right... [nr] did have... or maybe the right phrasing is \"have\" a thing for [fsName.Name]{/i}"
            fp "What's it to you?{i}You have a slight mocking tone that you don't really mean to use, but still...{/i}"
            nr blushing "Oh, well... uhm... I was just wondering! Nevermind..."
            "[nr] is looking like he wouldn't mind sinking through the floor right now"
            fp "She's fine. Actually, she's sort of... part of the reason why I wanted to talk to you"
            nr -blushing "Oh? {i}You can almost see his interest peaking{/i}"
            fp "She doesn't know I'm talking to you, and no, it's nothing like that. Chill!"
            nr "Oh... {i}He deflates, visibly{/i}"
            fp "Help me with this, and perhaps she'll remember you exist, at least"
            nr "That would be... cool, I guess. What's up?"
            "{i}You spend a bit of time telling [nr] about what happened with [fsName.name], and what [scn] told you{/i}"
            nr "Wow... that's actually... wow. What can I do?"
            fp "Well, I know you know about all this, so I was hoping you could figure something out..."
            nr "I'm gonna stop you right there. Yeah, I know computers, but I'm no genius hacker, or even a script-kiddie. I don't know jack about this shit"
            fp "Oh. {i}Crap, there goes that idea{/i}"
            nr "But I do know people who could probably shed some light on this. Problem is getting them to help"
            fp "Anyone you know-know, or just people on the www?"
            nr "First off... don't call it the www. You sound like a dumbass!"
            nr "Second, I do know someone. As in, personally"
            fp "That's grea..."
            nr "Third, she's never gonna help"
            fp "\"She\"?!? Are you serious?"
            nr "Yes...? Girls can play with computers too, you know"
            fp "Yes yes, I know that. Just... didn't expect you to know a girl who could hack. Didn't expect you to know {b}any{/b} girls, really"
            nr "Haha"
            fp "Kidding, but... why won't she help?"
            nr "Well, I said I know her, but... we're not really talking"
            fp "What did you do?"
            nr "Why is your first goto \"What did you do?\""
            fp "Because I know you. I've known you for nearly 10 years now. Chances are, you're the one that fucked up"
            nr "... yeah, I did"
            fp "{b}What{/b} exactly did you do?"
            nr "I... took her best friend on a date... and sort of... hooked up with her"
            fp "... okay... that explains that..."
            fp "Damn, you're an asshole sometimes"
            nr "No shit, Sherlock!"
            fp "Wait... are you talking about [nc]?"
            nr "Got it in one!"
            fp "Oh, you dumb fuck"
            nr "I know that!"
            fp "Do you still have her number, email... address? Anything?"
            nr "Yeah... I think so. At least something she used last year or so"
            fp "Text it to me, okay? Even though she doesn't wanna talk to you, she might still talk to me"
            nr "Sure. Wouldn't count on it, though... you know me, hence you're by extension the enemy"
            fp "Great..."
            $ text = "You turn your conversation to the bike standing in the middle of the garage, in pieces. After spending a few hours working on the bike, you decide to {0}".format('have a few beers to end the night' if backpack.has_item(beer_item) else 'call it a night')
            "[text]"
            if "You need to wait for "+nr.name+" to send you "+nc.name+"'s info" not in hints+read_hints+disabled_hints:
                $ hints.append("You need to wait for "+nr.name+" to send you "+nc.name+"'s info")
            $ text_msg_received.append(('nr',nr,"The number for "+nc.name+" is "+nc_number+""))
            call change_loc(current_location,loctrans=True)
