
from flask import jsonify, request
from Src import src
from Menu import menu
from TimeManager import tm
from DataManager import dm
import time


class Manager() :
    def __init(self) :
        None

    def process(self, s, req = None) :
        '''
        friend
        chat_room
        '''
        if s == 'keyboard' :
            return jsonify(self.keybod()), 200
        elif s == 'message' :
            print(req)

            if tm.update() :
                menu.update()
            
            # req['content'] == usually '아침', '점심', '저녁'
            content = req['content']
            if content[:2] == '아침' :
                content = '아침'

            # response
            resp = dict()
            resp['keyboard'] = self.keybod()

            if content in src.mealTime :
                resp['message'] = {'text' : menu.getMeal(content)}
            else :
                resp['message'] = {'text' : '아직 구현되지 않은 기능입니다....\n' + \
                                   '사용에 불편을 끼쳐드려 죄송합니다 ㅠㅠ'}
            return jsonify(resp), 200
        elif s == 'addFriend' :
            dm.addUser(req['user_key'])
            return '', 200
        elif s == 'removeFriend' or s == 'exitChatRoom':
            dm.removeUser(req)
            return '', 200
        else :
            return jsonify(self.keybod()), 200

    # keybod = {'type' : 'buttons', 'buttons' : self.mealTime + ...}
    # type(structTime) == time.struct_time == type(tm.mainTime.st)
    # when call keybod function, must jsonify return value
    def keybod(self, structTime = None) :
        tm.update()
        if structTime == None :
            structTime = tm.mainTime.st
        wday = ['월', '화', '수', '목', '금', '토', '일']
        keybod = src.keybod.copy()
        keybod['buttons'][0] = ('아침 - ' + str(structTime[1]) + '.' + str(structTime[2]) + \
                                '(' + str(wday[structTime[6]]) + ')')
        return keybod

manager = Manager()
