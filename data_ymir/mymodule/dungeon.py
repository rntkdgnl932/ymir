import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def dungeon_start(cla, data):

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("dungeon_start", data)

        # 발키리_일반_4_앰버
        # 혼돈_일반_5
        # 폴크_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 보스, 협력, 앰버, 경험, 황금, (시작)
        # read_data[3] => 포인트(1~4) // 발키리 제외하고....

        if read_data[0] == "발키리":
            dungeon_balkeyly(cla, data)
        elif read_data[0] == "혼돈" or read_data[0] == "폴크":
            dungeon_hondon_folk(cla, data)





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
    from action import attack_check, chaejib_check, attack_on, chaejib_on, fix_bag
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
        # 폴크_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크
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

            fix_bag(cla)

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

                            result_chaejib = chaejib_check(cla)
                            if result_chaejib == False:
                                juljun_off(cla)

                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun\\amber_room.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    chaejib_on(cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\amber_room.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        chaejib_on(cla)
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
                                result_chaejib = chaejib_check(cla)
                                if result_chaejib == False:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\juljun\\amber_room.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        chaejib_on(cla)
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\balkeyly\\out\\amber_room.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            chaejib_on(cla)
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
    from function_game import imgs_set_, click_pos_2
    from action import out_check
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
                        imgs_ = imgs_set_(20, 30, 130, 70, cla, img, 0.92)
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

##############################################################################################################################################
##################################################### 혼  돈 ##################################################################################
##############################################################################################################################################
def dungeon_hondon_folk(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_
    from action import out_check, juljun_check, juljun_on
    from action import attack_check, attack_on, fix_bag
    from clean_screen import clean_screen_go, clean_screen_start
    from potion import potion_check



    try:
        print("dungeon_hondon_folk", data)


        # 발키리_일반_4_앰버
        # 혼돈_일반_5
        # 폴크_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 포인트(1~4) // 발키리 제외하고....

        if read_data[0] == "혼돈":
            juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\hondon\\juljun"
            juljun_ready_list = os.listdir(juljun_ready)
            out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\hondon\\out"
            out_ready_list = os.listdir(out_ready)
        elif read_data[0] == "폴크":
            juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\folk\\juljun"
            juljun_ready_list = os.listdir(juljun_ready)
            out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\folk\\out"
            out_ready_list = os.listdir(out_ready)

        result_juljun = juljun_check(cla)
        if result_juljun == True:

            fix_bag(cla)

            is_in = False
            for i in range(len(juljun_ready_list)):
                result_list = juljun_ready_list[i].split(".")
                read_data = result_list[0]
                print("read_data", read_data)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\" + str(read_data) + "\\juljun\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    is_in = True

                    result_attack = attack_check(cla)
                    if result_attack == True:
                        print("굿굿")
                        potion_check(cla)
                    else:
                        attack_on(cla)
                        juljun_on(cla)


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
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\" + str(read_data) + "\\out\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    is_in = True

                    # 랜덤이동하기
                    random_spot_dun(cla, data)
                    # attack_on(cla)
                    # juljun_on(cla)


            if is_in == False:
                dungeon_in(cla, data)

    except Exception as e:
        print(e)
        return 0

def random_spot_dun(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, attack_on, juljun_on, go_maul, confirm_all, attack_check
    from clean_screen import clean_screen_start
    from game_check import move_check

    try:
        print("random_spot_dun", data)

        # 발키리_일반_4_앰버
        # 혼돈_일반_5_4
        # 폴크_일반_5_4

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 포인트(1~4)

        if read_data[0] == "혼돈":
            des = "hondon"
        elif read_data[0] == "폴크":
            des = 'folk'

        ran_x = 650
        ran_y = 725

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("random_spot_count", is_spot_count)
            if is_spot_count > 30:
                is_spot = True

            # ran_ready = random.randint(1, 3)
            if read_data[0] == "혼돈":

                ran_x = random.randint(330, 640)

                if read_data[3] == "1":
                    ran_y = random.randint(355, 400)
                elif read_data[3] == "2":
                    ran_y = random.randint(445, 570)
                elif read_data[3] == "3":
                    ran_y = random.randint(610, 645)
                elif read_data[3] == "4":
                    ran_y = random.randint(680, 735)

            elif read_data[0] == "폴크":
                ran_ready = random.randint(1, 3)
                if read_data[3] == "1":
                    if ran_ready == 1 or ran_ready == 2:
                        ran_y = 315
                    elif ran_ready == 3:
                        ran_y = 350
                elif read_data[3] == "2":
                    if ran_ready == 1 or ran_ready == 2:
                        ran_y = 385
                    elif ran_ready == 3:
                        ran_y = 420
                elif read_data[3] == "3":
                    if ran_ready == 1:
                        ran_y = 455
                    elif ran_ready == 2:
                        ran_y = 490
                    elif ran_ready == 3:
                        ran_y = 525
                elif read_data[3] == "4":
                    if ran_ready == 1:
                        ran_y = 560
                    elif ran_ready == 2:
                        ran_y = 595
                    elif ran_ready == 3:
                        ran_y = 630


            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\map_" + str(des) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(190, 30, 400, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("map_", str(des), imgs_)

                if read_data[0] == "혼돈":

                    is_foot = False

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\foot_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(230, 250, 730, 800, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("foot_point", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        is_foot = True
                        for i in range(10):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\not_move_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 500, 610, 580, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("not_move_notice", imgs_)
                                is_foot = False
                                break
                            QTest.qWait(100)


                    else:
                        click_pos_2(ran_x, ran_y, cla)
                        QTest.qWait(100)

                    if is_foot == True:

                        for i in range(10):
                            result_out = out_check(cla)
                            if result_out == True:
                                result_move = move_check(cla)
                                if result_move == True:
                                    break
                            QTest.qWait(500)

                        result_out = out_check(cla)
                        if result_out == True:
                            attack_on(cla)
                            juljun_on(cla)
                            result_attack = attack_check(cla)
                            if result_attack == True:
                                is_spot = True

                elif read_data[0] == "폴크":
                    is_monster = False
                    for i in range(10):
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\folk_monster_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(720, 290, 770, 660, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("folk_monster_btn", imgs_)
                            is_monster = True
                            click_pos_2(800, ran_y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\folk_monster_click_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 210, 800, 660, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("folk_monster_click_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        QTest.qWait(1000)
                    if is_monster == True:
                        click_pos_2(800, ran_y, cla)
                        time.sleep(1)
                        click_pos_2(910, 1005, cla)

                        is_move = True
                        for i in range(10):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\not_move_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 500, 610, 580, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("not_move_notice", imgs_)
                                is_move = False
                                break
                            time.sleep(0.1)
                        if is_move == False:
                            go_maul(cla)
                        else:
                            for i in range(10):
                                result_out = out_check(cla)
                                if result_out == True:
                                    result_move = move_check(cla)
                                    if result_move == True:
                                        break
                                QTest.qWait(500)

                            result_out = out_check(cla)
                            if result_out == True:
                                attack_on(cla)
                                juljun_on(cla)
                                result_attack = attack_check(cla)
                                if result_attack == True:
                                    is_spot = True

            else:
                result_out = out_check(cla)
                if result_out == True:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\" + str(des) + "\\out\\" + str(des) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 160, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print(str(des), imgs_)
                        click_pos_2(85, 50, cla)
                    else:
                        # 들어가기 ㄱ
                        dungeon_in(cla, data)
                        print("migoong_in(cla, data)")

                else:
                    clean_screen_start(cla)

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
        # 폴크_일반_5

        read_data = data.split("_")

        # read_data[0] => 발키리, 혼돈, 폴크
        # read_data[1] => 일반, 특수
        # read_data[2] => 층수
        # read_data[3] => 보스, 협력, 앰버, 경험, 황금, (시작)
        # read_data[3] => 포인트(1~4) // 발키리 제외하고....

        if read_data[1] == "일반":
            x_reg_1 = 50
            clicked = "common"
        elif read_data[1] == "특수":
            x_reg_1 = 150
            clicked = "dispute"
        # read_data[0] => 발키리, 혼돈, 폴크
        if read_data[0] == "발키리":
            y_reg_1 = 160
            is_pic = "balkeyly"
        elif read_data[0] == "혼돈":
            y_reg_1 = 230
            is_pic = "hondon"
        elif read_data[0] == "폴크":
            y_reg_1 = 300
            is_pic = "folk"
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


                is_in = False

                # 일반, 특수

                for i in range(7):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\" + str(clicked) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 210, 885, 280, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked :", clicked, imgs_)
                        # 발키리, 혼돈, 폴크
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\is_pic\\" + str(is_pic) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(690, 310, 945, 655, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("is_pic :", is_pic, imgs_)
                            is_in = True
                            break
                        else:
                            click_pos_2(120, y_reg_1, cla)
                            time.sleep(0.5)
                            click_pos_2(120, y_reg_1, cla)
                            time.sleep(0.5)
                    else:
                        click_pos_2(x_reg_1, 85, cla)
                        time.sleep(0.5)
                        click_pos_2(x_reg_1, 85, cla)
                        time.sleep(0.5)
                    QTest.qWait(1000)

                if is_in == True:


                    # 시간 만료인지 체크하기
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\dun_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 240, 880, 320, cla, img, 0.85)
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
                            for i in range(30):
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
                                        result_out = out_check(cla)
                                        if result_out == True:
                                            is_spot = True
                                            print("던전입장완료")

                                            if read_data[0] == "폴크":
                                                print("날아다니자....")
                                                for f in range(3):
                                                    # confirm_all
                                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\mission_end_btn.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(470, 550, 650, 650, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("mission_end_btn", imgs_)
                                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                                        time.sleep(1)
                                                        click_pos_2(480, 520, cla)
                                                    else:
                                                        click_pos_2(480, 520, cla)
                                                    time.sleep(3)
                                                for f in range(15):
                                                    click_pos_2(855, 890, cla)
                                                    time.sleep(0.05)
                                                time.sleep(5)
                                                for f in range(15):
                                                    click_pos_2(855, 890, cla)
                                                    time.sleep(0.05)
                                                time.sleep(3)
                                                for f in range(15):
                                                    click_pos_2(855, 890, cla)
                                                    time.sleep(0.05)
                                                time.sleep(3)
                                                for f in range(15):
                                                    click_pos_2(855, 890, cla)
                                                    time.sleep(0.05)

                                            break
                                        else:
                                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\skip_2.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(760, 30, 960, 120, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("skip_2", imgs_)
                                            else:
                                                confirm_all(cla)

                                time.sleep(0.5)

                            if out_after_notice == True:
                                go_maul(cla)



                    if complete == True:
                        myQuest_play_add(cla, data)
                else:
                    print("hmm....................")

            else:

                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\balhala.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 550, 850, 640, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\menu_balhala.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 490, 520, 580, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)

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
        # 발할라_일반_폴크_5 // 특수


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



