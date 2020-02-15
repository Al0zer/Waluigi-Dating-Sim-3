
style default:
    line_spacing 5
    line_leading 2

define m = Character(("Maria"), color="#f79b9b")
define b = Character(("Bob"), color = "#cf7ac2")
define w = Character(("Waluigi"),color ="#a486d9")
define t = Character(("Prof. Nook"), color = "#80d968")

define slowdissolve = Dissolve(1.0)
define fastdissolve = Dissolve(0.2)

##FIRST SCENE
label start:
    play music "accumula.mp3"

    scene black

    python:
        name = renpy.input("Enter your name")
        name = name.strip()

    define n = Character(("[name]"), color = "#86d5d9")
    $love = 6
    $tennis = False
    $crying = False
    $munkey = False


    "Today marks the start of a new chapter of my life: university"
    "But not just any university..."

    scene campus_main
    with slowdissolve

    "WESTERN UNIVERSITY, the famous party school of southwestern Ontario"
    "I have no idea what to expect, but I know one thing for sure..."
    "Coming to this school, my life will never be the same... for better or for worse "

    scene elgin
    with slowdissolve

    "And this is my residence, my new home away from home"
    "I wonder what kind of crazy shenanigans I'll get up to living here"
    "Well, I guess I should meet my roommates"

    scene dorm
    with slowdissolve

    "Looks like my roommates are already here"
    "This one... kind of looks like a female Mario??"
    "Whatever, I won't judge"
    show maria2
    with fastdissolve
    n "Hi, I'm your roommate, [name]! Nice to meet you"
    m "..."
    n "..."
    m "..."

    "Maybe she didn't hear me?"

    menu:
        "Say 'hello' again, but louder":
            jump louder
        "Say nothing and just stand there like an awkward person":
            jump awkward

    label louder:
        n "HELLO!!!!!!!!!!!"
        show maria2shock
        m "AH!!"
        n "CAN YOU HEAR ME?"
        hide maria2shock
        show maria2mad
        m "STOP SHOUTING, WHAT THE HELL??"
        n "Sorry, I said hello earlier but you didn't hear me..."
        m "No, I DID hear you, I just chose to ignore you!"
        n "What?? Why?"
        m "I don't talk to ugly people... >:/"
        hide maria2mad
        n "Sigh... fair"
        n "Hey, hold on a minute... you look familliar"
        n "Have I met you somewhere before?"
        show maria2mad
        m "Umm... no, wtf??"
        m "Are you crazy or something?"
        n "My bad then, I must've mistaken you for someone else"
        hide maria2mad
        m "Someone crazy obsessed with a lanky purple man, who forced a random bystander to gain information about him in order to win his love?"
        m "Which may or may not have been in the form of a very rushed dating simulator??"
        n "What?"
        m "What?"

        hide maria2
        with fastdissolve

        jump next_roommate


    label awkward:
        n "..."
        m "..."

        "Um... are you sure you don't want to say anything?"

        menu:
            "Yes, I'm staying silent":
                jump more_awkward

            "No, I'll speak up":
                jump louder

        label more_awkward:
            n "..."
            m "..."

            "She's... really not going to say anything dude..."

            menu:
                "I don't care, I'm not saying anything":
                    jump way_too_awkward

                "Yeah, I should probably say something":
                    jump louder

            label way_too_awkward:
                n "..."
                m "..."

                scene black
                with fade
                "So we both just stood there in silence, not saying a word"
                "I did not move a muscle, nor did she"
                "It's been 10 years now... where did the time go?"
                "I should've just said something..."
                "AWKWARD SILENCE END!"

                return

    label next_roommate:
        "Um... okay then"
        "She's quite the character, I'll say that"
        "I just hope the other one is... less of a character"

        n "Hi, nice to meet you, I'm [name]"
        show bob
        with fastdissolve
        b "Wuuuuz poppppinnnn gamer :3"
        "I... don't even know how to respond"
        menu:
            "Get out of this weird conversation":
                jump leave
            "Attempt to save the conversation":
                jump save

        label leave:
            n "I... uh... sorry, I gotta go"
            n "I need to go... fix my fridge"
            n "My fridge is... broken..."
            hide bob
            show bobshock
            b "Oh, that happened to me once."
            b "It was so weird, my fridge started heating up my food!"
            show maria2mad at left
            show bobshock at right
            with fastdissolve
            m "That's because you were putting your food in the oven, Bob..."
            hide bobshock
            hide maria2mad
            with fastdissolve
            jump meet_wah

        label save:
            n "Haha yeahhh... it's popping all right."
            hide bob
            show bobhappy
            b ":)"
            "How do you even say ':)' out loud?!?!??!?"
            hide bobhappy
            with fastdissolve
            jump meet_wah

    label meet_wah:
        "Well... my roommates are absolutely crazy"
        "This is just great. I haven't even been here for an hour and I already hate it!"
        "What other hooligans are going to show up here, huh??"

        scene black
        with fade

        play music "Tacostand.mp3"
        "And then... something amazing happened"
        "I'm not even sure how to describe it, but it felt like a dream"
        "First, I felt a light breeze coming from outside of our dorm"
        "Suddenly, flower petals began floating gently in the wind"
        "Where was this wind coming from?? We're indoors and the windows are closed"
        "Before I could question anything else, I saw... him"
        "Standing before us, a sight so beautiful, it could bring tears to your eyes"

        scene waluigicard
        with slowdissolve
        w "WAAAAAAAAAAAAAAAAAAAAAAAAH"
        w "Hello my fellow frosh, I'm WALUIGI, your rez soph for this year!!"
        w "I like to live my life with this simple philosophy:"
        w "WaAaAaAaAh!"
        w "And don't you forget it!"
        w "AnyWAHys, dinner is starting in 15 mins! Make sure to make your way down to the dining hall"
        w "See you soon, and don't forget to WAH!"

        "Oh my gosh... that guy... he..."

        scene dorm
        show maria2happy at left
        show bobhappy at right
        with fastdissolve
        m "He's so hot, omg!!"
        b "Wow, he lookin kinda cute tho, not gunna lie ;^)"
        n "I... uh.. huh??"

        "Uh oh... don't tell me we all have a crush on the same guy!"

        hide maria2happy
        hide bobhappy

        jump dinner


    label dinner:
        scene dining
        with slowdissolve
        "So the three of us headed down to the dining hall to get dinner"
        "I still couldn't get that Waluigi guy out of my head"
        "Something about him... he was so dreamy!"
        "Sadly, I wasn't the only one who thought that way about him..."

        show maria2 at left
        show bob at right
        with fastdissolve
        m "I wonder if that Waluigi guy is single, he is sooooo dreamy"
        b "He makes my knees weak, arms spaghetti"
        b "Vomit on my sweater already, mom's spaghett-"
        b "Oh look, there he is! :)"

        "My heart skipped a beat"
        "There he was, standing in line to grab food"
        "We got in line too, right behind him"
        hide maria2
        hide bob
        with fastdissolve

        show wah
        with fastdissolve
        w "WAAAAAAAAAHHHH!"
        show wahhappy
        w "Hello my fellow frosh! What shall you feast on this fine evening?"
        hide wahhappy
        "Omigosh, what should I get?? I feel the weird need to impress him with my food preferences"
        hide wah
        menu:
            "CHeeeeeken wings": #+love
                $love += 1
                jump chicken
            "Salad": #-love
                $love -= 1
                jump salad
            "Burger King foot lettuce":
                jump BK

        label chicken:
            n "Oh uh, I'm just gonna get chicken wings"
            show wahhappy
            with fastdissolve
            w "Waaaahhhhh! Excellent choice, [name]. Truly a meal fit for a king!"
            show maria2mad at left
            show wahhappy at right
            with fastdissolve
            m "W-well, *I'M* going to get a salad!"
            hide wahhappy
            show wahangry at right
            w "Wahhh... how boring"
            hide maria2mad
            show maria2sad at left
            m "HUH??"
            hide maria2sad
            hide wahangry
            show bobhappy at left
            show wah at right
            with fastdissolve
            b "Beep beep lechuga"
            w "ok"
            hide bob
            hide wah
            with dissolve
            jump night

        label salad:
            n "Oh uh, I'm just gonna get a salad"
            show wahsad
            with fastdissolve
            w "Wahhh... how boring"
            hide wahsad
            show wah at right
            show maria2happy at left
            with fastdissolve
            m "Hah, how boring indeed! Meanwhile, *I'VE* decided to get some chicken wings, like a true man of culture"
            m "Er... woman"
            hide wah
            show wahhappy at right
            w "Wahahah! That's what I like to hear!"
            hide maria2happy
            show bob at left
            with fastdissolve
            b "Beep beep lechuga"
            w "ok"
            hide wahhappy
            hide wahsad
            hide wah
            with dissolve
            jump night

        label BK:
            play music "lettuce.mp3"
            n "Number 15... burger king foot lettuce"
            show wah
            with fastdissolve
            w "..."
            w "The last thing you'd want in your Burger Kiiiiiiiiiiiiiiiing Burger"
            w "is someone's foooooot funguuuuuuuus"
            w "But as it turns out, that might be what you GAAAAAAAAAAEEEAAAEEEAAEEEEEEEEEET"
            hide wah
            show wahhappy
            w "Let's get married"
            hide wahhappy
            with fastdissolve
            show maria2mad
            m "UM WHAT???"
            hide maria2mad
            show bobshock
            with fastdissolve
            b "UWO?!?!!??!"
            hide bobshock
            with fastdissolve
            n "lol cool"
            scene wahtpose
            with slowdissolve
            "SECRET ENDING!"
            "Now THIS is epic!"
            return

        label night:
            scene black
            with fade
            "What a night!"
            "Who would've thought that meeting your one and only true love and your two sworn enemies would be so tiring?"
            "I better get some rest, classes start tomorrow! I've got a long day ahead"


        label day1:
            play music "flower.mp3"
            scene bed
            with fade
            $sleep = 0
            "(THE NEXT DAY...)"
            "rIsE aNd ShInE"
            "I should get up, I don't wanna be late for my very first class"
            "History of Hype Beasts sounds really interesting"
            "Unless..."
            menu:
                "Sleep in for 5 more minutes":
                    jump five_more_mins
                "Get out of bed":
                    jump class1

            label five_more_mins:
                if sleep == 12:
                    "You absolute buffoon"
                    "You missed your goddamn class"
                    "How will Waluigi ever love you now??"
                    "LAZY END!!"
                    return
                else:
                    "I snooze for 5 more mins, and then..."
                    "RiSe AnD sHiNe"
                    menu:
                        "5 more minutes!":
                            $sleep += 1
                            jump five_more_mins
                        "Get up, lazy!":
                            jump class1

        label class1:
            scene lecture
            with fade
            "I make it to class in time"
            "Wait... what the??"
            "To my shock, I see the one and only WALUIGI sitting in the lecture hall among the other students"
            "No way... are we in the same class???"
            "I decide to try and sit next to him"
            "But then..."

            show maria2happy at left
            show wah at right
            with fastdissolve
            m "Ahaha, you're SO funny Waluigi!"
            w "Waaahhh"
            "What the hell?? She's in my class too? And why is she sitting next to HIM??"
            menu:
                "Quietly sit down next to them":
                    jump quietly
                "Jump into the conversation":
                    jump jumpp

            label quietly:
                $love += 1
                "*Sits down*"
                m "SOOOO anyways, I was thinking that---"
                hide maria2happy
                show maria2mad at left
                hide wah
                show wahhappy at right
                w "Waahhh, hello there frosh! I see you're in this class too?"
                n "Oh! Um... yes, I am!"
                hide wahhappy
                show wah at right
                w "History of Hype Beasts... a very WAHpic course"
                w "Maria here was just telling me about how passionate she is about the subject, wahh!"
                hide maria2mad
                show maria2happy at left
                m "Oh yeah, definietly. I totally did not just switch into this course last night because I knew Waluigi was also in the class"
                m "Hahaha!"
                n "Hahaha...."
                n "(You liar...)"
                hide maria2happy

            label major:
                show wah at truecenter
                with fastdissolve
                w "So tell me, [name], what are you majoring in?"
                n "My major? Well..."
                menu:
                    "Ultimate Tennis":
                        jump parkour
                    "Competitive Crying":
                        jump koopa
                    "Munkey Maths":
                        jump munkey
                    "Music":
                        jump jazz

                label parkour: #+love
                    $love += 1
                    $tennis = True
                    n "I'm majoring in Ultimate Tennis"
                    hide wah
                    show wahhappy
                    w "WAAAH! I love tennis! Truly the sport of the legends"
                    hide wahhappy
                    with dissolve
                    jump class_starts

                label koopa: #no effect
                    $crying = True
                    n "I'm majoring in Competetive Crying"
                    hide wah
                    show wahsad
                    w "Waahhh, this is so sad, alexa play despacito"
                    hide wahsad
                    with dissolve
                    jump class_starts

                label munkey: #-love
                    $love -= 1
                    $munkey = True
                    n "I'm majoring in Munkey Math"
                    hide wah
                    show wahsad
                    w "Wahhhh? I don't know how to do math"
                    hide wahsad
                    with dissolve
                    jump class_starts

                label jazz:
                    n "I'm actually majoring in music. I play the trumpet"
                    play sound "bee.mp3"
                    n "Ya like jaaaazzzz?"
                    w "..."
                    hide wah
                    show wahangry
                    w "bruh"
                    w "wtf"
                    w "u just posted cringe"
                    w "u are going to loose subskriber"
                    n "owo"
                    "And then I died"
                    "THE END!!"
                    return

            label jumpp: #-love
                $love -= 1
                "I can't let Maria have Waluigi all to herself!"
                m "SOOO anyways, like I was saying--"
                n "Hey guys!! What are you talking about??"
                hide maria2happy
                show maria2mad at left
                m "OMG we're having a conversation here, don't interrupt us!"
                n "Shut UP Maria!!"
                hide wah
                show wahangry at right
                w "Waaahhh... that is very rude of you [name]"
                n "...I'm sorry!"
                "God dammit! I totally made a fool of myself"
                "I sure hope this one single decision I've made won't affect any events in the future..."
                hide maria2mad
                hide wahangry
                jump major

            label class_starts:
                "It's almost time for class to start, so we decide to put the conversation on hold"
                "But the prof is nowhere to be found!"
                #insert nooks cranny music here
                play music "nookscranny.mp3"
                "Hold on, what's that music?"
                show nook
                with fastdissolve
                t "Hoho, apologies for being late my students"
                t "I was too busy scamming my clien-"
                show nookmad
                t "Ah I mean, HELPING my clients... ahaha"
                t "Silly autocorrect"
                "ok boomer..."
                hide nookmad
                t "Anywho, despite the fact that this is the first class, we will be having a pop quiz!"
                t "I hope you have studied your knowledge of hype beasts well!"
                show nookmad
                t "And YES, this will count towards your grade!"
                t "God I love being a dickhead"
                hide nookmad
                hide nook
                "BRUH"
                "SAY SIKE RN"
                "A quiz?? I was not ready for this!!"
                "This is totally unfair, does he really expect us to study stuff over the break?"
                "I look around frantically to see if anyone else is as panicked as I am"
                with fastdissolve
                show maria2 at left
                show wah at right
                with fastdissolve
                m "What's wrong, [name]? Didn't come prepared for class, huh?"
                w "This'll be easy! Waaaahhhh!"
                hide maria2
                hide wah
                with fastdissolve
                "Crap... I guess everyone else got the memo.."
                "I'll just have to do my best"

                jump q1

            label q1:
                play music "wahfunk.mp3"
                $score = 0
                show wah
                with fastdissolve
                w "Are you ready for the quiz? It's all about MEEEE"
                "HUH???"
                "WTF?"
                "When did Waluigi get at the front of the class? Where did our WHACK prof go??"
                "Am I... am I hallucinating right now?"
                w "Question 1: Waht is my favourite sport?"
                menu:
                    "A) Bowling":
                        show wahangry
                        w "WAHHH! That's wrooong"
                        hide wahangry
                        jump q2

                    "B) Wah-king":
                        show wahangry
                        w "WAAAHH! That's wroooong"
                        hide wahangry
                        jump q2

                    "C) Tennis":
                        $score += 1
                        show wahhappy
                        w "WAHAHA! That's riggght"
                        hide wahhappy
                        jump q2

                    "D) Crying":
                        show wahangry
                        w "WAAAHHH that's wrooonng"
                        hide wahangry
                        jump q2

            label q2:
                w "qUESTION 2: Am I actually related to Wario?"
                menu:
                    "A) Uh, duh":
                        show wahangry
                        w "WAHHH! That's wrooong"
                        hide wahangry
                        jump q3

                    "B) Of course not!":
                        show wahangry
                        w "WAAAHH! That's wroooong"
                        hide wahangry
                        jump q3

                    "C) ;)":
                        $score += 1
                        show wahhappy
                        w "WAHAHA! That's riggght"
                        hide wahhappy
                        jump q3

                    "D) :)":
                        show wahangry
                        w "WAAAHHH that's wrooonng"
                        hide wahangry
                        jump q3

            label q3:
                w "Question 3: What does WAH mean?"
                menu:
                    "A) It comes from your name":
                        show wahangry
                        w "WAHHH! That's wrooong"
                        hide wahangry
                        jump q4

                    "B) Waaaaaaahh":
                        show wahangry
                        w "WAAAHH! That's wroooong"
                        hide wahangry
                        jump q4

                    "C) 'Woe Art He' ":
                        show wahhappy
                        $score += 1
                        w "WAHAHA! That's riggght"
                        hide wahhappy
                        jump q4

                    "D) Crying noise":
                        show wahangry
                        w "WAAAHHH that's wrooonng"
                        hide wahangry
                        jump q4
            label q4:
                w "QWAHstion 4: Waht is my favourite food?"
                menu:
                    "A) Wah-ter":
                        show wahangry
                        w "WAHHH! That's wrooong"
                        hide wahangry
                        jump fin

                    "B) Mom's spaghetti":
                        show wahangry
                        w "WAAAHH! That's wroooong"
                        hide wahangry
                        jump fin

                    "C) Whale":
                        show wahhappy
                        $score += 1
                        w "WAHAHA! That's riggght"
                        hide wahhappy
                        jump fin

                    "D) Knees weak, arms spaghetti":
                        show wahangry
                        w "WAAAHHH that's wrooonng"
                        hide wahangry
                        jump fin

            label fin:
                hide wah
                show nook
                with fastdissolve
                t "Okay class! Quiz is over, let's see how you did..."
                "I'm... so confused.... what just happened?!?!"
                if score == 4: #+LOve
                    $love += 1
                    t "Excellent work! I see you have studied hard"
                    hide nook
                    show wahhappy at left
                    show maria2mad at right
                    with fastdissolve
                    w "WAHH! You're so smart!"
                    m "What the... you scored more than me?? Impossible!"
                    hide wahhappy
                    hide maria2mad
                    with fastdissolve
                else: #-LOVE
                    $love -= 1
                    show nookmad
                    t "Oh dear... looks like someone needs to study more"
                    hide nookmad
                    hide nook
                    show wahsad at left
                    show maria2 at right
                    with fastdissolve
                    w "Waahhh.. you are so dumb.."
                    m "LMAO, even I did better than you, stoopid"
                    hide wahsad
                    hide maria2
                    with fastdissolve

        label night1:
            scene black
            with fade
            "What a crazy day..."
            "I don't know WHAT happened during class, maybe I was hallucinating or something"
            "Sigghhh, Waluigi is so dreamy, I can't stop thinking about him"
            "Time to sleep... another busy day ahead of me"

        label day2:
            play music "athletic.mp3"
            scene bed
            with slowdissolve
            "Ugghhh.... I don't want to get up"
            "OH wait :o! If I get up, I might see Waluigi!"
            "Okay, let's get up and go to class~"
            scene bridge
            with slowdissolve
            "*Several classes later bc I'm too lazy to make a proper storyline*"
            "As I walk back to class, I run into Waluigi!"
            show wah
            with fastdissolve
            if love >= 6:
                "He turns towards me"
                w "WAAAH! Hello [name]!"
                n "O-oh! Hi Waluigi! What brings you here?"
                w "I wahnted to talk to you, actually"
                "With ME???? Ohmigoshhhh"
                w "I thought you were super swanky the other day in class"
                w "Wahnna hang out together?"
                menu:
                    "Yes!":
                        jump date
                    "No!":
                        jump are_you_sure

                label are_you_sure:
                    "Hey wait... are you sure you meant to click no? SURELY that was an accident, yeah?"
                    menu:
                        "Oops! I meant to say yes!":
                            jump date
                        "Nope.. I don't wanna hang out":
                            "You absolute doofus"
                            "Why are you even playing this game"
                            return
            else:
                show wah
                with fastdissolve
                n "Hi Waluigi!"
                w "Waaahh... hello [name]"
                n "Are you doing anything right now?"
                w "Not really, waahh"
                n "Oh...! Do you wanna hang out, maybe grab food or something?"
                hide wah
                show wahangry
                w "Wahhhh... no, I don't want to do that"
                n "Oh... um..."
                w "See you later, waaaahh"
                n "Oh okay... bye"
                "Something about that didn't feel right..."
                hide wahangry
                jump other_girl

            label date:
                if tennis:
                    show wah
                    w "I know you said you're majoring in Ultimate Tennis, and I myself am a big tennis fan"
                    hide wah
                    show wahhappy
                    w "In fact, you could even call me... number WAHn!!!"
                    w "Let's go play tennis together! Waaahhh"
                    "Ohmygod ohmygod ohmygod"
                    "Is this REALLY happening??"
                    n "Yeah! That sounds like fun!"
                    hide wahhappy
                    scene wahtennis
                    with slowdissolve
                    "So Waluigi and I spent the day playing our favourite sport, tennis"
                    "He wasn't kidding, he really is good at the game"
                    "I had so much fun, it was like a dream come true!"
                    jump confess


                if crying:
                    show wah
                    w "I know you said you're majoring in Competetive Crying, and I myself am a VERY depressed individual"
                    n "Really? I would have never guessed... you always seem so confident"
                    hide wah
                    show wahsad
                    w "Waaahhh... not everything is waht it seems, my fellow frosh"
                    w "Anyways, I think it's totally woke of you to embrace your sad feelings like that"
                    w "I totally vibe with that, wahhhh"
                    w "Sometimes we just gotta let our feelings out, ya know?"
                    scene wahcry
                    with slowdissolve
                    "And so Waluigi and I proceeded to cry and cry and cry... for 4 hours straight"
                    "It was kind of strange, but also theraputic in the weirdest way"
                    hide wahsad
                    jump confess2


                if munkey:
                    play music "2am.mp3"
                    show wah
                    with fastdissolve
                    w "So you're majoring in Munkey Math wah?"
                    n "Ye"
                    hide wah
                    show wahsad
                    w "Wahhh, Waluigi hates math!"
                    hide wahsad
                    show wah
                    w "But my boyfriend is in the same major, so Waluigi is trying to appreciate it more"
                    n "Ohh, okay"
                    n "..."
                    n "Wait what??"
                    show wahhappy
                    w "Wah! You know my boyfriend, Bob!"
                    hide wahhappy
                    show wah at left
                    show bobshock at right
                    with fastdissolve
                    b "OWO?!?!?"
                    w "WAHHHsup Bob! You know [name], right?"
                    n "We're... roommates..."
                    hide bobshock
                    show bobhappy at right
                    b "Oh, hewwo [name], long time no see, eh?"
                    hide bobhappy
                    show bobshock at right
                    b "I think the writer just forgot about me for a while"
                    b "And then at the last minute, like maybe 4 hours before the project was due, she realized I was still a thing"
                    hide bobshock
                    show bob at right
                    b "Haha..."
                    n "What"
                    n "So um... *cough* when did this become a thing??"
                    hide wah
                    show wahhappy at left
                    w "Wahhh! Just a few seconds ago actually!"
                    hide bob
                    show bobhappy at right
                    b "We're getting married tomorrow :D"
                    b "You wanna come?"
                    n "..."
                    n "Sorry... um..."
                    n "I can't..."
                    n "My fridge is broken..."
                    n "Gotta blast"
                    hide bobhappy
                    hide wahhappy
                    with fastdissolve
                    "Well"
                    "I guess it's time to transfer"
                    "Waterloo, here I come!"
                    scene bobend
                    with slowdissolve
                    "WTF END! :o"
                    return


            label confess:
                play music "end.mp3"
                scene black
                with fade
                "I had such a wonderful time playing tennis with Waluigi"
                "I think we got along really well, he might even like me back!"
                "I've decided, I'm going to tell him how I feel..."
                scene cherry
                with slowdissolve
                "And what better place to confess your feelings to someone than under cherry blossom trees?"
                "(This is definitely located in London Ontario)"
                show wah
                with fastdissolve
                w "Hi [name], you wanted to meet me here?"
                n "Yes... now it's my turn to wahnt to talk to you"
                w "owo?"
                w "wahts all this about?"
                n "Waluigi, I really like you"
                n "I don't know if you feel the same way about me"
                n "But I just wanted you to know how I felt... I hope we can spend more time together"
                show wahhappy
                w "Waaahh! I like you too!"
                n "Wait what?? Really?"
                w "That's why I invited you to tennis! You're quite the player, by the waaaahhy"
                w "Let's be together, forever! WAAAHHH!"
                "I can't believe this..."
                "I feel... so happy"
                "Like I'm walking on clouds, like nothing in this world could ever hurt me"
                "Is this what love feels like???"
                scene wahlove
                with slowdissolve
                "GOOD END! :)"
                return

            label confess2:
                play music "sandgem.mp3"
                scene black
                with fade
                "I never thought I'd have a crying session with my crush, but here we are"
                "I think it helped us get closer"
                "And he mentioned letting out your feelings from time to time"
                "So I think it's time I tell Waluigi how I feel..."
                scene cherry
                with slowdissolve
                "Time to follow the stereotypes and confess to my crush under a cherry blossom tree!"
                "London Ontario is ESPECIALLY known for cherry blossom trees :^)"
                show wah
                with fastdissolve
                w "Wahh, hello [name], you wanted to meet me here?"
                n "Yes... there's something that's been on my mind"
                w "Waahht is it?"
                n "Well, ever since our crying session, I've been thinking"
                n "You know, about letting our feelings out and stuff"
                n "So I think it's about time I tell you... about the feelings I have for you"
                n "I really like you, Waluigi!"
                w "..."
                n "..."
                "Silence? Why???"
                hide wah
                show wahsad
                w "Wahh, [name], I'm sorry"
                w "I like you, but not in that way"
                w "I admire your courage to tell me though... wahhh"
                w "I'm sure you'll find that special someone someday, you just need patience"
                w "WAAAAAHHHH!"
                n "I... I'm so sorry!"
                "And just like that, I ran away in tears"
                "I feel so ashamed in myself"
                "I was so sure I had it all right... how could I mess this up??"
                scene waluigisad
                with slowdissolve
                "SAD END :("
                return


            label other_girl:
                scene black
                with fade
                play music "fuzzy.mp3"
                "I couldn't focus for the rest of the day"
                "All that I could think about was that interaction I had with Waluigi"
                "Something about him seemed very cold and unfriendly"
                "I wonder... did I do something wrong??"
                scene dining
                with slowdissolve
                "As I'm about to get dinner, I catch a glimpse of Waluigi and... Maria?? Standing outside the dining hall"
                "What the... what could they be talking about?"
                "I get closer, to eavesdrop"
                show wah at left
                show maria2 at right
                with fastdissolve
                m "Waluigi! I have to tell you something!"
                w "Wahhh, what is it?"
                hide maria2
                show maria2happy at right
                m "I'm like, totally in love with you!"
                m "Also, I heard that [name] has head lice lmao"
                hide wah
                show wahhappy at left
                w "WAAAHH! I love you too, Maria!"
                hide maria2happy
                hide wahhappy
                show maria2 at right
                show wah at left
                w "Wahh... strange, this feels like deja vu"
                w "Has this happened before??"
                m "No, definitely not"
                m "Especially not in the form of a dating simulator created for a high school hackathon in the year 2018"
                w "waht"
                m "waht"
                hide maria2
                hide wah
                with fastdissolve
                "So... this is what failure feels like"
                "I can't believe I lost to that Maria!"
                "If only... I was better at embracing the WAHHH..."
                ":((("
                scene mariaend
                with slowdissolve
                "MARIA END :("
