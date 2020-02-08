
import random
import os
import time


def bgp_quiz():
    q1 = "Enter a regex that means 'Anything': "
    q2 = "Enter a regex that means 'Directly Connected AS#'s': "
    q3 = "Enter a regex that means 'Locally Originated Routes': "
    q4 = "Enter a regex that means 'Learned from AS 32934':" 
    q5 = "Enter a regex that means 'Originated from AS 32934': "
    q6 = "Enter a regex that means 'Any instance of AS# 32934': " 
    q7 = "Enter a regex character for the start of a string:"
    q8 = "Enter a regex character for the end of a string:"
    q9 = "Enter the regex characters for a range of characters:"
    q10 = "Enter a regex character to specify a numerical range:"
    q11 = "Enter a regex characters for a logical grouping:"
    q12 = "Enter a regex character for any singel character:"
    q13 = "Enter a regex character for Zero or more:"
    q14 = "Enter a regex character for One or more:"
    q15 = "Enter a regex character for Zero or one:"
    q16 = "Enter a regex character for start/end of string:"
    q17 = "What is the BGP TCP port number?"
    q18 = "Two ways to controll BGP egress?"
    q19 = "Two ways to controll BGP ingress?"
    q20 = "Two ways to controll BGP advertisements?"
    q21 = "IPv6 Link Local prefix?"


    a1 = ".*"
    a2 = "^[0-9]+$"
    a3 = "^$"
    a4 = "^32934_"
    a5 = "_32934$"
    a6 = "_32934_"
    a7 = "^"
    a8 = "$"
    a9 = "[]"
    a10 = "-"
    a11 = "()"
    a12 = "."
    a13 = "*"
    a14 = "+"
    a15 = "?"
    a16 = "_"
    a17 = "179"
    a18 = "weight, local preference"
    a19 = "MED, AS-PATH"
    a20 = "NO_EXPORT, NO_ADVERTISE"
    a21 = "FE80"


    pairs = {q1:a1, q2:a2, q3:a3, q4:a4, q5:a5, q6:a6, q7:a7, q8:a8, q9:a9, q10:a10, q11:a11, q12:a12, q13:a13, q14:a14, q15:a15, q16:a16, q17:a17, q18:a18, q19:a19, q20:a20, q21:a21}
    
    question_bank = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21]


    score = 0


    os.system('clear')
    print("Starting BGP Quiz:" "\n")


    while score < 20:
        time.sleep(1)
        question =  random.choice(question_bank)
        response = input(question)
        answer = pairs[question]
        
        
        if answer in response:
            score = score + 1
            print("\n")
            print("Correct! Your score is now: " + str(score) + "\n" + "\n")
        
        
        else:
            score = score - 1
            print("\n")
            print("Incorrect! Your score is now: " + str(score) + "\n" + "\n")
            print("Correct Answer = " + answer + "\n")
            

def main():
    #pass
    bgp_quiz()    


if __name__ == '__main__':
    main()
