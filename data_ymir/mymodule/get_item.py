import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from chango import chango_start

    print("get_item_start")

    try:
        chango_start(cla)

        get_post(cla)
        get_upjuk(cla)
        get_sangjum_gyohwan(cla)


    except Exception as e:
        print(e)
        return 0

def get_post(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check, menu_open
    try:
        print("get_post")

        this_point_x = 720
        this_point_y = 573
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : post")
                click_pos_2(870, 100, cla)
                time.sleep(0.2)

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 80, 160, 330, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("post_point_1", imgs_)
                        click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 100, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 100, cla)
                        time.sleep(0.2)
                    else:
                        break
                    QTest.qWait(500)
                is_get = True
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(20, 50, cla)
                    else:
                        break
                    time.sleep(1)

            else:
                menu_open(cla)
                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                          this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_2")
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0




def get_upjuk(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check, menu_open
    try:
        print("get_upjuk")

        this_point_x = 540
        this_point_y = 573
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : upjuk")
                click_pos_2(870, 100, cla)
                is_get = True
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\upjuk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(20, 50, cla)
                    else:
                        break
                    time.sleep(1)

            else:
                menu_open(cla)
                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\upjuk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                          this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_2")
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


def get_sangjum_gyohwan(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check, menu_open
    from clean_screen import clean_screen_start
    try:
        print("get_sangjum_gyohwan")

        this_point_x = 350
        this_point_y = 573
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : sangjum")
                is_get = True

                # 소환하러 클릭하기
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\sohwan_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 110, 100, 150, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(110, 85, cla)
                    time.sleep(1)
                # 발키리 소환
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\sohwan_soldout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 300, 450, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("발키리품절")
                else:
                    for i in range(7):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\product_buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 550, 390, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\buy_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 680, 620, 750, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(620, 640, 700, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\buy_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 680, 620, 750, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                        else:
                            click_pos_2(390, 350, cla)
                        time.sleep(1)

                # 디시르 소환
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\sohwan_soldout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 300, 930, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("디시르품절")
                else:
                    for i in range(7):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\product_buy_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 550, 390, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\buy_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 680, 620, 750, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(620, 640, 700, 700, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(1)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\buy_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 680, 620, 750, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                break
                        else:
                            click_pos_2(870, 350, cla)
                        time.sleep(1)
                # 다 샀으면 나가기
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\sangjum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(20, 50, cla)
                    else:
                        break
                    time.sleep(0.3)

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(830, 55, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)
                else:
                    clean_screen_start(cla)
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0




def get_daily_mission(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open
    try:
        print("get_daily_mission")

        this_point_x = 450
        this_point_y = 448
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daily_mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : daily_mission")
                click_pos_2(870, 130, cla)
                is_get = True
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daily_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(20, 50, cla)
                    else:
                        break
                    time.sleep(1)

            else:
                menu_open(cla)
                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\daily_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                          this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_2")
                            click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0







