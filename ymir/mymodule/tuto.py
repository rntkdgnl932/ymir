import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check
    from game_check import move_check
    try:
        print("tuto_start")

        result_out = out_check(cla)
        if result_out == True:
            out_check(cla)
            tuto_go(cla)
        else:
            tuto_skip(cla)

    except Exception as e:
        print(e)
        return 0


def tuto_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import confirm_all
    from game_check import move_check
    try:

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\tuto_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(830, 90, 860, 140, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("tuto_ing")
            move_check(cla)
        else:
            is_tuto = False
            is_tuto_count = 0
            while is_tuto is False:
                is_tuto_count += 1
                if is_tuto_count > 10:
                    is_tuto = True

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\ready_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 60, 960, 130, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("ready_quest")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    im_move_not = False

                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\grow\\im_move_not.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 480, 660, 600, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("im_move_not")
                            im_move_not = True
                            break
                        time.sleep(0.1)
                    if im_move_not == True:
                        click_pos_2(800, 115, cla)
                        is_tuto = True
                    else:
                        print("빠른이동 오케이하기")
                        is_tuto = True
                        for i in range(5):
                            result_confirm = confirm_all(cla)
                            if result_confirm == True:
                                break
                            QTest.qWait(1000)
                else:
                    print("물음표??")
                    tuto_skip(cla)
                time.sleep(1)
    except Exception as e:
        print(e)
        return 0

def tuto_skip(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:

        is_skip = False
        is_skip_count = 0
        while is_skip is False:
            is_skip_count += 1
            if is_skip_count > 10:
                is_skip = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\skip\\skip_top_right_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(830, 30, 960, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("skip_top_right_1")
                click_pos_reg(imgs_.x, imgs_.y, cla)

            time.sleep(1)
    except Exception as e:
        print(e)
        return 0