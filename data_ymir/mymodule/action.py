import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

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
    try:
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

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("end_btn")
            click_pos_reg(imgs_.x, imgs_.y, cla)

        is_confirm = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 540, 600, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1")
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\soolock_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 540, 650, 750, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("soolock_1")
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_confirm = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\confirm_all\\select_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 540, 650, 750, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("select_1")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_confirm = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 655, 960, 710, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("request_confirm", imgs_)
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
        imgs_ = imgs_set_(340, 540, 480, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("cancle_btn")
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
                imgs_ = imgs_set_(370, 655, 480, 710, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("request_cancle", imgs_)
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
    try:
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
            print("juljun_on")
            for i in range(10):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\juljun\\juljun_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 100, 600, 160, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_on")
                    drag_pos(370, 500, 850, 500, cla)
                    QTest.qWait(1000)
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
    from function_game import imgs_set_, click_pos_reg, click_pos_2
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
        click_pos_2(750, 960, cla)

    except Exception as e:
        print(e)
        return 0


def go_maul(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
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
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\near_aim_spot_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 500, 530, 580, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("near_aim_spot_notice")
                            near_aim_spot = True
                            break
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
                                click_pos_2(190, 55, cla)
                            QTest.qWait(1000)

                else:
                    clean_screen_start(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0






