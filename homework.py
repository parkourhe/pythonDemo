# 定义有多少题目
# import logo
# import homework1
import os
import time
import sqlite3
# 操作系统级比较底层的一个模块
# import homework3

from PIL import Image, ImageDraw, ImageFont


def checkDb(name=0, score=0, a='*'):
    con = sqlite3.connect('data.db')
    sql = '''select s.name,s.score from students s order by s.score desc'''
    cursor = con.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    for key in res:
        print('姓名:{}，成绩:{}'.format(key[0], key[1]))
    con.commit()
    cursor.close()

def inserAnswer(name,answer,imgB):
    con = sqlite3.connect('data.db')
    sql = '''insert into answer values(:name,:answer,:imgB)'''
    cursor = con.cursor()
    cursor.execute(sql, {"name": name, "answer":answer,"imgB":imgB})
    con.commit()
    cursor.close()

def insertDb(name, score):
    con = sqlite3.connect('data.db')
    sql = '''insert into students values(:name,:score,:location)'''
    cursor = con.cursor()
    cursor.execute(sql, {"name": name, "score": int(score), "location": '默认'})
    con.commit()
    cursor.close()


def generateCertificate(name, score):
    headerText = "奖状"
    word = str(name)+"同学"+"您总共获得"+str(score)+'分'
    color = "#000000"
    fontPath = 'font.ttf'
    fontType = ImageFont.truetype(fontPath, 80)
    imgPath = 'bgheng.png'
    img1 = Image.open(imgPath)
    draw = ImageDraw.Draw(img1)
    draw.text((820, 350), headerText, '#FF3333', fontType)
    draw.text((500, 600), word, color, fontType)
    img1.save(str(name)+'-'+str(time.time())+'-'+'output.png')
    img1.save('tempOutput.png')

def showlogo():
    print('                   _                      _           ')
    print('                  | |                    | |          ')
    print(' ____  _____  ____| |  _ ___  _   _  ____| |__  _____ ')
    print('|  _ \(____ |/ ___) |_/ ) _ \| | | |/ ___)  _ \| ___ |')
    print('| |_| / ___ | |   |  _ ( |_| | |_| | |   | | | | ____|')
    print('|  __/\_____|_|   |_| \_)___/|____/|_|   |_| |_|_____)')
    print('|_|  ')
    print(' '*22+"牛逼考试系统"+' '*22)


def questions():
    return {
        "一": """
    “但愿人长久，千里共婵娟”，其中婵娟指的是什么？
    A、 月亮     B、姻缘
    """,
        "二": """
    王先生的QQ签名档最近改成了“庆祝弄璋之喜”，王先生近来的喜事是：
    A、新婚   B、搬家   C、妻子生了个男孩 D、考试通过
    """,
        "三": """
    “爆竹声中一岁除，春风送暖入屠苏”，这里的“屠苏”指的是：
    A、苏州   B、房屋     C、酒   D、庄稼
    """,
        "四": """
    拱手而立表示对长者的尊敬，一般来说，男子行拱手礼时应该：
    A、 左手在外   B、右手在外
    """,
        "五": """
    我国的京剧脸谱色彩含义丰富，红色一般表示忠勇侠义，白色一般表示阴险奸诈，那么黑色一般表示:
    A、 忠耿正直   B、刚愎自用
    """,
        "六": """
    《三十六计》是体现我国古代卓越军事思想的一部兵书，下列不属于《三十六计》的是：
    A、浑水摸鱼   B、反戈一击   C、笑里藏刀   D、反客为主
    """,
        "七": """
    床前明月光是李白的千古名句，其中 “床”指的是什么？
    A、窗户     B、卧具     C、井上的围栏
    """,
        "八": """
    1932年，清华大学招生试题中有一道对对子题，上联“孙行者”，下面下联中最合适的是：
    A、胡适之   B、周作人     C、郁达夫   D、唐三藏
    """,
        "九": """
    月上柳梢头，人约黄昏后”描写的是哪个传统节日？
    A、中秋节   B、元宵节     C、端午节 D、 七夕节
    """,
        "十": """
    我国古代有很多计量单位，比如诗句“黄河远上白云间，一片孤城万仞山”中的“仞”，一仞约相当于：
    A、一个成年人的高度     B、成年人一臂的长度
    """
    }


def answer():
    return {
        "一": [
            'A', 10
        ],
        "二": [
            'C', 10
        ],
        "三": [
            'C', 10
        ],
        "四": [
            'A', 10
        ],
        "五": [
            'A', 10
        ],
        "六": [
            'B', 10
        ],
        "七": [
            'C', 10
        ],
        "八": [
            'A', 10
        ],
        "九": [
            'B', 10
        ],
        "十": [
            'B', 10
        ]
    }


def userMess():
    loaction = None
    name = None
    print('\n\n\n请输入您的基本信息\n\n')
    loaction = input('您来自哪里?')
    while loaction.strip() == '':
        loaction = input('请输入地址')
    print('\n\n')
    name = input('您叫什么?')
    while name.strip() == '':
        name = input('请输入姓名')
    print('\n\n')
    input('按任意键开始答题')
    return {
        'loaction': loaction,
        'name': name
    }

# def showlogo():
#     logo.showlogo()


def answerCheck(AnswerCount, _answer, usermess, score):
    if AnswerCount != 0 and len(usermess) != 0:
        print("\n\n\n答案分别是:\n")
        for key in _answer:
            print(_answer[key])
        print('\n\n'+str(usermess['name'])+'一共答对了'+str(AnswerCount)+"道题\n\n\n")
        print('\n您一共得分'+str(score))
        # writeInHistory(usermess, score)
        insertDb(usermess['name'], score)
        print('正在生成您的成绩证书')
        generateCertificate(usermess['name'], score)
        print('生成完成')
        print('证书保存在'+str(os.path.realpath('output.png')))
        input('请按任意键退出')
        
        

    else:
        insertDb(usermess['name'], score)
        # writeInHistory(usermess, score)
        print("您傻逼了吧,一道题都没对")
        print('正在生成您的成绩证书')
        generateCertificate(usermess['name'], score)
        print('生成完成')
        print('证书保存在'+str(os.path.realpath('output.png')))
        input('请按任意键退出')
        


def startToAnswer():
    userAnswers = {}
    showlogo()
    _usermess = userMess()
    _ques = questions()
    _answer = answer()
    print('请回答10道问题')
    score = 0
    userAnswer = None
    AnswerCount = 0
    for key in _ques:
        print('\n\n第'+str(key)+'题:'+str(_ques[key]))
        userAnswer = input("请输入:")
        print(userAnswer)
        userAnswers[key]=userAnswer
        print(_answer[key])
        if userAnswer.lower() == _answer[key][0].lower():
            score += _answer[key][1]
            AnswerCount += 1      
    answerCheck(AnswerCount, _answer, _usermess, score)
    print('=============================')
    
    fp = open("tempOutput.png", 'rb')
    Bimg = fp.read()
    inserAnswer(_usermess['name'],str(userAnswers),Bimg)
    print('haah')  


def writeInHistory(usermess, score):
    con = {
        "name": usermess['name'],
        "score": score
    }
    # print(con)
    # print(usermess)
    # print(usermess['loaction'])
    # currentFile = os.getcwd()
    his = open("score.txt", 'a')
    his.write(str(con)+'&')


def checkHistory():
    dec = []
    data = open("score.txt", 'r')
    dataIn = data.read()
    dataIn = dataIn.replace('{', '')
    dataIn = dataIn.replace('}', '')
    dataIn = dataIn.replace('\'', '')
    dataIn = dataIn.split('&')
    # dataIn = decs(dataIn)
    # print(dataIn[1])
    # print(str(dec[0])[16:18])
    arr = sorted(dataIn, key=None, reverse=True)
    for key in arr:
        print(key)


def ShowMenu():
    selecM = ''
    while selecM.strip() == '':
        print('---[A]准备答题')
        print('---[B]查看排名')
        print('---[C]退出')
        selecM = input('>>>')
        print(selecM.lower())
        if selecM.lower() == 'a':
            print("开始答题")
            startToAnswer()
        elif selecM.lower() == 'b':
            print("查看排名")
            checkDb()
            ShowMenu()
        elif selecM.lower() == 'c':
            print("退出")
            break
        else:
            print("请按要求输入菜单项")


if __name__ == '__main__':
    # checkDb()
    ShowMenu()
    # homework3.generateCertificate('ssssss',50)
    # homework1.outputImg('timg.jpg')
