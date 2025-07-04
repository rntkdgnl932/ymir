import time
# import os
import sys


import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla, data):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import juljun_check, juljun_on, juljun_off, attack_check, attack_on, fix_bag, juljun_time_check
    from potion import potion_check
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
        print("jadong_start", data)

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
            # spot[4] => 최종 몬스터 위치

            # 우선 사냥터 이름 확인하기
            result_map = "none"
            for i in range(len(read_map)):
                read_ready_map = read_map[i].split("_")
                print("jadong_start", i, read_ready_map[0])
                if spot[3] == read_ready_map[0]:
                    print(read_map[i])
                    result_map = str(read_map[i])
                    map_name = result_map.split("_")
                    break

            # 절전모드인지 확인하고
            result_juljun = juljun_check(cla)
            if result_juljun == True:

                fix_bag(cla)

                if result_map == "none":
                    print("error...")
                else:
                    # 절전모드라면 해당맵 사냥중인지 확인하고 맞다면 물약검사, 아니라면 사냥터 옮기기
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\juljun_map\\" + str(map_name[1]) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 40, 200, 90, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("현재 [", str(map_name[0]), "] 에서 사냥중")
                        result_attack = attack_check(cla)
                        if result_attack == False:
                            juljun_off(cla)
                            attack_on(cla)
                            juljun_on(cla)
                        # 물약체크
                        potion_check(cla)
                        # 절전모드 중 정리하기
                        juljun_time_check(cla)
                    else:
                        print("여기 사냥터가 아니군")
                        jadong_spot_in(cla, data)
            else:
                # 절전모드 아니라면 절전모드 후 사냥터 맞는지 구분하기
                juljun_on(cla)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\juljun_map\\" + str(map_name[1]) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 40, 200, 90, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("현재 [", str(map_name[0]), "] 에서 사냥중")
                    # 물약체크
                else:
                    print("사냥터가 아니군")
                    jadong_spot_in(cla, data)


    except Exception as e:
        print(e)
        return 0


def jadong_spot_in(cla, data):
    import numpy as np
    import cv2
    import os
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, attack_on, confirm_all
    from clean_screen import clean_screen_start
    from potion import potion_buy
    from game_check import check_start, error_check

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
        print("jadong_spot_in", data)

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
                                    if landmark == 2:
                                        landmark = 0
                                    elif landmark == 3:
                                        landmark = 1
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
                                for i in range(5):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\im_move_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 980, 870, 1035, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        confirm_all(cla)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        error_check(cla)
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

                                for i in range(10):
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\im_move_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 980, 870, 1035, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        confirm_all(cla)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        error_check(cla)
                                        time.sleep(1)
                                    else:
                                        result_out = out_check(cla)
                                        if result_out == True:
                                            if spot[0] == "lv47파괴의땅의요툰파멸자":

                                                ran_spot = random.randint(1, 4)

                                                if ran_spot == 4:
                                                    attack_on(cla)
                                                else:
                                                    if ran_spot == 1:
                                                        x_reg = 480
                                                        y_reg = 540
                                                    elif ran_spot == 2:
                                                        x_reg = 600
                                                        y_reg = 450
                                                    elif ran_spot == 3:
                                                        x_reg = 590
                                                        y_reg = 590

                                                    random_spot_in(cla, x_reg, y_reg)
                                            else:
                                                attack_on(cla)
                                            is_spot = True
                                            break
                                    QTest.qWait(1000)


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

def random_spot_in(cla, x_reg, y_reg):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, attack_on, confirm_all
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
                                attack_on(cla)
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


def wonjung_check(cla):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, attack_on, confirm_all
    from clean_screen import clean_screen_start
    from game_check import move_check


    try:
        print("wonjung_check")

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\complete_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 710, 480, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("complete_btn", imgs_)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\complete_confirm_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 710, 670, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("complete_confirm_btn", imgs_)

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
                        click_pos_2(50, 85, cla)
                    if data == "raid":
                        click_pos_2(150, 85, cla)

                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\wonjung_information_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 300, 550, 400, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("wonjung_create_title", imgs_)

                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\wonjung\\unlock_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 175, 930, 1030, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("unlock_btn", imgs_)


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
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\post.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_icon\\wonjung.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 200, 960, 800, cla, img, 0.7)
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