label night_events():

    label end_of_day(end_called=False):
        if end_called or end_cfs:
            $ end_called = end_cfs = False
            hide jules
            hide anne
            hide nk_standing
            with dissolve
            $ nh = format(int(night[renpy.random.randint(0,(len(night)-1))]),"02d")
            $ nm = format(renpy.random.randint(00,59),"02d")
            $ settime(nh,nm)
            $ first_day = False
            if int(nh) in xrange(2,6,1):
                $ overslept = True
                $ overslept_time = int(nh)
            if int(current_time[:2]) in xrange(0,6,1):
                $ day_week = 0 if day_week == 6 else day_week+1
                if current_month_day == months_days[current_month][1]:
                    $ current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                    $ current_month_text = months_days[current_month][0]
                    $ current_month_day = 1
                else:
                    $ current_month_day += 1
                    $ day_ahead = True
            call fp_bedroom_scene from _call_fp_bedroom_scene
            "This ends the day"
            call sleep_the_night(True) from _call_sleep_the_night

    label sleep_the_night(stn_called=False):
        if stn_called or stn_cfs:
            $ stn_called = stn_cfs = False
            if int(current_time[:2]) not in night:
                menu:
                    "Sleep the day away":
                        call sleeping_day_away(True) from _call_sleeping_day_away
                    "Stay up":
                        call fp_bedroom_loc(True) from _call_fp_bedroom_loc
            else:
                menu:
                    "Go to sleep":
                        call sleeping(True) from _call_sleeping
                    "Stay up a bit longer":
                        call fp_bedroom_loc(True) from _call_fp_bedroom_loc_1

    label sleeping(sle_called=False):
        if sle_called:
            $ sle_called = False
            if dream_event:
                if dreameventsChars:
                    $ randomDreamEvent = renpy.random.choice(dreameventsChars)
                    show dreamintro
                    if randomDreamEvent == 'fs':
                        show fs_dream with flash                        
                        if fs_dream_event == 1:
                            show fp_fs_dream_1_1
                            fs "Hey, [fp]! Come to look, or join in?"
                            "You stare a bit at the inviting view before you"
                            menu:
                                "Uhm... join in!?":
                                    $ fs_dream_event = 0
                            fs "Thought so! Get over here!"
                            "[fsName.yourFormal] drags you closer, and tears off your boxers"
                            show fp_fs_dream_1_2
                            fs "Mmmmhm... you look hot, [fp]"
                            fp "Thanks, I guess?"
                            "You're not entirely sure what's going on, but you decide to just go with the flow"
                            show fp_fs_dream_1_3
                            fs "Uh..uh..."
                            fp "Oh, that feels good [fsName.informal]"
                            "..."
                            "..."
                            fp "If you keep doing that, I'm... I'm... CUMMING!"
                            show fp_fs_dream_1_4 with cumflash
                        elif fs_dream_event == 2:
                            show fp_fs_dream_2_1
                            fs "Hey, I missed you! ... and you hard dick!"
                            fs "Now, you just lay back, and let me do all the work, mkay?"
                            fp "Mkay..."
                            show fp_fs_dream_2_2
                            "You stretch out on the bed, spreading your legs to accomodate [fsName.yourformal]"
                            show fp_fs_dream_2_3
                            "[fsName.yourformal] crawls closer to you, and starts licking your rock hard member"
                            show fp_fs_dream_2_4
                            if fp_sex_pref in ["BJ", "Pussy"]:
                                show fp_fs_dream_2_5_1
                                "Working her way up onto the bed, she keeps licking and kissing your cock as long as she can manage, before settling on top of you"
                                show fp_fs_dream_2_5_2
                            elif fp_sex_pref == "Anal":
                                show fp_fs_dream_2_5_1
                                "Slowly crawling closer, she starts licking and kissing your cock. While this is pleasant enough, you decide to push her a bit further, and lift your legs, and cock an eyebrow towards her"
                                show fp_fs_dream_2_5_3
                                "She settles in, and starts rimming you"
                                show fp_fs_dream_2_5_4
                    elif randomDreamEvent == 'fm':
                        show dreamintro
                        show fm_dream with flash
                    elif randomDreamEvent == 'nc':
                        show dreamintro
                        show nc_dream with flash
                    elif randomDreamEvent == 'nk':
                        show dreamintro
                        show nk_dream with flash
                    elif randomDreamEvent == 'nb':
                        show dreamintro
                        show nb_dream with flash
                    elif randomDreamEvent == 'sn':
                        show dreamintro
                        show sn_dream with flash
                    show dreamoutro                        
            if not day_ahead:
                $ current_day_of_the_week_3 = day_week
                $ day_week = 0 if day_week == 6 else day_week+1
                $ current_day_of_the_week_1 = day_week
                $ thishappened_1 = "if"
                if current_month_day == months_days[current_month][1]:
                    $ current_month = 0 if int(current_month) == 11 else (int(current_month) + 1)
                    $ current_month_text = months_days[current_month][0]
                    $ current_month_day = 1
                else:
                    $ current_month_day += 1
                    $ current_day_of_the_week_2 = day_week
                    $ thishappened_2 = "else"
            $ after_sleep = True
            $ day_ahead = False
            if filth_val:
                $ filth_val += 10
            jump day_start

    label sleeping_day_away(sld_called=False):
        if sld_called:
            $ sld_called = False
            $ settime(22,False)
            call fp_bedroom_loc(True) from _call_fp_bedroom_loc_2

