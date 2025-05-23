import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random
    import pytesseract
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for, drag_pos, text_check_get, text_check_get_black_white
    from action import out_check, juljun_off, juljun_on, juljun_check, confirm_all, fix_bag_item
    from game_check import move_check, dun_check, check_start
    from get_item import get_item_start, get_event, get_pass, get_sangjum_gyohwan, get_just_wonjung, get_daily_mission
    from potion import potion_buy
    from chango import go_chango, chango_start, chango_maul_auction, chango_in, chango_maul_spot
    from request import request_get, request_start
    from clean_screen import clean_screen_go
    from dungeon import dungeon_in, random_spot_dun, dungeon_hondon_folk
    from boonhae_collection import collection_start, boonhae_start, collection_upgrade
    from auction_game import auction_in, auction_low_num, auction_qun_num, auction_start, auction_fast_start
    from migoong import migoong_start
    from jadong import random_spot_in, jadong_start
    from upgrade import upgrade_start
    from chaejib import chaejib_start

    print("test")
    cla = "one"

    plus = 0


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

        # request_get(cla, "외뢰_2")
        # 미궁_스비파_5
        # migoong_start(cla, "미궁_카라_1")

        # data = "혼돈_일반_5"
        # #
        # # random_spot_dun(cla, data)
        #
        # dungeon_hondon_folk(cla, data)

        # get_just_wonjung(cla)

        # \menu_
        # this_point_x
        # this_point_x_plus = 80

        # jilyung_get(cla)

        # fix_bag(cla)

        fix_bag_item(cla)

        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\out_check\\out_check.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 800, 60, 900, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("out_check", imgs_)
        #
        # for i in range(5):
        #     full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\jaelyo_in_ready.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(125, 100, 210, 160, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         print("jaelyo_in_ready", imgs_)
        #         break
        #     else:
        #         click_pos_2(850, 130, cla)
        #     time.sleep(1)


        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\click_request_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(835, 135, 920, 190, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("click_request_btn", imgs_)

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\season_jilyung\\season_jilyung_ready.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 130, 920, 190, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("season_jilyung_ready", imgs_)

        # auction_fast_start(cla)

        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\is_pic\\hondon.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(690, 310, 945, 655, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("hondon :", imgs_)
        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\is_pic\\folk.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(690, 310, 945, 655, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("folk :", imgs_)
        # click_pos_2(480, 520, cla)
        # time.sleep(3)
        # for i in range(15):
        #     click_pos_2(855, 890, cla)
        #     time.sleep(0.05)
        # time.sleep(5)
        # for i in range(15):
        #     click_pos_2(855, 890, cla)
        #     time.sleep(0.05)
        # time.sleep(3)
        # for i in range(15):
        #     click_pos_2(855, 890, cla)
        #     time.sleep(0.05)

        # for i in range(10):
        #     full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
        #         v_.data_folder) + "\\imgs\\check\\game_title_1.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(0, 0, 960, 1030, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("game_title_1", imgs_)
        #         result_confirm = confirm_all(cla)
        #         if result_confirm == False:
        #             click_pos_2(935, 15, cla)
        #     else:
        #         break
        #     QTest.qWait(1000)

        # attack_check(cla)

        # result_low = auction_low_num(cla)
        # print("==========================================================================")
        # result_qun = auction_qun_num(cla, 630, 660)
        # print("==========================================================================")
        # result_price = auction_qun_num(cla, 665, 700)
        #
        # print("result_low", result_low)
        # print("result_qun", result_qun)
        # print("result_price", result_price)
        #
        # result_ = int(result_low * result_qun)
        #
        # print("result_", result_)

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\auction\\enroll_information_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 310, 540, 360, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("enroll_information_title", imgs_)



        # ################### collection ##################
        #
        # result_get_1 = text_check_get_black_white(30, 85, 170, 110, cla)
        # print("result_get_1", result_get_1)
        #
        #
        # for i in range(30):
        #     result_get_2 = text_check_get_black_white(30, 85, 170, 110, cla)
        #     print("result_get_2", result_get_2)
        #     if result_get_1 != result_get_2:
        #         break
        #     time.sleep(1)
        #
        # print("last result", result_get_1, result_get_2)

        # x1 = 30
        # y1 = 85
        # x2 = 170
        # y2= 110
        #
        # # 이전 숫자 저장
        #
        # # 화면의 지정된 부분 캡처
        # screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        #
        # # 이미지를 흑백으로 변환
        # screenshot = screenshot.convert('L')
        #
        # # 이미지에서 텍스트 추출
        # current_text = pytesseract.image_to_string(screenshot, config='--psm 6').strip()
        #
        # previous_number = current_text
        #
        # print("previous_number", previous_number)
        #
        # # 실시간 숫자 감지
        # while True:
        #     # 화면의 지정된 부분 캡처
        #     screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        #
        #     # 이미지를 흑백으로 변환
        #     screenshot = screenshot.convert('L')
        #
        #     # 이미지에서 텍스트 추출
        #     current_text = pytesseract.image_to_string(screenshot, config='--psm 6').strip()
        #
        #     # 텍스트가 숫자로 바뀌었는지 확인
        #     if current_text.isdigit():
        #         if current_text != previous_number:
        #             print(f'숫자가 바뀌었습니다! 이전: {previous_number}, 현재: {current_text}')
        #             previous_number = current_text
        #         else:
        #             print("아직 숫자가 바뀌지 않음")
        #     # 0.1초 간격으로 화면 캡처
        #     time.sleep(1)


        # ran_x = random.randint(100, 200)
        # print("result", ran_x)
        #
        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\dungeon\\dun_complete.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(805, 255, 870, 320, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("dun_complete", imgs_)

        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\get_item\\event_title_point_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(275, 380, 300, 720, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("event_title_point_1", imgs_)

        # prohibition = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition"
        # prohibition_list = os.listdir(prohibition)
        #
        # for i in range(len(prohibition_list)):
        #     result_prohibition_list = prohibition_list[i].split(".")
        #     read_data = result_prohibition_list[0]
        #     print("read_data", read_data)
        #     full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition\\" + str(
        #         read_data) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(210, 140, 460, 220, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         print("prohibition_list", str(read_data), imgs_)
        #         is_prohibition = True

        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\end_btn.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(480, 570, 630, 630, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("end_btn")
        #
        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\request\\prohibition\\15.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(210, 100, 460, 960, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("prohibition_list", imgs_)
        # full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\chango\\bag_auction_item.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_for = imgs_set_for(730, 110, 960, 1000, cla, img, 0.8)
        # if imgs_for is not None and imgs_for != False:
        #     print("bag_auction_item", imgs_for)
        #
        #     if len(imgs_for) > 0:
        #         for i in range(len(imgs_for)):
        #             click_pos_reg(imgs_for[i][0] - 15, imgs_for[i][1] + 15, cla)
        #             time.sleep(1)


        ####################### file list#################################
        # out_potion = "c:\\my_games\\ymir\\data_ymir\\imgs\\potion\\out"
        # out_list = os.listdir(out_potion)
        # for i in range(len(out_list)):
        #     result_file_list = out_list[i].split(".")
        #     read_data = result_file_list[0]
        #     print("read_data", read_data)

    except Exception as e:
        print(e)
        return 0

def send_message(token, chat_id, text):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response

