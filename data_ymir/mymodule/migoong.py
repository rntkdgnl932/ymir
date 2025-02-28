import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def migoong_start(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import out_check, juljun_off, juljun_on, juljun_check, confirm_all, attack_check
    from game_check import move_check
    from action import attack_check, chajib_check, attack_on, chajib_on
    from potion import potion_check
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go

    try:
        print("migoong_start", data)

        # 미궁_스비파_5
        # 미궁_카라_5

        read_data = data.split("_")

        # read_data[1] => 스비파, 카라
        # read_data[2] => 층수

        if read_data[1] == "스비파":
            migoong_check(cla, data)
        elif read_data[1] == "카라":
            migoong_check(cla, data)





    except Exception as e:
        print(e)
        return 0
##############################################################################################################################################
##################################################### 미  궁 ##################################################################################
##############################################################################################################################################
def migoong_check(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import out_check, juljun_off, juljun_on, juljun_check, attack_on, attack_check
    from game_check import move_check
    from action import attack_check, chajib_check, attack_on, chajib_on
    from potion import potion_check
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go, clean_screen_start

    try:
        print("migoong_check", data)

        # 미궁_스비파_5
        # 미궁_카라_5

        read_data = data.split("_")

        # read_data[1] => 스비파, 카라
        # read_data[2] => 층수


        if read_data[1] == "스비파":
            des = "sbipa"
        elif read_data[1] == "카라":
            des = 'kara'


        result_juljun = juljun_check(cla)
        if result_juljun == True:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\juljun\\" + str(des) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("migoong juljun :", str(des), imgs_)
                result_attack = attack_check(cla)
                if result_attack == True:
                    potion_check(cla)
                else:
                    random_spot(cla, data)
            else:
                migoong_in(cla, data)
        else:
            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\out\\" + str(des) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 200, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("migoong out :", str(des), imgs_)
                    juljun_on(cla)
                    result_attack = attack_check(cla)
                    if result_attack == True:
                        potion_check(cla)
                    else:
                        random_spot(cla, data)
                else:
                    migoong_in(cla, data)
            else:
                clean_screen_start(cla)
    except Exception as e:
        print(e)
        return 0


#############################################################################################################
#############################################################################################################
#############################################################################################################


#############################################################################################################
############################ 공통 #################################################################
#############################################################################################################
def migoong_in(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import menu_open, out_check
    from schedule import myQuest_play_add


    try:
        print("migoong_in", data)

        # 미궁_스비파_5
        # 미궁_카라_5

        read_data = data.split("_")

        # read_data[1] => 스비파, 카라
        # read_data[2] => 층수

        x_reg_1 = 50
        if read_data[1] == "스비파":
            y_reg_1 = 160
        elif read_data[1] == "카라":
            y_reg_1 = 230


        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("migoong_in_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\migoong.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : balhala", imgs_)

                # 일반



                click_pos_2(x_reg_1, 85, cla)
                time.sleep(0.5)
                click_pos_2(x_reg_1, 85, cla)
                time.sleep(0.5)

                # 스비파,, 카라
                click_pos_2(120, y_reg_1, cla)
                time.sleep(0.5)
                click_pos_2(120, y_reg_1, cla)
                time.sleep(0.5)


                # 스텝 클릭
                step_check(cla, read_data[2])

                # 입장하기 => 여기에서 add 등 처리하깅

                print("입장완료")

                click_pos_2(820, 1010, cla)

                fix = False
                for i in range(10):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\im_fix_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(350, 490, 600, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("im_fix_notice", imgs_)
                        fix = True
                        break
                    time.sleep(0.1)
                if fix == True:
                    myQuest_play_add(cla, data)
                    # 혹시 컨텐츠가 안될수도 있어서 뒤에 자동사냥터 한개 넣기
                else:
                    out_after_notice = False
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out_after_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 510, 540, 570, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("out_after_notice", imgs_)
                            out_after_notice = True
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\migoong.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("title : balhala", imgs_)
                                click_pos_2(820, 1010, cla)
                            else:
                                break
                        time.sleep(0.5)

                    if out_after_notice == True:
                        go_maul(cla)
                    else:
                        is_spot = True
                        for i in range(10):

                            result_out = out_check(cla)
                            if result_out == True:
                                print("미궁입장완료")
                                break
                            else:
                                print("미궁 입장중")
                            time.sleep(1)

                        # 입장했으면 지도 랜덤 가기
                        random_spot(cla, data)




            else:
                menu_open(cla)
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\migoong.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\menu_migoong.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 490, 470, 580, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    QTest.qWait(1000)

            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0


def random_spot(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import out_check, attack_on, juljun_on, juljun_check, confirm_all, attack_check
    from game_check import move_check
    from get_item import get_item_start
    from potion import potion_buy
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_start

    try:
        print("random_spot", data)

        # 미궁_스비파_5
        # 미궁_카라_5

        read_data = data.split("_")

        # read_data[1] => 스비파, 카라
        # read_data[2] => 층수

        ran_x = 650
        ran_y = 725

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_count", is_spot_count)
            if is_spot_count > 30:
                is_spot = True

            if read_data[1] == "스비파":

                if int(read_data[2]) < 4:
                    ran_x = random.randint(290, 650)
                    ran_y = random.randint(400, 720)
                elif int(read_data[2]) < 6:
                    ran_x = random.randint(290, 650)
                    ran_y = random.randint(380, 750)

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\map_sbipa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(190, 30, 400, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("map_sbipa", imgs_)

                is_foot = False

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\foot_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(230, 250, 730, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("foot_point", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_foot = True
                    QTest.qWait(1000)
                else:
                    click_pos_2(ran_x, ran_y, cla)

                if is_foot == True:
                    result_out = out_check(cla)
                    if result_out == True:
                        time.sleep(7)
                        attack_on(cla)
                        juljun_on(cla)
                        result_attack = attack_check(cla)
                        if result_attack == True:
                            is_spot = True

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(85, 50, cla)
                else:
                    clean_screen_start(cla)

            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0

def step_check(cla, step):
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

    step_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\step_num"
    step_list = os.listdir(step_ready)


    try:
        print("step_check", step)



        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\step_num\\" + str(step) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 120, 850, 210, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("step", str(step), imgs_)
                is_spot = True



            else:
                is_now_step = 0
                for i in range(len(step_list)):
                    result_step_list = step_list[i].split(".")
                    read_data = result_step_list[0]
                    print("read_data", read_data)
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\step_num\\" + str(read_data) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 120, 850, 210, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("step", str(read_data), imgs_)
                        is_now_step = int(read_data)
                        if is_now_step == int(step):
                            break
                        elif is_now_step < int(step):
                            click_pos_2(905, 160, cla)
                        elif is_now_step > int(step):
                            click_pos_2(725, 160, cla)
                    QTest.qWait(1000)



            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0




