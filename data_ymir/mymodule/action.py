import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

this_point_x_plus = 80

def macro_out(cla):
    import numpy as np
    import cv2
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:
        dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
        file_path = dir_path + "\\start.txt"
        # cla.txt
        cla_data = str(cla) + "cla"
        file_path2 = dir_path + "\\" + cla_data + ".txt"
        with open(file_path, "w", encoding='utf-8-sig') as file:
            data = 'no'
            file.write(str(data))
            time.sleep(0.2)
        with open(file_path2, "w", encoding='utf-8-sig') as file:
            data = cla
            file.write(str(data))
            time.sleep(0.2)
        os.execl(sys.executable, sys.executable, *sys.argv)



    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from dead_die import dead_recovery
    try:
        # print("out_check")
        is_out = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\out_check\\small_out.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 800, 60, 930, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("small_out")
            small_ui_big_change(cla)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\out_check\\out_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 800, 60, 900, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_check", imgs_)
            is_out = True

        if is_out == True:
            is_out = close_check(cla)

        # if is_out == True:
        #     full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dead_die\\out_dead_point.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(400, 850, 560, 900, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("out_dead_point", imgs_)
        #         dead_recovery(cla)


        return is_out
    except Exception as e:
        print(e)
        return 0

def close_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from dead_die import dead_recovery
    try:
        # print("out_check")
        is_out = True

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("out_check close_1 : ", imgs_, len(imgs_))
            is_out = False
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("out_check close_2 : ", imgs_)
                is_out = False
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_3.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("out_check close_3 : ", imgs_)
                    is_out = False
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 550, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("out_check close_4 1: ", imgs_)
                        is_out = False
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\clean_screen\\close_4.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(610, 30, 960, 1040, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("out_check close_4 1: ", imgs_)
                            is_out = False
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(650, 550, 850, 650, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("out_check : menu_post", imgs_)
                                is_out = False
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\18\\event_1818.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 0, 960, 1040, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("out_check event_1818 : ", imgs_)
                                    is_out = False


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
    from get_item import get_post, get_daily_mission
    from massenger import line_to_me
    from guild import guild_check

    from schedule import myQuest_play_check
    from character_select_and_game_start import character_change

    try:

        is_post = False

        plus_minus = 20

        is_menu = False
        is_menu_count = 0


        while is_menu is False:
            is_menu_count += 1

            print("is_menu_count..is_menu_count...", is_menu_count)

            if 8 < is_menu_count < 11:
                print("메뉴 안 열려??")

                dun_out(cla)

            elif is_menu_count > 11:
                print("이레도 메뉴 안 열려??")
                why = "메뉴 안 열려"
                line_to_me(cla, why)
                macro_out(cla)

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 550, 850, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_post(menu_open)")
                    this_point_x = 720 + this_point_x_plus
                    this_point_y = 510
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                      this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_open : guild_check")
                        guild_check(cla)
                        is_menu_count = 0


                    else:
                        this_point_x = 450 + this_point_x_plus
                        this_point_y = 448
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                          this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_open : get_daily_mission")
                            get_daily_mission(cla)
                            is_menu_count = 0
                        else:
                            this_point_x = 720 + this_point_x_plus
                            this_point_y = 573
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\menu_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_open : get_post")
                                get_post(cla)
                                is_menu_count = 0
                            else:

                                is_menu = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        result_schedule = myQuest_play_check(v_.now_cla, "check")
                        character_id = result_schedule[0][1]
                        character_change(cla, character_id)
                    else:
                        confirm_all(cla)
                        clean_screen_start(cla)
                        click_pos_2(915, 45, cla)
                    # result_out = out_check(cla)
                    # print("menu__open,, result_out", result_out)
                    # if result_out == True:
                    #     print("out")
                    #     result_confirm = confirm_all(cla)
                    #     if result_confirm == True:
                    #         time.sleep(0.5)
                    #     click_pos_2(915, 45, cla)
                    # else:
                    #     clean_screen_start(cla)
            QTest.qWait(1000)



    except Exception as e:
        print(e)
        return 0


def menu_open_pure(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    from massenger import line_to_me
    from schedule import myQuest_play_check
    from character_select_and_game_start import character_change

    try:


        is_menu = False
        is_menu_count = 0

        while is_menu is False:
            is_menu_count += 1
            if 8 < is_menu_count < 11:
                print("메뉴 안 열려??")

                dun_out(cla)

            elif is_menu_count > 11:
                print("이레도 메뉴 안 열려??")
                why = "메뉴 안 열려"
                line_to_me(cla, why)
                macro_out(cla)

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 550, 850, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_post")
                    is_menu = True
                else:


                    result_out = out_check(cla)
                    if result_out == True:
                        print("out")
                        result_confirm = confirm_all(cla)
                        if result_confirm == True:
                            time.sleep(0.5)
                        click_pos_2(915, 45, cla)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            result_schedule = myQuest_play_check(v_.now_cla, "check")
                            character_id = result_schedule[0][1]
                            character_change(cla, character_id)
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

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\pass.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 350, 550, 400, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("confirm_all : pass")
            cancle_all(cla)

        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("confirm_all : sangjum")
                cancle_all(cla)

            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 570, 750, 750, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("end_btn")
                    click_pos_reg(imgs_.x, imgs_.y, cla)



                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 540, 750, 750, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("confirm_1")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_confirm = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\soolock_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 540, 750, 750, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("soolock_1")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_confirm = True
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\select_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 540, 750, 750, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("select_1")
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            is_confirm = True
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 655, 750, 750, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("request_confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                is_confirm = True
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\move_btn_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(470, 570, 750, 750, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_btn_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_confirm = True
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\out_btn_545_595.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 400, 740, 700, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("out_btn_545_595", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        is_confirm = True


        return is_confirm
    except Exception as e:
        print(e)
        return 0


def cancle_all(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:
        is_cancle = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\cancle_all\\cancle_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(340, 530, 480, 750, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("cancle_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_cancle = True
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("end_btn")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_cancle = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 530, 560, 750, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("request_cancle", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_cancle = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\boonhae_collection\\cancle_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 530, 560, 750, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("boonhae cancle_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_cancle = True



        return is_cancle
    except Exception as e:
        print(e)
        return 0

def juljun_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import error_check2
    try:
        error_check2(cla)

        is_juljun = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 100, 600, 160, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on")
            is_juljun = True

        return is_juljun
    except Exception as e:
        print(e)
        return 0


def juljun_time_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from auction_game import auction_fast_start
    try:

        num = ""
        for i in range(10):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\juljun_time\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(425, 60, 455, 110, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                num += str(i)

        for i in range(10):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\juljun_time\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(455, 60, 485, 110, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                num += str(i)

        for i in range(10):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\game_check\\juljun_time\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(475, 60, 505, 110, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                num += str(i)

        print("juljun_time_check????", num)
        if len(num) > 2:
            if int(num[0]) % 3 == 0:
                if num[1] == "0" and num[2] == "0":
                    auction_fast_start(cla)
    except Exception as e:
        print(e)
        return 0

def fix_bag(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from boonhae_collection import boonhae_collection_start
    try:
        for i in range(10):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\juljun\\lack_of_space.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 160, 100, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("lack_of_space")
                boonhae_collection_start(cla)
                juljun_on(cla)
                break
            time.sleep(0.1)


    except Exception as e:
        print(e)
        return 0

def juljun_on(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:

        for i in range(10):
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 100, 600, 160, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on")
                break
            else:
                result_out = out_check(cla)
                if result_out == False:
                    clean_screen_start(cla)
                else:
                    click_pos_2(205, 965, cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0

def juljun_off(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, drag_pos, click_pos_2
    try:
        print("juljun_off")
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 100, 600, 160, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            for i in range(10):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\juljun\\juljun_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 100, 600, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_on")
                    drag_pos(370, 500, 850, 500, cla)
                else:
                    break
                QTest.qWait(1000)
    except Exception as e:
        print(e)
        return 0


def attack_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, text_check_get_black_white, click_pos_2
    try:
        is_data = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\attack.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("attack")

            result_get_1 = text_check_get_black_white(25, 85, 170, 110, cla)
            print("attack : result_get_1", result_get_1)

            for i in range(30):
                result_get_2 = text_check_get_black_white(25, 85, 170, 110, cla)
                print("result_get_2", result_get_2)
                if result_get_1 != result_get_2:
                    is_data = True
                    break
                time.sleep(1)

            print("attack : last result", result_get_1, result_get_2)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\ready.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("ready")
            is_data = False


        return is_data
    except Exception as e:
        print(e)
        return 0

def attack_check_mission(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, text_check_get_black_white, click_pos_2
    try:
        is_data = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\attack.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("attack")

            is_data = True


        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\ready.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("ready")
            is_data = False


        return is_data
    except Exception as e:
        print(e)
        return 0

def chaejib_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:
        is_data = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\chajib_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # print("chajib_ing")
            is_data = True

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\ready.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("ready")
            is_data = False


        return is_data
    except Exception as e:
        print(e)
        return 0


def bag_open_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    try:
        is_data = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\bag_refresh_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(770, 980, 870, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("bag_refresh_btn")
            is_data = True


        return is_data
    except Exception as e:
        print(e)
        return 0


def bag_open(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:
        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\tuto\\story\\bag_refresh_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(770, 980, 870, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("bag_refresh_btn")
                is_data = True
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(870, 55, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)


        return is_data
    except Exception as e:
        print(e)
        return 0

def attack_on(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:
        print("attack_on")
        clean_screen_start(cla)
        click_pos_2(750, 965, cla)

    except Exception as e:
        print(e)
        return 0


def chaejib_on(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:
        print("chajib_on")
        result_out = out_check(cla)
        if result_out == False:
            clean_screen_start(cla)

        click_pos_2(770, 1000, cla)

    except Exception as e:
        print(e)
        return 0


def go_maul(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from clean_screen import clean_screen_start
    from auction_game import auction_fast_start
    try:
        print("go_maul")

        is_maul = False
        is_maul_count = 0
        while is_maul is False:
            is_maul_count += 1
            if is_maul_count > 7:
                is_maul = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                is_maul = True
                confirm_all(cla)

            else:

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\out_maul_go.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 920, 710, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_maul_go")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    near_aim_spot = False
                    unusable_item_notice = False
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\near_aim_spot_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 500, 530, 580, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("near_aim_spot_notice")
                            near_aim_spot = True
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\go_maul\\unusable_item_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 500, 750, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("unusable_item_notice", imgs_)
                                unusable_item_notice = True
                        time.sleep(0.2)

                    if near_aim_spot == True:
                        for i in range(4):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\maul_personal_chango_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("maul_personal_chango_btn")
                                    drag_pos(90, 75, 90, 180, cla)
                                    time.sleep(1)
                                else:
                                    click_pos_2(190, 55, cla)
                            QTest.qWait(1000)
                    elif unusable_item_notice == True:
                        for i in range(5):

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\go_maul\\move_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(450, 550, 660, 660, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("move_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                click_pos_2(195, 55, cla)
                            QTest.qWait(1000)
                else:
                    clean_screen_start(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0


def go_maul_pure(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from clean_screen import clean_screen_start
    from auction_game import auction_fast_start
    try:
        print("go_maul_pure")

        is_maul = False
        is_maul_count = 0
        while is_maul is False:
            is_maul_count += 1
            if is_maul_count > 7:
                is_maul = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                is_maul = True
                confirm_all(cla)

            else:

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\out_maul_go.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 920, 710, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("out_maul_go")
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    near_aim_spot = False
                    unusable_item_notice = False
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\near_aim_spot_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 500, 530, 580, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("near_aim_spot_notice")
                            near_aim_spot = True
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\go_maul\\unusable_item_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 500, 750, 600, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("unusable_item_notice", imgs_)
                                unusable_item_notice = True
                        time.sleep(0.2)

                    if near_aim_spot == True:
                        for i in range(4):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\maul_personal_chango_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("maul_personal_chango_btn")
                                    drag_pos(90, 75, 90, 180, cla)
                                    time.sleep(1)
                                else:
                                    click_pos_2(190, 55, cla)
                            QTest.qWait(1000)
                    elif unusable_item_notice == True:
                        for i in range(5):

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\go_maul\\move_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(450, 550, 660, 660, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("move_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                click_pos_2(195, 55, cla)
                            QTest.qWait(1000)
                else:
                    clean_screen_start(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0

def dun_out(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import dun_check
    try:



        is_dun = dun_check(cla)
        is_dun_count = 0

        while is_dun is True:
            is_dun_count += 1
            print("dun_out", is_dun_count)
            is_dun = dun_check(cla)
            if is_dun == True:
                result_confirm = confirm_all(cla)
                if result_confirm == False:
                    click_pos_2(195, 55, cla)

            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0



