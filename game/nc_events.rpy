label nc_talk(event=False,callrand=False):
    if event == 'first_talk':
        if callrand:
            if callrand > .35 and not nc_after_ft:
                nc "Hello?"
                fp "Hi. Dunno if you remember me..."
                nc "I remember you, [fp]!"
                "You can sense... not hostility... just... sceptisism? in her voice"
                fp "Even remember my name..."
                nc "Don't flatter yourself! Caller ID! Ever heard of it?"
                fp "Right..."
                nc "Dumbass"
                fp "Well, perhaps. I didn't call you out of the blue, though"
                nc "I'm sure you didn't. I don't really give a shit!"
                fp "I..."
                $ calling = duringcall = False
                "{b}beeeeeep...{/b}"
                fp "{i}She hung up on me! The bitch... hung up on me!{/i}"
                fp "{i}Okay... not the best start. Maybe I can figure out a way to get her to talk to me, at least...{/i}"
                $ nc_after_ft = True
                if "You need to figure out a way to get "+nc.name+" to talk to you. Perhaps talk to "+nr.name+" again, see if he knows anything else that might help" not in hints+read_hints+disabled_hints:
                    $ renpy.notify("You need to find a way to get "+nc.name+" to talk to you")
                    $ set_hint("You need to figure out a way to get "+nc.name+" to talk to you. Perhaps talk to "+nr.name+" again, see if he knows anything else that might help")
            else:
                $ calling = duringcall = False
                if nc_after_ft:
                    fp "No answer. No surprise there, after what she did when I called the first time..."
                else:
                    fp "No answer. I guess I'll have to try again later"
        call change_loc(current_location) from _call_change_loc_25

    if event == 'icafe_visit':
        $ settime(20,00)
        if visit_icafe_1:
            $ addtime(False,30)
            "You arrive at [icafe]. Looking around, trying to let your eyes adjust to the dimly lit location, with glowing screens across the interior. Not the easiest place to find someone..."
            "Scanning the room, you try to spot [nc] in the crowd. Not that many girls in here, that you can see, but then half the crowd is wearing hoodies and headphones, making it hard to pinpoint gender"
            "Suddenly, you hear yelling from the far side of the cafe"
            unk_f "{b}Hell to the FUCK no!{/b}"
            unk_m "Listen..."
            unk_f "{b}Shut the FUCK UP!{/b}"
            unk_m "Calm down!"
            unk_f "{b}I will not \"calm down\"! I'm fucking pissed!{/b}"
            "You start heading for the commotion... knowing [nc], this... sorta sounds like her, even though you cannot really remember her voice"
            "When you approach them, they seem to at least have turned down the volume a little bit, but the tension is still palpable"
            "You hang back, trying to figure out if this is both something you want to get involved in, and also if this is even the girl you're looking for"
            "The girl rips off her headphones and throws them on the table, before pulling back the hoodie and releasing a mane of jet black hair"
            unk_f "{b}How the fuck can you manage to be this fucking clumsy, you idiot?{/b}"
            "You can see a laptop on the table, no lights or anything... and then you spot the Jolt-cup... oooooh, you get the anger now. That laptop looks like something in the $2000+ range"
            unk_m "I'm sorry, [nc]! I will get it fixed, I promise..."
            "{b}Score!{/b} You found her!"
            nc "The fuck you will. I'm not letting you anywhere near my laptop, you pathetic piece of shit"
            unk_m "I just wanted to help..."
            nc "Help? What you want is to get hold of my drives. Which would do you no good, since they're encrypted, and the only key is in my head. You would've gotten exactly nowhere!"
            "The guy slinks away without looking back."
            "In the meantime, [nc] seems like she wants to kill someone, and you decide that you really don't wanna be that guy. You decide to come back and talk to her when she's in a slighlty less confrontational mood"
            $ visit_icafe_1 = False
            $ visit_icafe_2 = True
            $ addtime(False,20)
        else:
            fp "I should call [nr] and see if he knows where I might find [nc]..."
        call change_loc(current_location) from _call_change_loc_55

    if event == 'icafe_talk':
        $ addtime(False, 30)
        "You decide to go try to get a hold of [nc]. Hopefully she's calmed down after the accident with her laptop"
        "Arriving at [icafe], slightly earlier in the day this time around, you head to the back, to see if you can find [nc] anywhere"
        fp "{i}There she is...{/i}"
        fp "Hey, [nc]!"
        "She looks a bit startled. If it's just that you suddenly show up, or that you know her name, is up for grabs"
        nc "[fp]... You should really learn to take a hint!"
        fp "Oh, well, I just couldn't stay away! And I figured you were just having a bad day!"
        nc "You figured wrong!"
        fp "Did you get your laptop fixed?"
        nc "My... laptop...? How the fuck did you know my laptop got fried?"
        fp "Well, I was in here looking for you the other day... Found you too, but decided against talking to you. Seemed you were a bit... cross, with whomever the idiot was who spilled on your box"
        nc "Yeah... don't say it like that"
        fp "Huh? Oh, right! \"Your laptop\". Better?"
        nc "Slightly. What do you want?"
        fp "Would you believe me if I said I just wanted to see how you were doing?"
        nc "No, I would not"
        fp "Fine. I'm looking for some help with what I suspect is a hacker-attack on HSS' systems"
        nc "You... suspect a \"hacker attack\"?!? {i}The mirth in her voice is not really endearing...{/i}"
        fp "Yeah, I do. I'm willing to pay, of course. Seems like you could use a new computer?"
        nc "Hm. How much?"
        fp "How much do you need?"
        nc "For a new laptop?"
        fp "Yeah"
        nc "A couple grand should do it"
        if fp_money > 2000:
            fp "No problem"
            "[nc] looks a little perplexed with your seeming indifference to the amount she asked for"
            nc "O... kay. Money up front, then tell me what you need"
            $ nc_owed = 0
            $ visit_icafe_2 = False
            $ visit_icafe_3 = True
            call nc_talk(event='icafe_talk_after_payment')
        else:
            fp "I can't afford that right now"
            nc "Then get back to me when you can"
            "She gets up, and leave you sitting there, a little taken aback by her straight forwardness and boldness"
            fp "{i}2 grand. Holy shit... Where the fuck am I gonna get 2 grand?{/i}"
            $ nc_owed = 2000
            $ visit_icafe_2 = False
            $ visit_icafe_3 = True
        $ addtime(False,30)

    if event == 'icafe_talk_after_payment':
        if nc_owed <= 2000 and nc_owed != 0:
            nc "So, [fp]... you got my cash?"
            if fp_money > nc_owed:
                fp "Yeah, I do..."
            else:
                fp "Well, I got some of it..."
            label give_nc_money():
                menu:
                    "Give [nc] the $[nc_owed]":
                        $ fp_money -= nc_owed
                        $ nc_owed -= nc_owed
                        jump after_money_exchange
                    "How much do you want to give?":
                        python:
                            try:
                                give_cash = int(renpy.input("Input the amount you want to give"))
                                if not isinstance(give_cash,int):
                                    raise ValueError()
                            except ValueError:
                                renpy.say(None,"Please input only numbers")
                                renpy.jump('give_nc_money')
                            else:
                                if fp_money > int(give_cash):
                                    fp_money -= int(give_cash)
                                    nc_owed -= int(give_cash)
                                    renpy.jump('after_money_exchange')
                                else:
                                    "You don't have that much money"
                                    renpy.jump('give_nc_money')
        else:
            label after_money_exchange():
                if not nc_owed:
                    nc "Nice... I should've asked for more"
                    fp "No, you really shouldn't - I don't mind paying, but I refuse to be taken advantage of!"
                    nc "{i}She looks at you with a mischevious glint in her eyes{/i}\nDo you now..."
                    fp "{i}You feel your cheeks turning red...{/i}\nSo... about what I asked you"
                    nc "Yeah... you think someone hacked the school. So, in your expert opinion, how did this happen?"
                    fp "{i}This was a bad idea...{/i}"
                    fp "I'm not an expert. But word from employees at the school is that there are things happening with the school systems that would mean that there is either a hacker somewhere, modifying records, or the system is just so fucked that it messes with records without leaving traces"
                    nc "Hmm... did it mess with you?"
                    fp "What? No!"
                    nc "Then why do you care?"
                    fp "Because... they messed with [fsName.shortname], okay?"
                    nc "Jules... oh, [fsName.yourformal]"
                    fp "Yeah..."
                    nc "Hm, okay - noone messes with family. I can see how that would be a trigger"
                    nc "What do you need?"
                    fp "Well... I would like for you to check out the system. Maybe you can find something, or at least figure out if it's just the system being crappy, or if someone is actually messing with it"
                    nc "I can probably do that... I'm guessing this isn't sanctioned by the school, hm?"
                    fp "Haha. You're funny. The school just wanna sweep this under the rug"
                    nc "Okay, I'm gonna need a bit of time to set this up. Gimme a week or so. I'll contact you via text"
                    $ nc_action_started = 1
                else:
                    nc "You still owe me $[nc_owed]"
                    fp "I know. I was hoping you could perhaps start, and I will get the rest of the..."
                    nc "No!"
                    nc "You need my help, not the other way around. You pay me, up front, and I help. Until you pay, no help"
                    fp "Fine..."

        $ visit_icafe_3 = False
        call change_loc(current_location)

    if event == 'icafe_talk_7_days':
        fp "{i}Now, where is she...{/i}"
        nc "Hey, [fp]!"
        "Jumping a bit, you quickly gather your wits about you again..."
        fp "Uhm... eh... heyu..."
        "Or not..."
        nc "You scare easily"
        "You can hear the grin even though you can't really see her face in the dark cafe"
        fp "Yeah, well... fine, you scared me. You're a scary chick, okay?"
        "[nc] looks a bit taken aback by that statement"
        nc "Well, at least you showed up. I've figured out a couple things, although nothing really conclusive"
        fp "What you got?"
        nc "I did run a few checks on the systems. They're secured with gaffa and safety pins, it'll take the average script kiddie about 2 minutes to get access"
        fp "So what you're saying anyone could've done this?"
        nc "Nah, you didn't let me finish. Access is easy. Getting to do what this guy has done, however, isn't quite as straight forward. Mostly, the system is fairly automated, especially the logs of who does what. Without proper access, you would trigger between 3 and 5 fail-safes"
        fp "But... nothing like that showed up?"
        nc "Exactly! That means that this guy knows what he's doing. Which also means that he didn't really leave much of a trace"
        fp "So... I basically wasted $2000 on you, huh?"
        "Again, she looks at you with contempt"
        nc "I didn't fail. I just didn't find out much. Noone else would be able to find more"
        fp "Easy... did you find anything at all, anything that can be of help?"
        nc "Well... there was one thing. I dunno if it's of any use, but the way I think he got a hold of the info he needed to manipulate the system is sort of a signature for [hj]"
        fp "[hj]? You're kidding now, right?"
        nc "No, I'm not. I know the name is dorky as fuck, but the guy is legit one of the best coders and hackers in the wild. Which sort of makes me wonder why the hell he would bother with this. It's way beneath his usual bravado, and with no obvious gain"
        fp "Yeah, that was sort of one of the things I was wondering about as well. It didn't seem to serve any purpose at all, apart from messing with students"
        fp "Do you know anything about this guy? Where I might find him, or anything useful to track him down?"
        "She looks away for a bit..."
        nc "No... no, not really"
        fp "Oh, come on. You clearly know {b}something(/b}! Tell me!"
        nc "I don't take orders from you. I don't even think I like you. So don't come here and demand information about my... {i}She cuts herself off, before finishing the sentence{/i}"
        fp "Your... wait. [hj] is your... what? Boyfriend?"
        nc "NO! He's just... "
        "She looks flustered... not embarrassed, just... unsure of what she should tell you, maybe?"
        nc "He's a guy I used to hook up with, okay? Then... shit happened, and we had to stop doing that. It's... sorta weird, and not something I wanna share. Okay?"
        fp "Okay, no problem. I don't really care who you bonk, what I do care about is whether or not I can get a hold of him"
        nc "I can probably get him here..."
        fp "Okay. Have him show up, then text me. I can be here in 30 minutes max!"
        nc "I'll text you when I got him"
        "You head out, going back home seems like a good plan for now"
        $ nc_action_started = 1
        call change_loc('outside')

    if event == 'icafe_talk_hj':
        "This is as far as this story goes for now"