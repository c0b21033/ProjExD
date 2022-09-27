from random import randint
def shutudai():
    global questionnum, answernum, Maxnum, questions
    questionnum = randint(7, 10)
    questions = set()
    answernum = randint(1, 4)
    Maxnum = 3
    for i in range(questionnum):
        questions.add(chr(randint(65, 90)))
    print(f"対象文字\n{questions}")

def kaitou():
    answers = []
    for i in range(answernum):
        a = questions.pop()
        answers.append(a)
    print(f"欠損文字{answers}")
    print(answernum)
    print(f"表示文字{questions}")
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
    else:
        print("不正解です")
    
def main():
    shutudai()
    kaitou()

main()
        
    