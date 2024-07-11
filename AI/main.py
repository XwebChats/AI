from textblob import WordList,Word
import string as st
from funcs import *

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
        prompt = prompt.capitalize().strip()
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
            newQ = prompt
            prompt = input('will you teach me it?\nyou:')
            prompt = prompt.strip().capitalize()
            prompt = Word(prompt)
            if prompt.correct() == 'Yes':
                questions.append(newQ)
                prompt = int(input(f"what does {newQ} mean:\n1.Function\n2.Question\nYou:"))
                if prompt == 1:
                    with open('funcs.py','a+') as fil:
                        args = []
                        t = int(input('How many args: '))
                        for b in range(t):
                            arg = input(f'arg {b}: ')
                            args.append(arg)
                        step = []
                        steps = int(input('how many steps: '))
                        for n in range(steps):
                            prompt = int(input('step type :\n1.print\n2.input\nstep: '))
                            if prompt == 1 :
                                prnt = input('what to print: ')
                                step.append(f'  print(\'{prnt}\')\n')
                            elif prompt == 2 :
                                prompt = int(input('inputing:\n1.integer\n2.string\ntype casting:'))
                                if prompt == 1:
                                    varn = input('variable name: ')
                                    vari = input('what to type when inputting: ')
                                    step.append(f'  {varn} = int(input(\'{vari}\'))\n')
                                if prompt == 2:
                                    varn = input('variable name: ')
                                    vari = input('what to type when inputting: ')
                                    step.append(f'  {varn} = input(\'{vari}\')\n')
                                else:
                                    print('bad choose.')
                            else:
                                print('bad choose.')
                        if len(args) >0:
                            func = [f'def {newQ}({args}):\n']
                        else:
                            func = [f'def {newQ}():\n']
                            
                        for z in range(len(step)):
                            func.append(step[z])
                        fil.writelines(func)            
                elif prompt == 2:
                    pass
                else:
                    print('bad choose.')


if __name__ == '__main__':
    main()
    