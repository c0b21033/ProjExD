import random
from tokenize import Number
def shutudai(): #問題をランダムに出題する関数
    global answers #kaito関数で使用するので
    questions = ["鮪の読みを答えよ", "魑魅魍魎の読みを答えよ", "亜米利加の読みを答えよ", "闘球の読みを答えよ"] #問題のリスト
    answers = [["まぐろ", "マグロ"], ["ちみもうりょう", "チミモウリョウ"], ["あめりか", "アメリカ"], ["らぐびー", "ラグビー"]] #答えのリスト
    number = random.randint(0, 3) #問題と答えの番号をランダムに決定し、変数に保存
    print(questions[number]) #問題の出題
    return number #問題と答えの番号を返す

def kaito(number): #ユーザーの解答を受け付け結果を返す関数
    ans = input("ひらがなかカタカナで答えてね：") #解答を受け付ける
    if ans in answers[number]: #正解の場合
        result = "正解"
    else: #不正解の場合
        result = "不正解"
    return result #結果を返す

def main(): #クイズゲームを行う関数
    number = shutudai() #numberに問題と解答の番号を代入しながらクイズを出題する
    result = kaito(number) #resultに結果を代入
    print(result) #結果を表示する

main() #関数の実行
