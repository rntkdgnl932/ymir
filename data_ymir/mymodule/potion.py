import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from get_item import get_item_start


    try:
        print("potion_check")

        is_buy_potion = False

        result_out = out_check(cla)

        if result_out == True:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\out_zero_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(615, 970, 680, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("out_zero_potion")
                v_.potion_count += 1
                if v_.potion_count > 2:
                    juljun_off(cla)
                    potion_buy(cla)
                    is_buy_potion = True

        else:
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\juljun_small_potion.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 920, 680, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_small_potion")
                    v_.potion_count = 0
                else:
                    v_.potion_count += 1
                    if v_.potion_count > 2:
                        juljun_off(cla)
                        potion_buy(cla)
                        is_buy_potion = True

        return is_buy_potion
    except Exception as e:
        print(e)
        return 0


def potion_buy(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import go_maul
    from clean_screen import clean_screen_start
    from get_item import get_item_start

    try:
        print("potion_buy")

        is_potion = False
        is_potion_count = 0
        while is_potion is False:
            is_potion_count += 1
            if is_potion_count > 10:
                is_potion = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\jabhwa_sangin.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : jabhwa_sangin")

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\full_buy_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 490, 600, 600, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        is_potion = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\buy_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 950, 700, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(230, 1010, cla)
                        time.sleep(0.5)

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa_sangin_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\jabhwa_sangin.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("end_btn")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("이동중")
                                    time.sleep(1)
                                else:
                                    break
                        time.sleep(1)
                else:
                    go_maul(cla)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\jabhwa_sangin.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 55, cla)
            else:
                break
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

