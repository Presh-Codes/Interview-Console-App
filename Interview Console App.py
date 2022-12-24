score = 0

print("Hello there, would you like to participate in this interview and answer a few questions?\n1.Yes\n2.No\n")
choice = input()
if choice == "1":
    print("Okay, so the rules are; if you answer a question correctly, you get two points\nSo let's begin\n")
    print("First of all, what is your First name?\n")
    First_name = input()
    print("What is your surname?\n")
    Sur_name = input()
    print("How old are you?\n")
    age = input()
    print("First question; What does CPU stand for?\n")
    cpu_answer = input()
    if cpu_answer.lower() == "central processing unit":
        print("Correct!\n")
        score += 2
    else:
        print("WRONG! The answer is Central Processing Unit\n")
    print("What does RAM stand for?\n")
    ram_answer = input()
    if ram_answer.lower() == "random access memory":
        print("Correct!\n")
        score += 2
    else:
        print("WRONG! The answer is Random Access Memory\n")
    print("What does ROM stand for?\n")
    rom_answer = input()
    if rom_answer.lower() == "read only memory":
        print("Correct!\n")
        score += 2
    else:
        print("WRONG! The answer is Read Only Memory\n")
    print("What is another name for touchpad?\n")
    touchpad_answer = input()
    if touchpad_answer.lower() == "trackpad":
        print("Correct!\n")
        score += 2
    else:
        print("WRONG! The answer is trackpad\n")
    print("What is 2x2x25+50-25-15-10?\n")
    math_answer = input()
    if math_answer.lower() == "100":
        print("Correct!\n")
        score += 2
    else:
        print("WRONG! The answer is 100\n")
    if score <= 4:
        print("Man, you've failed quite a lot\n")
        print("Would you like to answer a bonus question to boost up your score?\n1.Yes\n2.No")
        bonus = input()
        if bonus == "1":
            print("Okay, Who is the founder and owner of Space X?\n")
            bonus_answer = input()
            if bonus_answer.lower() == "elon musk":
                print("Correct!\n")
                score += 4
            else:
                print("WRONG! The answer is Elon Musk\nOh well\n")
        else:
            print("Alright\n")

    percentage_score = str((score/10)*100)

    print("Name: "+First_name+" "+Sur_name+"\nAge: "+age+"\nScore: "+str(score)+"\nPercentage1: "+percentage_score+"%\n")