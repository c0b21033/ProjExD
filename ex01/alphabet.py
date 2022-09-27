from random import randint, shuffle
import datetime

def shutudai():
    global questionnum, answernum,questions, Maxnum
    questionnum = randint(7, 10)
    questions = set()
    answernum = randint(1, 4)
    for i in range(questionnum):
        questions.add(chr(randint(65, 90)))
    print(f"対象文字\n{display(questions)}")

def kaitou():
    global counts, end, questions
    counts += 1
    answers = []
    questions = list(questions)
    for i in range(answernum):
        a = questions.pop()
        answers.append(str(a))
        shuffle(questions)
    print(f"欠損文字{display(answers)}")
    print(answernum)
    print(f"表示文字{display(questions)}")
    ansnum = int(input("欠損文字はいくつあるでしょうか？"))
    if ansnum == answernum:
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
        for j in range(answernum):
            ans = input(f"では{j+1}つ目の欠損文字を入力してください")
            if ans in answers:
                pass
            else:
                print("不正解です　またチャレンジしてください")
                break
        else:
            print("欠損文字も全て正解です！")
            end = True
            ed = datetime.datetime.now()
            print("かかった時間"+str((ed-st).seconds)+"秒")
    else:
        print("不正解です")
    if Maxnum == counts:
        end = True

def display(lis):
    result = ""
    for i in lis:
        result += i
        result += " "
    return result
    
def main():
    shutudai()
    kaitou()

end = False
counts = 0
Maxnum = 3
st = datetime.datetime.now()
for i in range(Maxnum):
    main()
    if end == True:
        print("またチャレンジしてください")
        break