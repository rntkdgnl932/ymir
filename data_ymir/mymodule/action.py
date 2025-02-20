import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def out_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:
        is_out = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\out_check\\small_out.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 880, 60, 930, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("small_out")
            small_ui_big_change(cla)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\out_check\\out_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 840, 60, 900, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_check")
            is_out = True



        return is_out
    except Exception as e:
        print(e)
        return 0


def small_ui_big_change(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:

        is_open = False
        is_open_count = 0
        while is_open is False:
            is_open_count += 1
            if is_open_count == 10:
                is_open = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\ui_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 60, 530, 130, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("ui_title")
                is_open = True
                clean_screen_start(cla)
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\small_ui_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 60, 520, 100, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("small_ui_title")
                    click_pos_2(580, 115, cla)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\small_post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 550, 700, 620, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("small_post")
                        click_pos_2(495, 1010, cla)
                    else:
                        click_pos_2(915, 45, cla)
                        time.sleep(0.5)

            time.sleep(1)
    except Exception as e:
        print(e)
        return 0
def menu_open(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:
        is_menu = False
        is_menu_count = 0

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("menu_post")
            is_menu = True

        while is_menu is False:
            is_menu_count += 1
            if is_menu_count > 7:
                is_menu = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("menu_post")
                is_menu = True
            else:

                result_out = out_check(cla)
                if result_out == True:
                    print("out")
                    click_pos_2(915, 45, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0


def confirm_all(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:
        is_confirm = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 540, 600, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1")
            click_pos_reg(imgs_.x, img.y, cla)



        return is_confirm
    except Exception as e:
        print(e)
        return 0