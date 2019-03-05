
# -*-coding: utf-8 -*-


class Src() :
    def __init__(self) :
        self.intro = '[소개]\n' + \
                     'Koreatech 학식 메뉴를 알려주는 플러스 친구 입니다!\n' + \
                     '아침, 점심, 저녁 버튼을 누르면 해당하는 메뉴를 알려주고, ' + \
                     '날짜 변경 버튼을 통해다른 날짜의 메뉴도 확인할 수 있습니다!\n' + \
                     '\'자동\' 표시가 되어있을 때는 자동으로 날짜가 선택되는데,' + \
                     '18시 30분 이전에는 오늘 날짜가 선택되고, 이후에는 내일 날짜가 선택됩니다.\n\n' + \
                     '버그 제보나 문의 사항은 1:1 채팅방(하단 링크)을 이용해주시기 바랍니다.\n' + \
                     '감사합니다.'
        self.openchatLink = 'open.kakao.com/o/szgsEkZ'
        self.wday = ['월', '화', '수', '목', '금', '토', '일']
        self.mealTime = ['아침', '점심', '저녁']
        self.mealType = ['한식', '일품', '특식 (전골 / 뚝배기)', '양식', '능수관', '수박여']
        self.keybod = {
            'type' : 'buttons',
            'buttons' : self.mealTime + ['이전 날로 날짜 변경', '다음 날로 날짜 변경', '소개']
        }

src = Src()
