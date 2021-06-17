# class to contain questions and corresponding answers
import time


class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# question prompts
question_prompts = [
    "1)Which among the following is not a correct pair?\na)Ellora Caves – Rastrakuta Rulers\nb)Mahabalipuram – "
    "Pallava Rulers\nc)Khajuraho – Chandellas\nd)Elephanta Caves – Maurya Era\n\n",

    "2)Which king started the organization of Kumbh fair at Allahabad?\na)Harshavardhana\nb)Dhruvasena "
    "Ii\nc)Narshimhvarman\nd)Akabar\n\n",

    "3)Mudumalai Sanctuary is situated in:\na)Arunachal Pradesh\nb)Tamil Nadu\nc)West Bengal\nd)Kerela\n\n",

    "4)What led to the end of Indus Valley Civilization?\na)Invasion of Aryans\nb)Recurrent "
    "Floods\nc)Earthquakes\nd)All the above\n\n",

    "5)Which of the following river is called as the ‘Sorrow of Bengal’?\na)The Gandak\nb)The Kosi\nc)The Son\nd)The "
    "Damodar\n\n",

    "6)India's permanent research station Dakshin Gangotri is situated in:\na)Great Himalayas\nb)Indian "
    "Ocean\nc)Antarctica\nd)Arabian Sea\n\n",

    "7) Who among the following can remove the governor of a state from office?\na)Legislative "
    "Assembly\nb)Parliament\nc)President\nd)Supreme Court\n\n",

    "8) In which year, Goa was formally assimilated in the territories of India by 12th Amendment Act, which made "
    "Goa, Daman & Diu a Union Territory?\na)1960\nb)1961\nc)1962\nd)1963\n\n",

    "9)The President of India can nominate ___members in Lok Sabha and __ members in Rajya Sabha.\na)12, 2\nb)2, "
    "12\nc)2, 10\nd)10, 2\n\n",

    "10)What is the full form of BIOS?\na)Basic Input-Output System\nb)Bureau of Information Science\nc)Business "
    "Investment on Shares\nd)Broadcasting and Information Organisation\n\n",

    "11)What is the full form of CV?\na)Circulum Vitae\nb)Computer Virus\nc)Central Vigilance\nd)Circular Velocity\n\n",

    "12)Which of the following books has been written by Vikram Seth?\na)My God Died Young\nb)Islamic Bomb\nc)Look "
    "Back in Anger\nd)A Suitable Boy\n\n",

    "13)Which is the highest gallantry award in India?\na)Param Vishishtat Seva Medal\nb)Param Vir Chakra\nc)Kirti "
    "Chakra\nd)Vir Chakra\n\n",

    "14)Devaluation of a currency means:\na)reduction in the value of a currency vis-a-vis major internationally "
    "traded currencies\nb)permitting the currency to seek its worth in the international market\nc)fixing the value "
    "of the currency in conjunction with the movement in the value of a basket of pre-determined currencies\nd)fixing "
    "the value of currency in multilateral consultation with the IMF, the World Bank and major trading partners\n\n",

    "15)Who among the following was an eminent painter?\na)Sarada Ukil\nb)Uday Shanker\nc)V. Shantaram\nd)Meherally\n\n"
]

# 5 additional questions
optional_questions = [
    "16)Which scientist discovered the radioactive element radium?\na)Isaac Newton\nb)Albert Einstein\nc)Benjamin "
    "Franklin\nd)Marie Curie\n\n",

    "17)Dr. M. S. Swaminathan has distinguished himself in which of the following "
    "fields?\na)Agriculture\nb)Medicine\nc)Astrophysics\nd)Physics\n\n",

    "18)'OS' computer abbreviation usually means?\na)Order of Significance\nb)Open Software\nc)Operating "
    "System\nd)Optical Sensor\n\n",

    "19)Which was the 1st non Test playing country to beat India in an international match?\na)Canada\nb)Sri "
    "Lanka\nc)Zimbabwe\nd)East Africa\n\n",

    "20)20th August is celebrated as\na)Earth Day\nb)Sadbhavana Divas\nc)No Tobacco Day\nd)None of these\n\n"
]

# invoking class objects
questions = [
    Questions(question_prompts[0], "d"),
    Questions(question_prompts[1], "a"),
    Questions(question_prompts[2], "b"),
    Questions(question_prompts[3], "d"),
    Questions(question_prompts[4], "b"),
    Questions(question_prompts[5], "c"),
    Questions(question_prompts[6], "c"),
    Questions(question_prompts[7], "d"),
    Questions(question_prompts[8], "b"),
    Questions(question_prompts[9], "a"),
    Questions(question_prompts[10], "a"),
    Questions(question_prompts[11], "d"),
    Questions(question_prompts[12], "b"),
    Questions(question_prompts[13], "a"),
    Questions(question_prompts[14], "a")
]

# invoking class objects
opt_questions = [
    Questions(optional_questions[0], "d"),
    Questions(optional_questions[1], "a"),
    Questions(optional_questions[2], "c"),
    Questions(optional_questions[3], "b"),
    Questions(optional_questions[4], "b")
]


# function to calculate and display marks
def quiz(question, opt_question):
    marks = 0
    ques = 0
    skip = 0
    for question in question:
        ques += 1
        answer = input(question.prompt)
        if answer == question.answer:
            marks += 2
        elif answer == "s":
            skip += 1
    if skip == 0:
        opt = input(
            "You are eligible to attempt for an extra 5 questions! Do you want to take this opportunity?(Y/N): ")
        if opt == "Y" or opt == "y":
            for question in opt_question:
                ques += 1
                answer = input(question.prompt)
                if answer == question.answer:
                    marks += 2
                elif answer == "s":
                    skip += 1

    print("You have completed the quiz!!")
    print("You got {} out of {}".format(marks, 2 * ques))
    return (marks / (2 * ques)) * 100


# User enters name and willingness to attempt the quiz
start_time = time.time()
name = input("Enter your Name here: ")
ans = input("Are you ready to test your General Knowledge?(y/n) ")

if ans == "Y" or ans == "y":
    print("Let's start then! ")
    print("Instructions:\n"
          "1. Read each and every question carefully.\n"
          "2. Every right answer awards +2 and no negative marking.\n"
          "3. If you answer all the questions, you can opt to answer 5 bonus questions.\n"
          "4. If at any question, you get stuck and want to skip, Enter 's'!\n"
          "5. Good luck! Give your best.\n")
    input("Press enter to view the 1st question. ")

    percentage = quiz(questions, opt_questions)
    # Displays customized message based on the %age
    if percentage >= 85:
        print("You did a great job answering those questions, {}".format(name))
    elif 40 <= percentage < 85:
        print("Trust yourself {}, you know more than you think you do".format(name))
    elif percentage < 40:
        print("Hey, {}! Don't get disappointed. Everybody is a genius. But if you judge a fish by its ability to "
              "climb a tree, it will spend its whole life believing that it is stupid".format(name))

    print("\nBelow are the correct answers for the questions:")
    for question in questions:
        print(question.answer)
    for question in opt_questions:
        print(question.answer)
    print("--- {} seconds ---".format(time.time() - start_time))
    input("Press Enter to exit:")

else:
    print("You have chosen to opt out of the Quiz!")
