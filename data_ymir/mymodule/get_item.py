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
    from upgrade import upgrade_start

    print("get_item_start")

    try:
        chango_start(cla)

        # get_just_wonjung(cla)

        get_event(cla)
        get_pass(cla)
        get_post(cla)
        get_main(cla)
        get_upjuk(cla)
        get_daily_mission(cla)
        get_sangjum_gyohwan(cla)

        upgrade_start(cla)

    except Exception as e:
        print(e)
        return 0



def get_just_wonjung(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    from boonhae_collection import boonhae_collection_start
    try:
        print("get_just_wonjung")

        # 보스 원정
        just_wonjung_in_out(cla, "boss")

        # # 레이드 원정
        just_wonjung_in_out(cla, "raid")

    except Exception as e:
        print(e)
        return 0

def just_wonjung_in_out(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure, dun_out, out_check, macro_out, confirm_all
    from game_check import loading_check, dun_check
    from massenger import line_to_me

    try:
        print("just_wonjung_in_out", data)

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 20:
                is_get = True
                why = "원정에 문제 있다 1"
                line_to_me(cla, why)
                macro_out(cla)


            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\wonjung_mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(775, 75, 875, 115, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("wonjung_mission", imgs_)

                click_pos_2(195, 55, cla)
                time.sleep(1)
                confirm_all(cla)

                is_dun = True
                is_dun_count = 0
                while is_dun is True:
                    is_dun_count += 1
                    if is_dun_count > 100:
                        is_get = True
                        is_dun = False
                        why = "원정에 문제 있다 2"
                        line_to_me(cla, why)
                        macro_out(cla)
                    if is_dun_count % 5 == 0:
                        print("dun_out", str(is_dun_count), "초")
                    result_out = out_check(cla)
                    if result_out == True:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\wonjung_mission.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(775, 75, 875, 115, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            result_confirm = confirm_all(cla)
                            if result_confirm == False:
                                click_pos_2(195, 55, cla)
                                time.sleep(1)
                                confirm_all(cla)

                        else:
                            is_dun = False
                            is_get = True
                    QTest.qWait(1000)

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\wonjung.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("title : wonjung")


                    if data == "boss":
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\hogny.PNG"
                    if data == "raid":
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\yarn_hamash.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 240, 900, 310, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("hogny", imgs_)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\wonjung_information_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("wonjung_create_title", imgs_)
                            click_pos_2(690, 700, cla)

                            for i in range(15):
                                result_out = out_check(cla)
                                if result_out == True:
                                    break
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\wonjung_information_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("wonjung_create_title", imgs_)
                                        click_pos_2(690, 700, cla)
                                    else:
                                        loading_check(cla)
                                QTest.qWait(1000)

                        else:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\wonjung_create_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("wonjung_create_title", imgs_)
                                click_pos_2(480, 730, cla)
                            else:
                                click_pos_2(880, 1020, cla)
                    else:
                        if data == "boss":
                            click_pos_2(50, 85, cla)
                        if data == "raid":
                            click_pos_2(150, 85, cla)


                else:

                    is_in = False
                    for i in range(5):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\wonjung.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            is_in = True
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_wonjung.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 550, 430, 640, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("menu_wonjung", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                menu_open_pure(cla)
                        time.sleep(1)
                    if is_in == False:
                        is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0


def get_event(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import out_check
    from clean_screen import clean_screen_start
    try:
        print("get_event")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 10:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\event.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 350, 530, 400, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : event")

                is_title_point = False
                this_point_name = "none"


                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("event_title_point_1", imgs_)

                    is_title_point = True
                    this_point_name = "event_title_point_1"

                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                    time.sleep(0.5)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("event_title_point_2", imgs_)
                        is_title_point = True
                        this_point_name = "event_title_point_2"
                        click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                        time.sleep(0.5)

                if is_title_point == True:
                    for i in range(15):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\" + str(this_point_name) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_des_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 500, 810, 720, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("event_des_point_1", imgs_)
                                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_des_point_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(340, 500, 810, 720, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("event_des_point_2", imgs_)
                                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                    time.sleep(0.5)
                                    click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                    time.sleep(0.5)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_des_point_3.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(340, 500, 810, 720, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("event_des_point_3", imgs_)
                                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                        time.sleep(0.5)
                                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                        time.sleep(0.5)
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_des_point_4.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(340, 500, 810, 720, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("event_des_point_4", imgs_)
                                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                            time.sleep(0.5)
                                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                            time.sleep(0.5)
                                        else:
                                            break

                        else:
                            break
                        time.sleep(0.5)

                else:
                    is_point = False
                    for i in range(3):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            is_point = True
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                is_point = True
                                break
                            else:
                                drag_pos(220, 680, 220, 420, cla)
                        QTest.qWait(1000)
                    if is_point == False:
                        is_get = True

            else:
                result_out = out_check(cla)
                if result_out == True:
                    for i in range(5):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\event.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 350, 530, 400, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            click_pos_2(230, 55, cla)
                        time.sleep(1)
                else:
                    clean_screen_start(cla)

            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0


def get_pass(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import out_check
    from clean_screen import clean_screen_start
    try:
        print("get_pass")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 10:
                is_get = True
                clean_screen_start(cla)
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\pass.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 350, 540, 400, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : pass")

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("event_title_point_1", imgs_)
                    click_pos_reg(imgs_.x - 50, imgs_.y + 15, cla)
                    time.sleep(0.5)
                    click_pos_2(765, 695, cla)
                    time.sleep(0.5)
                    click_pos_2(765, 695, cla)
                    time.sleep(0.5)

                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        is_get = True
                    else:
                        clean_screen_start(cla)

            else:
                result_out = out_check(cla)
                if result_out == True:
                    for i in range(5):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\pass.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 350, 540, 400, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            click_pos_2(270, 55, cla)
                        time.sleep(1)
                else:
                    clean_screen_start(cla)

            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0

def get_post(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    from boonhae_collection import boonhae_collection_start
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

                is_collection = False

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\bag_lack_of_space.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 510, 600, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("bag_lack_of_space", imgs_)
                        is_collection = True
                        boonhae_collection_start(cla)
                        break
                    QTest.qWait(500)
                if is_collection == False:
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
                            for c in range(5):
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\post.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(20, 50, cla)
                                else:
                                    is_get = True
                                    break
                                time.sleep(1)
                        QTest.qWait(500)





            else:

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
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0




def get_main(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure
    try:
        print("get_main")

        this_point_x = 355
        this_point_y = 450
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\main.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : main")
                is_get = True

                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\main_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(115, 75, 140, 1020, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\main.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(870, 1010, cla)
                            time.sleep(0.5)
                            click_pos_2(870, 1010, cla)
                    else:
                        break
                    time.sleep(1)

            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\main.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)
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
    from action import menu_open_pure
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
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)
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
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import out_check, menu_open_pure
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

                ########################################################
                #######################특별##############################
                ########################################################
                # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(0, 110, 100, 150, cla, img, 0.9)
                # if imgs_ is not None and imgs_ != False:


                ########################################################
                #######################기본##############################
                ########################################################

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
                # 11개
                # 발키리 소환
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\sohwan_soldout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 730, 450, 830, cla, img, 0.8)
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
                            click_pos_2(390, 770, cla)
                        time.sleep(1)
                # 11개
                # 디시르 소환
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\sohwan_soldout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 730, 930, 830, cla, img, 0.8)
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
                            click_pos_2(870, 770, cla)
                        time.sleep(1)
                #
                # 마나재생물약

                # 소모품 클릭하기

                is_somopoom = False
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\moogi_ganghwasuk_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(270, 110, 500, 210, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_somopoom = True
                        break
                    else:
                        click_pos_2(30, 210, cla)
                    time.sleep(1)
                if is_somopoom == True:

                    x_reg = 0
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\mana_potion_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(160, 110, 950, 210, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("mana_potion_1", imgs_)
                            x_reg = imgs_.x
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\right_drag_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(160, 110, 950, 210, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(760, 350, 370, 350, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\right_drag_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(160, 110, 950, 210, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    drag_pos(760, 350, 370, 350, cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\left_drag_1.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(160, 110, 950, 210, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        drag_pos(370, 350, 760, 350, cla)
                        QTest.qWait(1000)
                    if x_reg != 0:
                        # 위에꺼
                        for i in range(7):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\soldout_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 510, 600, 580, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("top soldout_notice", imgs_)
                                break

                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\not_buy_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 510, 600, 580, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("top not_buy_notice", imgs_)
                                    break
                                else:
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
                                        click_pos_2(x_reg, 350, cla)
                            time.sleep(0.5)
                        # 밑에꺼
                        for i in range(7):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\soldout_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 510, 600, 580, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("bottom soldout_notice", imgs_)
                                break

                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\not_buy_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(400, 510, 600, 580, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("bottom not_buy_notice", imgs_)
                                    break
                                else:
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
                                        click_pos_2(x_reg, 770, cla)
                            time.sleep(0.5)
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

                ########################################################
                ########################################################
                ########################################################

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
    from action import menu_open_pure
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
                time.sleep(0.5)
                click_pos_2(870, 130, cla)
                time.sleep(0.5)
                click_pos_2(440, 105, cla)
                time.sleep(0.5)
                click_pos_2(440, 105, cla)
                time.sleep(0.5)
                click_pos_2(770, 105, cla)
                time.sleep(0.5)
                click_pos_2(770, 105, cla)
                time.sleep(0.5)
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
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_2")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(0.5)
                    QTest.qWait(1000)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)
        return 0







