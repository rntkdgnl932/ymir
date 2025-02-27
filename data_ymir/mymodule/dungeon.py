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
    from action import attack_check, chajib_check, attack_on, chajib_on
    from potion import potion_check
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("dungeon_start", data)

        # 발할라_일반_발키리_4_보스, 협력, 앰버, 경험, 황금, (시작) // 특수
        # 발할라_일반_혼돈_5 // 특수
        # 발할라_일반_폴크방_5 // 특수

        read_data = data.split("_")
        # read_data[1] => 일반, 특수
        # read_data[2] => 발키리, 혼돈, 폴크방
        # read_data[3] => 층수
        # read_data[4] => 보스, 협력, 앰버, 경험, 황금, (시작)

        if read_data[0] == "발할라":
            if read_data[2] == "발키리":
                dungeon_balkeyly(cla, data)
            elif read_data[2] == "혼돈":
                dungeon_balkeyly(cla, data)
            elif read_data[2] == "폴크방":
                dungeon_balkeyly(cla, data)

        elif read_data[0] == "미궁":
            if read_data[2] == "발키리":
                dungeon_balkeyly(cla, data)





    except Exception as e:
        print(e)
        return 0
##############################################################################################################################################
##################################################### 발키리 ##################################################################################
##############################################################################################################################################
def dungeon_balkeyly(cla, data):
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

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("dungeon_start", data)

        # 발할라_일반_발키리_4_보스, 협력, 앰버, 경험, 황금, (시작) // 특수
        # 발할라_일반_혼돈_5 // 특수
        # 발할라_일반_폴크방_5 // 특수

        read_data = data.split("_")
        # read_data[1] => 일반, 특수
        # read_data[2] => 발키리, 혼돈, 폴크방
        # read_data[3] => 층수
        # read_data[4] => 보스, 협력, 앰버, 경험, 황금, (시작)

        if read_data[4] == "보스":
            des = "boss_room"
        elif read_data[4] == "협력":
            des = 'cooperate_room'
        elif read_data[4] == "앰버":
            des = "amber_room"
        elif read_data[4] == "경험":
            des = "exp_room"
        elif read_data[4] == "황금":
            des = "gold_room"

        result_juljun = juljun_check(cla)
        if result_juljun == True:

            for i in range(len(juljun_ready_list)):
                result_list = juljun_ready_list[i].split(".")
                read_data = result_list[0]
                print("read_data", read_data)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\juljun\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\juljun\\" + str(des) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("good")
                        if str(des) == "amber_room":

                            for x in range(60):
                                result_chajib = chajib_check(cla)
                                if result_chajib == False:
                                    juljun_off(cla)
                                    break
                                time.sleep(10)

                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\juljun\\amber_room.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                chajib_on(cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out\\amber_room.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    chajib_on(cla)

                        else:
                            result_attack = attack_check(cla)
                            if result_attack == True:
                                print("굿굿")
                                potion_check(cla)
                            else:
                                attack_on(cla)
                    else:
                        print("방 옮기자")
                        my_room_check(cla, des)

        else:
            result_out = out_check(cla)
            if result_out == True:
                for i in range(len(out_ready_list)):
                    result_list = out_ready_list[i].split(".")
                    read_data = result_list[0]
                    print("read_data", read_data)
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out\\" + str(read_data) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("room", str(read_data), imgs_)

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out\\" + str(des) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("good")
                            if str(des) == "amber_room":

                                for x in range(10):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\already_amber_need_move.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(150, 300, 800, 800, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("already_amber_need_move")
                                        click_pos_2(click_pos_2(800, 700, cla))
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\amber_over_notice.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(150, 300, 800, 800, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("amber_over_notice")
                                            break

                                    time.sleep(1)

                                juljun_on(cla)
                                result_chajib = chajib_check(cla)
                                if result_chajib == False:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\juljun\\amber_room.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        chajib_on(cla)
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out\\amber_room.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            chajib_on(cla)


                            else:
                                result_attack = attack_check(cla)
                                if result_attack == True:
                                    print("굿굿")
                                    potion_check(cla)
                                else:
                                    attack_on(cla)
                        else:
                            print("방 옮기자")
                            my_room_check(cla, des)


    except Exception as e:
        print(e)
        return 0



def my_room_check(cla, room):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos
    from action import menu_open, juljun_off, juljun_on, juljun_check, confirm_all, attack_check, out_check
    from get_item import get_item_start
    from potion import potion_buy
    from chango import go_chango, chango_start
    from request import request_get, request_start
    from clean_screen import clean_screen_go

    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("my_room_check", room)


        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_count", is_spot_count)
            if is_spot_count > 30:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out\\" + str(room) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("out_room : amber_room", imgs_)
                is_spot = True
            else:

                result_out = out_check(cla)
                if result_out == True:

                    is_room = False

                    for i in range(len(out_ready_list)):
                        result_list = out_ready_list[i].split(".")
                        read_data = result_list[0]
                        print("read_data", read_data)
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\out\\" + str(
                            read_data) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 30, 130, 70, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("room", str(read_data), imgs_)
                            is_room = True
                    if is_room == True:
                        click_pos_2(910, 100, cla)
                        time.sleep(0.5)
                        click_pos_2(875, 100, cla)
                else:
                    clean_screen_go(cla)



            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0
#############################################################################################################
#############################################################################################################
#############################################################################################################


#############################################################################################################
############################ 공통 #################################################################
#############################################################################################################
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

        # 발할라_일반_발키리_4 // 특수
        # 발할라_일반_혼돈_5 // 특수
        # 발할라_일반_폴크방_5 // 특수

        read_data = data.split("_")
        # read_data[1] => 일반, 특수
        # read_data[2] => 발키리, 혼돈, 폴크방
        # read_data[3] => 층수
        #
        # y_reg_1 = 140
        # if read_data[2] == "1":
        #     print("의뢰_이둔골짜기")
        # elif result_request_step[1] == "2":
        #     print("레이븐스홀")
        #     y_reg_1 = 175
        # elif result_request_step[1] == "3":
        #     print("아스가르드성")
        #     y_reg_1 = 215
        # elif result_request_step[1] == "4":
        #     print("헤르모드의갈림길")
        #     y_reg_1 = 250

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


                # 스텝 클릭
                step_check(cla, read_data[3])


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
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\menu_balhala.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 490, 420, 580, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                    QTest.qWait(1000)

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

        # 발할라_일반_발키리_4 // 특수
        # 발할라_일반_혼돈_5 // 특수
        # 발할라_일반_폴크방_5 // 특수


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



