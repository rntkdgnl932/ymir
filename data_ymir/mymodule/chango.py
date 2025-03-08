import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def chango_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import cancle_all, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from potion import potion_buy
    from schedule import myQuest_play_check, myQuest_play_add

    try:

        print("chango_start")
        # 먼저 마을로 와서(세계지도 이용해야할듯...아니면 창고관리인 없는 곳으로 갈수도 있음)
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(10, 30, 160, 80, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            cancle_all(cla)
            chango_maul_spot(cla)
        else:
            go_chango(cla)

        # 창고지기 와서

        # 시간템 제외하고 싹다 넣고끝끝

    except Exception as e:
        print(e)
        return 0



def go_chango(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, macro_out
    from clean_screen import clean_screen_start
    from game_check import error_check
    try:
        print("go_chango")

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("chango_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\asgard_castle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 30, 550, 80, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("asgard_castle")

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\personal_chango_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 200, 960, 1040, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("personal_chango_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\im_move_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 980, 880, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("im_move_btn")
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        error_check(cla)

                    for i in range(5):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\asgard_castle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 30, 550, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("asgard_castle")
                        else:
                            is_spot = True

                            time.sleep(5)

                            chango_maul_spot(cla)

                            break
                        time.sleep(1)

                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\sangin_npc.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 200, 960, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("sangin_npc")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        click_pos_2(60, 85, cla)
            else:
                result_out = out_check(cla)
                if result_out == True:

                    # 마을은 클릭위치 다름....

                    click_pos_2(100, 50, cla)

                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\whole_map.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(380, 460, 540, 540, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("whole_map", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\asgard.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(430, 500, 550, 550, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("asgard")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(2)

                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\whole_map_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 30, 120, 70, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("whole_map_title", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)
                            else:
                                clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
            print(e)
            return 0

def chango_maul_spot(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import go_maul
    from clean_screen import clean_screen_start
    from get_item import get_item_start

    try:
        print("chango_maul_spot")

        is_chango = False
        is_chango_count = 0
        while is_chango is False:
            is_chango_count += 1
            if is_chango_count > 10:
                is_chango = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : chango")


                # 바로 넣기 확인
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\baro_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 990, 940, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("baro_on", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\baro_off.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 990, 940, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("baro_off", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)


                # 재료 넣기 준비

                click_pos_2(850, 130, cla)
                time.sleep(1)

                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\jaelyo_in_ready.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(125, 100, 210, 160, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("jaelyo_in_ready", imgs_)
                        break
                    else:
                        click_pos_2(850, 130, cla)
                    time.sleep(1)



                chango_in(cla)
                is_chango = True

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\maul_personal_chango_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("maul_personal_chango_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
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
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\maul_personal_chango_btn.PNG"
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
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\asgard_maul_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 140, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("이동중")
                            drag_pos(90, 180, 90, 75, cla)
                            time.sleep(1)
                        else:
                            click_pos_2(190, 55, cla)
                    else:
                        go_maul(cla)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
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

def chango_in(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from potion import potion_buy
    from schedule import myQuest_play_check, myQuest_play_add

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:
        print("chango_in")

        x_reg_1 = 0
        y_reg_1 = 0

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\bag_time_item.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_for = imgs_set_for(730, 110, 960, 1000, cla, img, 0.8)
        if imgs_for is not None and imgs_for != False:
            print("bag_time_item", imgs_for)

            if len(imgs_for) > 0:
                x_reg_1 = imgs_for[len(imgs_for) - 1][0]
                y_reg_1 = imgs_for[len(imgs_for) - 1][1]
                # for i in range(len(imgs_for)):
                #     click_pos_reg(imgs_for[i][0] - 15, imgs_for[i][1] + 15, cla)
                #     time.sleep(1)
        if x_reg_1 != 0:
            print("x_reg_1", x_reg_1)
            print("y_reg_1", y_reg_1)
            if x_reg_1 < 900 + plus:
                x_reg_1 = x_reg_1 + 40
            else:
                x_reg_1 = 735 + plus
                y_reg_1 = y_reg_1 + 70

            for i in range(20):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\chango_max_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(570, 520, 650, 590, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("chango_max_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(550, 610, cla)
                else:
                    click_pos_reg(x_reg_1, y_reg_1, cla)
                time.sleep(0.5)
        else:
            print("clean")
            x_reg_1 = 735
            y_reg_1 = 175
            for i in range(20):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\chango_max_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(570, 520, 650, 590, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("chango_max_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(550, 610, cla)
                else:
                    click_pos_2(x_reg_1, y_reg_1, cla)
                time.sleep(0.5)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\bag_auction_item.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(730, 110, 960, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("bag_auction_item", imgs_)
            y_reg_2 = imgs_.y

    except Exception as e:
        print(e)
        return 0


def chango_maul_auction(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import go_maul
    from clean_screen import clean_screen_start
    from get_item import get_item_start

    try:
        print("chango_maul_auction")

        is_chango = False
        is_chango_count = 0
        while is_chango is False:
            is_chango_count += 1
            if is_chango_count > 10:
                is_chango = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : chango")

                # 바로 넣기 확인
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\baro_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(860, 990, 940, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("baro_on", imgs_)
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\baro_off.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(860, 990, 940, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("baro_off", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                # 재료 빼기
                chango_out(cla)
                is_chango = True

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\maul_personal_chango_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("maul_personal_chango_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
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
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\maul_personal_chango_btn.PNG"
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
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\asgard_maul_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 30, 140, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("이동중")
                            drag_pos(90, 180, 90, 75, cla)
                            time.sleep(1)
                        else:
                            click_pos_2(190, 55, cla)
                    else:
                        go_maul(cla)

            time.sleep(1)
        for i in range(5):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\chango.PNG"
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

def chango_out(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import out_check, juljun_off, juljun_on, juljun_check
    from game_check import move_check
    from potion import potion_buy
    from schedule import myQuest_play_check, myQuest_play_add

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:
        print("chango_out")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\bag_auction_item.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_for = imgs_set_for(20, 140, 250, 1020, cla, img, 0.8)
        if imgs_for is not None and imgs_for != False:
            print("bag_auction_item", imgs_for)

            if len(imgs_for) > 0:
                for i in range(len(imgs_for)):
                    click__ = len(imgs_for) - 1 - i
                    click_pos_reg(imgs_for[click__][0] - 15, imgs_for[click__][1] + 15, cla)
                    time.sleep(1)


    except Exception as e:
        print(e)
        return 0



