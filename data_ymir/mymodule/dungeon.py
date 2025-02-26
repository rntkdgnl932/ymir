import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def dungeon_start(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import out_check, juljun_off, juljun_on, juljun_check, confirm_all, attack_check
    from game_check import move_check
    from get_item import get_item_start
    from potion import potion_buy
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go
    try:
        print("dungeon_start", data)

        # 던전_일반_발키리_4 // 특수
        # 던전_일반_혼돈_5 // 특수
        # 던전_일반_폴크방_5 // 특수

        read_data = data.split("_")
        # read_data[1] => 일반, 특수
        # read_data[2] => 발키리, 혼돈, 폴크방
        # read_data[3] => 층수
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("end_btn")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\cancle_all\\cancle_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(340, 540, 480, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("cancle_btn")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\juljun\\juljun_middle_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 920, 680, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_potion")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("click_request_btn", imgs_)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_complete_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("request_complete_btn", imgs_)


    except Exception as e:
        print(e)
        return 0
def dungeon_in(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import menu_open, juljun_off, juljun_on, juljun_check, confirm_all, attack_check
    from game_check import move_check
    from get_item import get_item_start
    from potion import potion_buy
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go


    try:
        print("dungeon_in", data)



        data = "의뢰_1"

        result_request_step = data.split("_")
        y_reg_1 = 140
        # result_request_step[1] => step
        if result_request_step[1] == "1":
            print("의뢰_이둔골짜기")
        elif result_request_step[1] == "2":
            print("레이븐스홀")
            y_reg_1 = 175
        elif result_request_step[1] == "3":
            print("아스가르드성")
            y_reg_1 = 215
        elif result_request_step[1] == "4":
            print("헤르모드의갈림길")
            y_reg_1 = 250

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\balhala.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : balhala", imgs_)




            else:
                menu_open(cla)
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\balhala.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        

                        QTest.qWait(1000)

            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0


