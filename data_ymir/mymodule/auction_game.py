import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:

        result_dia = 0
        result_silver = 0

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)

            result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
            result_text = change_number(result_text)
            result_dia = int_put_(result_text)
            result_dia_num = in_number_check(result_dia)
            print("result_text", result_dia_num, result_dia)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("silver_reg", imgs_)
            result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
            result_text2 = change_number(result_text2)
            result_silver = int_put_(result_text2)
            result_silver_num = in_number_check(result_silver)
            print("result_text2", result_silver_num, result_silver)

        if result_dia_num == True:

            return result_silver, result_dia

    except Exception as e:
        print(e)


def auction_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:
        # 창고에 가서 물품 꺼내고

        # 거래소 들어가서

        # 정산 후

        # 아이템 판매 등록 활성화하고

        # 현재 최저가 판독
        result_auction_low_num = auction_low_num(cla)
        # 수량 판독
        result_auction_qun_num = auction_qun_num(cla)

        # 곱하고
        result = float(result_auction_low_num) * float(result_auction_qun_num)
        print("result", result)
        result = int(result)
        print("result", result)

        # 판매한다.

        # 마무리로 창고에 다시 넣는다다

    except Exeption as e:
        print(e)


def auction_in(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, in_number_check, int_put_, change_number
    from action import menu_open

    try:
        print("auction_in")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 7:
                is_action = True

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)
                is_action = True

            else:
                menu_open(cla)
                time.sleep(0.3)
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 430, 750, 520, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("menu_auction", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)


    except Exception as e:
        print(e)

def auction_low_num(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        # text_check_get(365, 520, 433, 533, cla)

        is_point = False
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(365, 520, 433, 533, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("point", imgs_)
            is_point = True
            point_x = imgs_.x

        num_find_front = False
        num_find_front_count = 0
        num_find_back = False
        num_find_back_count = 0

        x_reg_1 = 0
        this_price = ""
        if is_point == True:

            front_first_num = 0

            print("소수점 앞 자리, 가장 앞에 숫자 찾기")
            # 숫자 있는지 파악하기..
            print("숫자 있는지 파악하기..")
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, point_x - plus, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_front = True
                    break
            # 맨 앞 숫자 위치 파악하기
            print("맨 앞 숫자 위치 파악하기", x_reg_1)
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, point_x - plus, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x


            # 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
            print("맨앞부터 숫자 찾아 돌려서 숫자 파악하기..")
            while num_find_front is True:
                num_find_front_count += 1
                is_num = False

                if num_find_front_count == 1:
                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 5, 533, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("앞 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            if point_x > imgs_.x:
                                this_price += str(i)
                                x_reg_1 = imgs_.x + 4
                                is_num = True
                                break
                        if i == 1:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 5, 533, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("앞 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                                if point_x > imgs_.x:
                                    this_price += str(i)
                                    x_reg_1 = imgs_.x + 4
                                    is_num = True
                                    break
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("앞 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            if point_x > imgs_.x:
                                this_price += str(i)
                                x_reg_1 = imgs_.x + 4
                                is_num = True
                                break
                        if i == 1:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("앞 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                                if point_x > imgs_.x:
                                    this_price += str(i)
                                    x_reg_1 = imgs_.x + 4
                                    is_num = True
                                    break
                if is_num == False:
                    num_find_front = False
                QTest.qWait(100)

            #######
            this_price += str(".")
            back_first_num = 0
            ######
            print("소수점 뒷 자리, 가장 앞에 숫자 찾기")

            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(point_x - plus, 512, 433, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_back = True
                    break
            # 소수점 뒷자리 중 가장 앞 숫자 찾기
            print("소수점 뒷자리 중 가장 앞 숫자 찾기")
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(point_x - plus, 512, 433, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x

            # 소수점 뒷자리 중 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
            print("소수점 뒷자리 중 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..", x_reg_1)
            while num_find_back is True:
                num_find_back_count += 1
                is_num = False

                if num_find_back_count == 1:
                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(point_x - plus, 512, x_reg_1 - plus + 4, 533, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("뒤 : ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                        if i == 1:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(point_x - plus, 512, x_reg_1 - plus + 4, 533, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("뒤 : ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                                x_reg_1 = imgs_.x + 4
                                this_price += str(i)
                                is_num = True
                                break
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("뒤 : ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                        if i == 1:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("뒤 : ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                                x_reg_1 = imgs_.x + 4
                                this_price += str(i)
                                is_num = True
                                break
                if is_num == False:
                    num_find_back = False
                QTest.qWait(100)

        else:
            print("소수점 없을 경우 가장 앞에 숫자 및 가장 뒷 숫자 찾기")
            # 숫자 있는지 파악하기..
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, 433, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_front = True
                    break
            # 맨 앞 숫자 위치 파악하기
            print("맨 앞 숫자 위치 파악하기")
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, 433, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x

            # 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
            print("맨앞부터 숫자 찾아 돌려서 숫자 파악하기..")
            while num_find_front is True:
                num_find_front_count += 1
                is_num = False

                if num_find_front_count == 1:
                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 5, 533, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 8, 533, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                        if i == 1:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 8, 533, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                                x_reg_1 = imgs_.x + 4
                                this_price += str(i)
                                is_num = True
                                break
                if is_num == False:
                    num_find_front = False
                QTest.qWait(100)


        print("this_price", this_price)
        return this_price
    except Exception as e:
        print(e)


def auction_qun_num(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:
        print("auction_qun_num")
        # text_check_get(365, 520, 433, 533, cla)

        num_find_front = False
        num_find_front_count = 0

        x_reg_1 = 0
        this_price = ""
        # 숫자 있는지 파악하기..
        for i in range(10):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 400, 615, 430, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print(str(i), imgs_)
                x_reg_1 = imgs_.x
                num_find_front = True
                break
        # 맨 앞 숫자 위치 파악하기
        print("맨 앞 숫자 위치 파악하기")
        for i in range(10):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 400, 615, 430, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print(str(i), imgs_)
                if x_reg_1 > imgs_.x:
                    x_reg_1 = imgs_.x

        # 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
        print("맨앞부터 숫자 찾아 돌려서 숫자 파악하기..")
        while num_find_front is True:
            num_find_front_count += 1
            is_num = False

            if num_find_front_count == 1:
                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg_1 - plus - 4, 400, x_reg_1 - plus + 5, 430, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                        x_reg_1 = imgs_.x + 4
                        this_price += str(i)
                        is_num = True
                        break
            else:

                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg_1 - plus - 4, 400, x_reg_1 - plus + 8, 430, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                        x_reg_1 = imgs_.x + 4
                        this_price += str(i)
                        is_num = True
                        break
            if is_num == False:
                num_find_front = False
            QTest.qWait(100)


        print("this_price", this_price)



        return this_price
    except Exception as e:
        print(e)