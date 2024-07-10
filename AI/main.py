from textblob import WordList,Word
import string as st

NAME = 'Zane'
VERSION = '0.0.1'
DEVELOPER ='Eyad Hassan'


def ask():
    prompt = input("ask something....\nYou:")
    return prompt


def getanswerindex(question:str,questions:list):
    for Index in range(len(questions)):
        if questions[Index] == question:
            break
        else:
            continue
    return Index


def getanswer(question_index :int,answer:list):
    return answer[question_index]



def addanswer(questions:list,answers:list,question:str,answer:str):
    questions.append(question)
    answers.append(answer)
    return [questions,answers]

def main():
    questions =['Hi','Hello','Bye',"Close","Exit","Who are you"]
    answers =["Hi","Hello","GoodBye","GoodBye","GoodBye",f'I\'m Your Chatbot {NAME} V.{VERSION} I\'d Created By {DEVELOPER}.']
    is_r =True
    while is_r:
        prompt = ask()
        promptstr = ''
        promptsent = []
        word = []
        x = 0
        if ' ' in prompt.strip():
            for f in range(len(prompt)):
                if prompt[f] == ' ':
                    promptsent.append(promptstr)
                    print(promptsent)
                    x+= 1
                    promptstr =''
                    
                else:
                    prompstr = promptstr.join(prompt[f])
                    word.append(promptstr)
                    print(word)
            ch =WordList(promptsent)
            promptstr =''
            print(promptsent)
        else:
            ch = Word(prompt)
        prompt = ch.correct()
        prompt = prompt.capitalize()
        print(f"searching {prompt}")
        if prompt in questions:
            ind = getanswerindex(prompt,questions)
            print(f"Zain:{getanswer(ind,answers)}")
            if prompt in questions[2:5]:
                break
            else:
                continue
        else:
            print('I don\' Understand You!')


if __name__ == '__main__':
    main()