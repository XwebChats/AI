import enchant.checker as ec


NAME = 'Zane'
VERSION = '0.0.1'
DEVELOPER ='Eyad Hassan'
def ask():
    prompt = input("ask something....\n")
    return prompt
def getanswerindex(question:str,questions:list):
    Index = 0
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
    dic = ec.get_default_language()
    questions =['Hi','Hello','Bye',"Close","Exit","Who are you"]
    answers =["Hi","Hi","GoodBye","GoodBye","GoodBye",f'I\'m {NAME} V{VERSION} I\'d Created By {DEVELOPER}']
    is_r =True
    while is_r:
        prompt = ask()
        prompt = prompt.capitalize()
        ind = getanswerindex(prompt,questions)
        print(getanswer(ind,answers))
        if prompt in questions[2:5]:
            break
        else:
            continue
    


if __name__ == '__main__':
    main()