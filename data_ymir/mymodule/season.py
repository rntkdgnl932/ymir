import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def season_start(cla, data):

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("season_start", data)

        # 시즌_4

        read_data = data.split("_")

        # read_data[1] => 4

        dungeon_season(cla, data)





    except Exception as e:
        print(e)
        return 0


##############################################################################################################################################
##################################################### 혼  돈 ##################################################################################
##############################################################################################################################################
def dungeon_season(cla, data):
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

    juljun_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\juljun"
    juljun_ready_list = os.listdir(juljun_ready)
    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("dungeon_season", data)


        # 시즌_4

        read_data = data.split("_")

        # read_data[1] => 4



        result_juljun = juljun_check(cla)
        if result_juljun == True:

            fix_bag(cla)

            is_in = False
            for i in range(len(juljun_ready_list)):
                result_list = juljun_ready_list[i].split(".")
                read_data = result_list[0]
                print("read_data", read_data)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\juljun\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    is_in = True

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\juljun\\grow_room.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 40, 150, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("grow_room", imgs_)





                        result_attack = attack_check(cla)
                        if result_attack == True:
                            print("굿굿")
                            potion_check(cla)
                        else:
                            attack_on(cla)
                            juljun_on(cla)
                    else:
                        print("방 옮기자")
                        my_room_check(cla)
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

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("room", str(read_data), imgs_)

                    is_in = True

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out\\grow_room.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("grow_room", imgs_)





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
                        my_room_check(cla)
            if is_in == False:
                dungeon_in(cla, data)

    except Exception as e:
        print(e)
        return 0



def my_room_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from action import out_check
    from clean_screen import clean_screen_go

    out_ready = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out"
    out_ready_list = os.listdir(out_ready)

    try:
        print("my_room_check")


        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("my_room_check_count", is_spot_count)
            if is_spot_count > 30:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out\\grow_room.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 130, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("out_room : grow_room", imgs_)
                is_spot = True
            else:

                result_out = out_check(cla)
                if result_out == True:

                    is_room = False

                    for i in range(len(out_ready_list)):
                        result_list = out_ready_list[i].split(".")
                        read_data = result_list[0]
                        print("read_data", read_data)
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\season\\out\\" + str(read_data) + ".PNG"
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

        # 시즌_4

        read_data = data.split("_")

        # read_data[1] => 4

        x_reg_1 = 250
        y_reg_1 = 160
        is_pic = "season"



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
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\is_pic\\" + str(is_pic) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 310, 945, 655, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("is_pic :", is_pic, imgs_)
                        is_in = True
                        break
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

                        step_check(cla, read_data[1])

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

                                        step_check(cla, read_data[1])

                                        click_pos_2(820, 1010, cla)
                                    else:
                                        result_out = out_check(cla)
                                        if result_out == True:
                                            is_spot = True
                                            print("던전입장완료")

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



