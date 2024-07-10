import enchant.checker as ec


NAME = 'Zane'
VERSION = '0.0.1'
DEVELOPER ='Eyad Hassan'
def ask():
    prompt = input("ask something....\n")
    return prompt

def getanswer(question_index :int,answer:list):
    return answer[question_index]
def addanswer(questions:list,answers:list,question:str,answer:str):
    questions.append(question)
    answers.append(answer)
    return [questions,answers]

def main():
    dic = ec.get_default_language()
    questions =['Hi','Hello','Bye',"Close","Exit"]
    answers =["Hi","Hi","GoodBye","GoodBye","GoodBye"]
    is_r =True
    while is_r:
        prompt = ask()
    


if __name__ == '__main__':
    main()