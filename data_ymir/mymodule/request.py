import time
# import os
import sys


import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def request_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import juljun_check, juljun_off, juljun_on, attack_check, out_check
    from potion import potion_check
    from game_check import move_check
    from dead_die import dead_check
    try:
        print("request_start", data)

        # 의뢰_1 => 이둔골짜기
        # 의뢰_2 => 레이븐스홀
        # 의뢰_3 => 아스가르드성
        # 의뢰_4 => 헤르모드의갈림길

        result_request_step = data.split("_")

        # result_request_step[1] => step

        if result_request_step[1] == 1:
            print("의뢰_이둔골짜기")
        elif result_request_step[1] == 2:
            print("레이븐스홀")
        elif result_request_step[1] == 3:
            print("아스가르드성")
        elif result_request_step[1] == 4:
            print("헤르모드의갈림길")


        is__request = False
        is__request_count = 0

        while is__request is False:
            is__request_count += 1
            if is__request_count > 4:
                request_get_ready(cla, data)
                is__request = True

            result_juljun = juljun_check(cla)
            if result_juljun == True:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("click_request_btn", imgs_)
                    is__request_count = 0
                    result_attack = attack_check(cla)
                    if result_attack == True:
                        potion_check(cla)
                    else:
                        juljun_off(cla)
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(835, 135, 900, 190, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("click_request_btn", imgs_)
                            click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                            juljun_on(cla)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_complete_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("request_complete_btn", imgs_)
                        is__request_count = 0
                        juljun_off(cla)
                        time.sleep(2)
                        click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                        time.sleep(2)
                        request_get_ready(cla, data)

                    else:
                        request_get_ready(cla, data)
            else:
                result_out = out_check(cla)
                if result_out == True:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(835, 135, 900, 190, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("click_request_btn", imgs_)
                        is__request_count = 0
                        click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                        juljun_on(cla)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_complete_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("request_complete_btn", imgs_)
                            is__request_count = 0
                            juljun_off(cla)
                            click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                            request_get_ready(cla, data)
                        else:
                            request_get_ready(cla, data)
                else:
                    print("로딩중이거나 걷는 거?")
                    dead_check(cla)
                    move_check(cla)
                    QTest.qWait(1500)
            QTest.qWait(1000)

    except Exception as e:
        print(e)
        return 0



def request_get_ready(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start, clean_screen_go
    from action import out_check, confirm_all

    try:
        print("request_get_ready", data)

        # 의뢰_1 => 이둔골짜기
        # 의뢰_2 => 레이븐스홀
        # 의뢰_3 => 아스가르드성
        # 의뢰_4 => 헤르모드의갈림길

        result_request_step = data.split("_")

        # result_request_step[1] => step
        x_reg_2 = 55
        y_reg_2 = 85
        if result_request_step[1] == "1":
            print("의뢰_이둔골짜기")
            x_reg_1 = 405
            y_reg_1 = 815
        elif result_request_step[1] == "2":
            print("레이븐스홀")
            x_reg_1 = 465
            y_reg_1 = 505
        elif result_request_step[1] == "3":
            print("아스가르드성")
            x_reg_1 = 465
            y_reg_1 = 505
        elif result_request_step[1] == "4":
            print("헤르모드의갈림길")
            x_reg_1 = 640
            y_reg_1 = 455

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_ready_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\map_in\\" + str(result_request_step[1]) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(240, 30, 550, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("map_in", str(result_request_step[1]))

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_notice_board.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 200, 950, 700, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("request_notice_board", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(1000)
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\im_move_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 980, 870, 1035, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:

                        confirm_all(cla)

                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\request_notice_board.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 200, 950, 700, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                QTest.qWait(1000)
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\im_move_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 980, 870, 1035, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    confirm_all(cla)

                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                result_out = out_check(cla)
                                if result_out == True:
                                    request_get(cla, data)
                                    is_spot = True
                                    break
                            QTest.qWait(1000)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\elite.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 140, 880, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

                    click_pos_2(55, 85, cla)
            else:
                for i in range(10):
                    result_out = out_check(cla)
                    if result_out == True:
                        # 마을은 클릭위치 다름....

                        click_pos_2(100, 50, cla)

                    else:

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\map_in\\" + str(
                            result_request_step[1]) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(240, 30, 550, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("map_in", str(result_request_step[1]))
                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\jadong\\asgard.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 500, 550, 550, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("asgard", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\asgard_whole_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 240, 70, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("asgard_whole_title", imgs_)
                                    click_pos_2(x_reg_1, y_reg_1, cla)
                                else:
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\asgard_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(120, 30, 240, 70, cla, img, 0.7)
                                    if imgs_ is not None and imgs_ != False:
                                        print("asgard_title", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(2)
                                    else:
                                        # clean_screen_start(cla)
                                        clean_screen_go(cla)
                                        print("한번만")

                    QTest.qWait(1000)

            QTest.qWait(1000)



    except Exception as e:
        print(e)
        return 0


def request_get(cla, data):
    import numpy as np
    import cv2
    import os
    from function_game import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from game_check import move_check
    from schedule import myQuest_play_add
    from action import confirm_all, juljun_on, attack_check, juljun_check, juljun_off

    prohibition = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition"
    prohibition_list = os.listdir(prohibition)
    # for i in range(len(prohibition_list)):
    #     result_prohibition_list = prohibition_list[i].split(".")
    #     read_data = result_prohibition_list[0]
    #     print("read_data", read_data)

    try:
        print("request_get", data)

        complete = False

        # 의뢰_1 => 이둔골짜기
        # 의뢰_2 => 레이븐스홀
        # 의뢰_3 => 아스가르드성
        # 의뢰_4 => 헤르모드의갈림길

        result_request_step = data.split("_")
        y_reg_1 = 140
        # result_request_step[1] => step
        if result_request_step[1] == "1":
            print("의뢰_이둔골짜기")
        elif result_request_step[1] == "2":
            print("레이븐스홀")
            y_reg_1 = 175
        elif result_request_step[1] == "3":
            print("아스가르드성")
            y_reg_1 = 215
        elif result_request_step[1] == "4":
            print("헤르모드의갈림길")
            y_reg_1 = 250

        is_spot = False
        is_spot_count = 0
        while is_spot is False:
            is_spot_count += 1
            print("request_get_count", is_spot_count)
            if is_spot_count > 15:
                is_spot = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)

                click_pos_2(60, y_reg_1, cla)
                time.sleep(0.5)
                click_pos_2(60, y_reg_1, cla)
                time.sleep(0.5)

                # 여기서 분별 잘해서 받도록 하자
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\complete_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(770, 130, 910, 190, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("complete_1", imgs_)
                    is_spot = True
                    complete = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prerequisites.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(220, 130, 450, 190, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("prerequisites", imgs_)
                        is_spot = True
                        complete = True
                    else:
                        ##############//////////////////####################
                        # 아랫값 정하기
                        y_reg_3 = 1040

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\complete_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(770, 130, 910, y_reg_3, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("complete_1", imgs_)
                            y_reg_3 = imgs_.y

                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prerequisites.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 130, 450, y_reg_3, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("prerequisites", imgs_)
                            if y_reg_3 > imgs_.y:
                                y_reg_3 = imgs_.y

                        print("y_reg_3", y_reg_3)
                        if y_reg_3 < 190:
                            complete = True
                        else:
                            y_scan_1 = 50  # 120
                            y_scan_2 = 120 # 190

                            click_y = 85 # 155

                            for s in range(10):
                                y_scan_1 += 70
                                y_scan_2 += 70
                                click_y += 70
                                print("y_scan_1, y_scan_2, click_y", y_scan_1, y_scan_2, click_y)
                                if y_scan_2 > y_reg_3:
                                    complete = True

                                    break
                                else:
                                    is_prohibition_y = 200
                                    is_prohibition = False
                                    for i in range(len(prohibition_list)):
                                        result_prohibition_list = prohibition_list[i].split(".")
                                        read_data = result_prohibition_list[0]
                                        print("read_data", read_data)
                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition\\" + str(
                                            read_data) + ".PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(210, y_scan_1, 460, y_scan_2, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("prohibition_list", imgs_)
                                            is_prohibition = True
                                    # 금지 안되어 있으면 클릭하고
                                    if is_prohibition == False:
                                        click_pos_2(840, click_y, cla)
                                        break
                                    # 금지 되어 있으면 다음꺼 클릭하기 위함인데
                                    # y_reg_3 이건 완료 또는 불가능한 최소값
                                    # 그래서 이번에 금지된것이고, y_scan_1, y_scan_2 의 범주내에 최소값이 있으면 퀘스트 완료로 간주
                                    else:

                                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\complete_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(770, y_scan_1, 910, y_scan_2, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("complete? complete_1", imgs_)
                                            complete = True
                                        else:
                                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prerequisites.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(220, y_scan_1, 450, y_scan_2, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("complete? prerequisites", imgs_)
                                                complete = True
                        if complete == False:
                            # 이제 수락 받으러 가는 길
                            for i in range(50):
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("quest", imgs_)
                                    click_pos_2(815, click_y, cla)
                                else:
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == False:
                                        move_check(cla)
                                    else:
                                        break
                                time.sleep(1)


                            for i in range(10):
                                confirm_all(cla)

                                result_attacl_check = attack_check(cla)
                                if result_attacl_check == False:
                                    juljun_off(cla)
                                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(835, 135, 900, 190, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("click_request_btn", imgs_)
                                        click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                                        juljun_on(cla)
                                else:
                                    break
                                time.sleep(1)


                        is_spot = True



                    # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\move_btn.PNG"
                    # img_array = np.fromfile(full_path, np.uint8)
                    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    # imgs_ = imgs_set_(770, y_reg_2, 910, y_reg_3, cla, img, 0.85)
                    # if imgs_ is not None and imgs_ != False:
                    #     print("move_btn", imgs_)


            else:
                for i in range(5):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\safe_map_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 60, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\maul_in_request_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 50, 170, 200, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("maul_in_request_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)

                            for r in range(10):
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\quest.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 30, 200, 80, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("quest", imgs_)
                                    break
                                time.sleep(0.5)

                            break
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\jabhwa_sangin_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(10, 60, 160, 210, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(90, 75, 90, 180, cla)
                            else:
                                click_pos_2(190, 55, cla)
                                time.sleep(1)

                    QTest.qWait(1000)

            QTest.qWait(1000)

        if complete == True:
            print("add 하거라")
            myQuest_play_add(cla, data)

    except Exception as e:
        print(e)
        return 0



