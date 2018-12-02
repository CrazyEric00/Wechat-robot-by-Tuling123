import itchat,time
from itchat.content import *
import requests

key='333ea858fc9944aa845f9d6ed05bf0e8'
username='@cf0d952a304097303e303ae2c2c59fffc9252e4b67b36e5c00ca616fbf34ac41'
api='http://www.tuling123.com/openapi/api'

def chat(msg):
    data={
        'key':key,
        'info':msg,
        'userid':'wechat-robot'
    }
    try:
        r=requests.post(api,data=data).json()
        return '机器人回复:'+r.get('text')
    except:
        None

@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def reply(msg):
    print(msg['Text'])
    normal="我的回复:"+msg['Text']
    robot_reply=chat(msg['Text'])
    replymsg=robot_reply or normal
    print(replymsg)
    return replymsg

@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def read(msg):
    # msg.download(msg.fileName)
    # typeSymbol={
    #     PICTURE:'img',
    #     VIDEO:'vid'
    # }.get(msg.type,'fil')
    # return '@%s@%s' % (typeSymbol,msg.fileName)
    return '机器人回复:整天就知道斗图，真傻比'

@itchat.msg_register(FRIENDS)
def add(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send('你好呀！',msg['RecommendInfo']['UserName'])

itchat.auto_login(hotReload=True)
itchat.run(True)
