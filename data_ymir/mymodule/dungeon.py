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

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("dungeon_start", data)

        # 발키리_일반_4_앰버
        # 혼돈_일반_5
        # 폴크방_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크방
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 보스, 협력, 앰버, 경험, 황금, (시작)

        if read_data[0] == "발키리":
            dungeon_balkeyly(cla, data)
        elif read_data[0] == "혼돈":
            dungeon_balkeyly(cla, data)
        elif read_data[0] == "폴크방":
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
    from clean_screen import clean_screen_go, clean_screen_start

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("dungeon_balkeyly", data)


        # 발키리_일반_4_앰버
        # 혼돈_일반_5
        # 폴크방_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크방
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 보스, 협력, 앰버, 경험, 황금, (시작)


        if read_data[3] == "보스":
            des = "boss_room"
        elif read_data[3] == "협력":
            des = 'cooperate_room'
        elif read_data[3] == "앰버":
            if v_.amber == True:
                des = "amber_room"
            else:
                des = "exp_room"
        elif read_data[3] == "경험":
            des = "exp_room"
        elif read_data[3] == "황금":
            des = "gold_room"

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            is_in = False
            for i in range(len(juljun_ready_list)):
                result_list = juljun_ready_list[i].split(".")
                read_data = result_list[0]
                print("read_data", read_data)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    is_in = True

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun\\" + str(des) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("good juljun")



                        if str(des) == "amber_room" and v_.amber == True:

                            result_chajib = chajib_check(cla)
                            if result_chajib == False:
                                juljun_off(cla)

                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun\\amber_room.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    chajib_on(cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\amber_room.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        chajib_on(cla)
                            else:
                                juljun_off(cla)

                        else:
                            result_attack = attack_check(cla)
                            if result_attack == True:
                                print("굿굿")
                                potion_check(cla)
                            else:
                                attack_on(cla)
                                juljun_on(cla)
                    else:
                        print("방 옮기자")
                        my_room_check(cla, des)
            if is_in == False:
                dungeon_in(cla, data)
        else:
            result_out = out_check(cla)
            if result_out == False:
                clean_screen_start(cla)

            is_in = False

            for i in range(len(out_ready_list)):
                result_list = out_ready_list[i].split(".")
                read_data = result_list[0]
                print("read_data", read_data)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    is_in = True

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\" + str(des) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("good")
                        if str(des) == "amber_room"and v_.amber == True:

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
                                        # 앰버 초과
                                        v_.amber = False
                                        break
                                time.sleep(1)

                            if v_.amber == True:
                                juljun_on(cla)
                                result_chajib = chajib_check(cla)
                                if result_chajib == False:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun\\amber_room.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        chajib_on(cla)
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\amber_room.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            chajib_on(cla)
                                else:
                                    juljun_off(cla)
                                    for x in range(300):
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
                                                # 앰버 초과
                                                v_.amber = False
                                                break
                                        time.sleep(1)
                        else:
                            juljun_on(cla)
                            result_attack = attack_check(cla)
                            if result_attack == True:
                                print("굿굿")
                                potion_check(cla)
                            else:
                                attack_on(cla)
                                juljun_on(cla)
                    else:
                        print("방 옮기자")
                        my_room_check(cla, des)
            if is_in == False:
                dungeon_in(cla, data)

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

    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("my_room_check", room)


        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("my_room_check_count", is_spot_count)
            if is_spot_count > 30:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\" + str(room) + ".PNG"
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
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\" + str(
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
    from action import menu_open, out_check, go_maul, confirm_all
    from schedule import myQuest_play_add


    try:
        print("dungeon_in", data)

        # 발키리_일반_4_앰버
        # 혼돈_일반_5
        # 폴크방_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크방
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 보스, 협력, 앰버, 경험, 황금, (시작)

        if read_data[1] == "일반":
            x_reg_1 = 50
            clicked = "common"
        elif read_data[1] == "특수":
            x_reg_1 = 150
            clicked = "dispute"
        # read_data[0] => 발키리, 혼돈, 폴크방
        if read_data[0] == "발키리":
            y_reg_1 = 160
        elif read_data[0] == "혼돈":
            y_reg_1 = 230
        elif read_data[0] == "폴크방":
            y_reg_1 = 300
        # read_data[2] => 층수
        #

        complete = False

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("dungeon_in_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\balhala.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : balhala", imgs_)

                # 일반, 특수



                click_pos_2(x_reg_1, 85, cla)
                time.sleep(0.5)
                click_pos_2(x_reg_1, 85, cla)
                time.sleep(0.5)

                # 발키리, 혼돈, 폴크방
                click_pos_2(120, y_reg_1, cla)
                time.sleep(0.5)
                click_pos_2(120, y_reg_1, cla)
                time.sleep(0.5)

                # 시간 만료인지 체크하기
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\dun_complete.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(805, 255, 870, 320, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dun_complete", imgs_)
                    complete = True
                if complete == False:
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
                        else:
                            result_confirm = confirm_all(cla)
                            if result_confirm == True:
                                break
                        time.sleep(0.1)
                    if fix == True:
                        myQuest_play_add(cla, data)
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
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\balhala.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("title : balhala", imgs_)
                                    click_pos_2(820, 1010, cla)
                                else:
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == True:
                                        break
                            time.sleep(0.5)

                        if out_after_notice == True:
                            go_maul(cla)
                        else:
                            is_spot = True
                            for i in range(10):
                                result_out = out_check(cla)
                                if result_out == True:
                                    print("던전입장완료")
                                    break
                                else:
                                    print("던전입장중")
                                time.sleep(1)


                if complete == True:
                    myQuest_play_add(cla, data)


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



