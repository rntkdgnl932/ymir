import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def chaejib_start(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import juljun_check, juljun_on, juljun_off, attack_check, attack_on, fix_bag, juljun_time_check, chaejib_check, chaejib_on
    from potion import potion_check
    from schedule import myQuest_play_add
    # 사냥터
    dir_path = "C:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder)
    file_data = dir_path + "\\jadong\\asgard.txt"
    file_title = dir_path + "\\jadong\\reg_title_point.txt"
    file_des = dir_path + "\\jadong\\reg_des_point.txt"
    file_map = dir_path + "\\jadong\\map_name.txt"
    file_spot_in = dir_path + "\\jadong\\map_spot_in.txt"

    if os.path.isfile(file_data) == True:
        with open(file_data, "r", encoding='utf-8-sig') as file:
            read_asgard = file.read().splitlines()
        with open(file_title, "r", encoding='utf-8-sig') as file:
            read_title = file.read().splitlines()
        with open(file_des, "r", encoding='utf-8-sig') as file:
            read_des = file.read().splitlines()
        with open(file_map, "r", encoding='utf-8-sig') as file:
            read_map = file.read().splitlines()
        with open(file_spot_in, "r", encoding='utf-8-sig') as file:
            read_spot_in = file.read().splitlines()


    try:
        print("chaejib_start")

        # 절전모드인지 확인하고
        result_juljun = juljun_check(cla)
        if result_juljun == True:

            fix_bag(cla)

            result_chaejib = chaejib_check(cla)

            if result_chaejib == False:
                chaejib_go(cla)
            else:
                print("채집중...")

                chaejib = True
                chaejib_count = 0
                chaejib_time = 0
                while chaejib is True:
                    chaejib_time += 1
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\attack_check\\chajib_ing.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 900, 600, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        if chaejib_time > 3600:
                            chaejib = False
                            myQuest_play_add(cla, "채집하기")
                        if chaejib_time % 60 == 0:
                            now_minute = chaejib_time // 60
                            print("채집시간 60분 중", str(now_minute), "분 지났다.")
                    else:
                        chaejib_count += 1
                        if chaejib_count > 4:
                            chaejib = False
                    QTest.qWait(1000)



        else:
            juljun_on(cla)

    except Exception as e:
        print(e)
        return 0

def chaejib_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure, go_maul, dun_out
    from boonhae_collection import boonhae_collection_start
    try:
        print("chaejib_go")


        ran_spot = random.randint(1, 3)
        if ran_spot == 1:
            # 트롤하층
            print("트롤유적하층")
            data = "lv25학살자헬데이아"
            x_reg = 410
            y_reg = 630
        elif ran_spot == 2:
            # 트롤상층
            print("트롤유적상층")
            data = "lv26스에만"
            x_reg = 465
            y_reg = 625
        elif ran_spot == 3:
            # 애쉬르산
            print("애쉬르산")
            data = "정찰대의절벽"
            x_reg = 590
            y_reg = 630

        chaejib_spot_in(cla, data, x_reg, y_reg)

    except Exception as e:
        print(e)
        return 0



def chaejib_spot_in(cla, data, data_x, data_y):
    import numpy as np
    import cv2
    import os
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, attack_on, confirm_all
    from clean_screen import clean_screen_start
    from potion import potion_buy
    from game_check import check_start, error_check
    from schedule import myQuest_play_add

    # 사냥터
    dir_path = "C:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder)
    file_data = dir_path + "\\jadong\\asgard.txt"
    file_title = dir_path + "\\jadong\\reg_title_point.txt"
    file_des = dir_path + "\\jadong\\reg_des_point.txt"
    file_map = dir_path + "\\jadong\\map_name.txt"
    file_spot_in = dir_path + "\\jadong\\map_spot_in.txt"

    if os.path.isfile(file_data) == True:
        with open(file_data, "r", encoding='utf-8-sig') as file:
            read_asgard = file.read().splitlines()
        with open(file_title, "r", encoding='utf-8-sig') as file:
            read_title = file.read().splitlines()
        with open(file_des, "r", encoding='utf-8-sig') as file:
            read_des = file.read().splitlines()
        with open(file_map, "r", encoding='utf-8-sig') as file:
            read_map = file.read().splitlines()
        with open(file_spot_in, "r", encoding='utf-8-sig') as file:
            read_spot_in = file.read().splitlines()


    try:
        print("chaejib_spot_in", data)

        ###### 게임체크하기
        check_start(cla)

        ################ 물약부터 사보자(이때 던전은 자동으로 나가짐)
        potion_buy(cla)

        # 들어온 데이터와 비교하기....
        result_spot = "none"
        for i in range(len(read_asgard)):
            read_ready = read_asgard[i].split("_")
            print("jadong_start", i, read_ready[0])
            if read_ready[0] == data:
                print(read_asgard[i])
                result_spot = str(read_asgard[i])
                break
        # lv7히티도적단부두목_아스가르드_이둔의골짜기_이둔의골짜기_구분없음_800,400
        if result_spot == "none":
            print("error")
        else:
            spot = result_spot.split("_")
            # spot[1] => file_title 여기와 비교 후 값 가져오기(전체 지도)
            # spot[2] => file_title 여기와 비교 후 값 가져오기(큰 지도)
            # spot[3] => file_des 여기와 비교 후 값 가져오기(내부타이틀 위치) // 해당맵에 들어왔는지 확인 // 절전모드 확인
            # spot[4] => 구분없음/일반//정예 => 몹 종류에 따른 것
            # spot[5] => 최종 몬스터 위치

            # 맵이름부터 찾아오기
            map_spot_in = "none"
            for i in range(len(read_spot_in)):
                read_ready_spot_in = read_spot_in[i].split("_")
                print("read_ready_spot_in", i, read_ready_spot_in[0])
                if spot[2] == read_ready_spot_in[0]:
                    print(read_spot_in[i])
                    result_spot_in = str(read_spot_in[i])
                    map_spot_in = result_spot_in.split("_")
                    break

            if map_spot_in == "none":
                print("코딩 문제 있는듯")
            else:
                is_spot = False
                is_spot_count = 0
                while is_spot is False:
                    is_spot_count += 1
                    print("is_spot_countis_spot_countis_spot_countis_spot_countis_spot_countis_spot_count", is_spot_count)
                    if is_spot_count > 15:
                        is_spot = True
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\des_map_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 970, 960, 1040, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("des_map_in")
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\spot_in_map\\" + str(
                            map_spot_in[1]) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 30, 550, 80, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("okokokokokokokokokokok")

                            # 구분없음 // 일반// 정예
                            print("구분?", spot[4])
                            if spot[4] == "일반":
                                for i in range(5):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\common.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 140, 880, 180, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\elite.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(780, 140, 880, 180, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    QTest.qWait(1000)
                            elif spot[4] == "정예":
                                for i in range(5):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\elite.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 140, 880, 180, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\common.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(780, 140, 880, 180, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    QTest.qWait(1000)
                            else:
                                print("구분없음", spot[4])


                            # 작은 맵에 제목 클릭위치 가져오기
                            # 들어온 데이터와 비교하기....
                            result_des = "none"
                            for i in range(len(read_des)):
                                read_ready_des = read_des[i].split("_")
                                print("read_ready_des", i, read_ready_des[0])
                                if spot[3] == read_ready_des[0]:
                                    print(read_des[i])
                                    result_des = str(read_des[i])
                                    break
                            if result_des == "none":
                                print("코딩코딩.....")
                            else:
                                result_des_ready = result_des.split("_")
                                result_des_reg = result_des_ready[1].split(",")
                                x_reg = int(result_des_reg[0])
                                y_reg = int(result_des_reg[1])
                                click_pos_2(x_reg, y_reg, cla)
                                time.sleep(0.2)
                                click_pos_2(x_reg, y_reg, cla)
                                time.sleep(0.2)



                            # 몬스터 클릭해주기

                            is_mon = False

                            if spot[4] == "랜드마크":
                                for i in range(4):
                                    landmark = i
                                    if landmark > 2:
                                        landmark = i % 2
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\landmark_btn_" + str(landmark) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 180, 800, 900, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("is_mon", i, imgs_)
                                        is_mon = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\is_landmark_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(700, 180, 800, 900, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        QTest.qWait(1000)
                            else:


                                for i in range(4):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\mon_btn_" + str(i) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 180, 800, 900, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("is_mon", i, imgs_)
                                        is_mon = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\is_mon_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(700, 180, 800, 900, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        QTest.qWait(1000)
                            print("1")
                            if is_mon == False:
                                if spot[4] == "랜드마크":
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\is_landmark_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 180, 800, 900, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\is_mon_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 180, 800, 900, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                print("2")
                            else:
                                # 마지막으로 추출한 값을 클릭
                                print("3")
                                result_err = False
                                for i in range(5):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\im_move_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 980, 870, 1035, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        confirm_all(cla)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        result_err = error_check(cla)
                                        time.sleep(1)
                                        break
                                    else:
                                        result_reg = spot[5].split(",")
                                        result_x_reg = int(result_reg[0])
                                        result_y_reg = int(result_reg[1])
                                        click_pos_2(result_x_reg, result_y_reg, cla)
                                        time.sleep(0.2)
                                        click_pos_2(result_x_reg, result_y_reg, cla)
                                        time.sleep(0.2)
                                    QTest.qWait(500)
                                if result_err == False:
                                    for i in range(10):
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\im_move_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(780, 980, 870, 1035, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            confirm_all(cla)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            result_err = error_check(cla)
                                            if result_err == True:
                                                myQuest_play_add(cla, "채집하기")
                                                is_spot = True
                                                clean_screen_start(cla)
                                                break
                                            time.sleep(1)
                                        else:
                                            result_out = out_check(cla)
                                            if result_out == True:
                                                print("도착했으니...랜덤지침대로 옮겨서 채집쓰")
                                                random_spot_in_chaejib(cla, data_x, data_y)
                                                is_spot = True
                                                break
                                        QTest.qWait(1000)
                                else:
                                    myQuest_play_add(cla, "채집하기")
                                    is_spot = True
                                    clean_screen_start(cla)

                        else:
                            click_pos_2(70, 50, cla)
                    else:
                        result_out = out_check(cla)
                        if result_out == True:

                            # 마을은 클릭위치 다름....

                            click_pos_2(100, 50, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\asgard.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 500, 550, 550, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("asgard")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)

                                # 맵 내에 클릭위치 가져오기
                                # 들어온 데이터와 비교하기....
                                result_title = "none"
                                for i in range(len(read_title)):
                                    read_ready_title = read_title[i].split("_")
                                    print("read_ready_title", i, read_ready_title[0])
                                    if spot[2] == read_ready_title[0]:
                                        print(read_title[i])
                                        result_title = str(read_title[i])
                                        break
                                if result_title == "none":
                                    print("코딩코딩")
                                else:
                                    result_title_ready = result_title.split("_")
                                    result_title_reg = result_title_ready[1].split(",")
                                    x_reg = int(result_title_reg[0])
                                    y_reg = int(result_title_reg[1])
                                    click_pos_2(x_reg, y_reg, cla)


                            else:
                                clean_screen_start(cla)
                    QTest.qWait(1000)


    except Exception as e:
        print(e)
        return 0



def random_spot_in_chaejib(cla, x_reg, y_reg):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, chaejib_on, juljun_on
    from clean_screen import clean_screen_start
    from game_check import move_check


    try:
        print("random_spot_in", x_reg, y_reg)

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("random_spot_in_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\des_map_in.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 970, 960, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("des_map_in")

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\migoong\\foot_point.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(230, 250, 730, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("foot_point", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            result_move = move_check(cla)
                            if result_move == True:
                                chaejib_on(cla)
                                juljun_on(cla)
                                is_spot = True
                        time.sleep(0.5)



                else:
                    click_pos_2(x_reg, y_reg, cla)
                    QTest.qWait(100)

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(100, 50, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)


    except Exception as e:
        print(e)
        return 0

