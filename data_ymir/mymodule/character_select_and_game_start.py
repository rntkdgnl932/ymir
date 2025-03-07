import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def game_start_screen(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from stop_event18 import _stop_please


    try:

        # 실수로 새 캐릭터 클릭시...
        click_miss(cla)

        # 캐릭터 선택 화면
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            character_change(cla, character_id)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                character_change(cla, character_id)
            else:

                ready = False

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    ready = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\ready_cancle_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        ready = True
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            _stop_please(cla)
                            click_pos_2(500, 400, cla)
                            ready = True
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\ready_cancle_btn2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                ready = True
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\down_load_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 400, 660, 530, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    ready = True

                if ready == True:
                    game_ready(cla)
                    character_change(cla, character_id)
                else:
                    dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
                    if cla == 'one':
                        file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
                    if cla == 'two':
                        file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
                    if cla == 'three':
                        file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
                    if cla == 'four':
                        file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
                    if cla == 'five':
                        file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
                    if cla == 'six':
                        file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

                    same = False

                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                # 메뉴 안 열어도 됨
                                same = True
                    if same == False:
                        character_change(cla, character_id)


    except Exception as e:
        print(e)


def click_miss(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:

        # 실수로 새 캐릭터 클릭시...
        back_ready = False
        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\mooli_attack.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(65, 210, 150, 250, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 이건 잘못 클릭시 나가기
            back_ready = True
            print("mooli_attack", imgs_)
            click_pos_2(30, 55, cla)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\magic_attack.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(65, 210, 150, 250, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 이건 잘못 클릭시 나가기
                back_ready = True
                print("magic_attack", imgs_)
                click_pos_2(30, 55, cla)
        if back_ready == True:

            click_pos_2(30, 55, cla)

            for i in range(10):
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\mooli_attack.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(65, 210, 150, 250, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            # 이건 잘못 클릭시 나가기
                            print("mooli_attack", imgs_)
                            click_pos_2(30, 55, cla)
                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\magic_attack.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(65, 210, 150, 250, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                # 이건 잘못 클릭시 나가기
                                print("magic_attack", imgs_)
                                click_pos_2(30, 55, cla)

                time.sleep(0.5)




    except Exception as e:
        print(e)

def character_change(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action import out_check, menu_open
    from clean_screen import clean_screen_start

    from massenger import line_to_me
    try:



        print(str(character_id), "번으로 캐릭터 체인지")


        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

            # 실수로 새 캐릭터 클릭시...
            click_miss(cla)

            # 저장된 캐릭 번호 불러오기
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            if cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            if cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            if cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"
            if cla == 'five':
                file_path = dir_path + "\\mysettings\\myschedule\\five_now_id.txt"
            if cla == 'six':
                file_path = dir_path + "\\mysettings\\myschedule\\six_now_id.txt"

            # 캐릭터 선택 화면

            character_select_screen = False

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                character_select_screen = True
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    character_select_screen = True

            if character_select_screen == True:
                x_reg = imgs_.x
                y_reg = imgs_.y

                # select 1 (730, 360)
                # select 2 (730, 435)
                if int(character_id) == 1:
                    click_pos_2(850, 110, cla)
                    time.sleep(0.1)
                    click_pos_2(850, 110, cla)
                    time.sleep(0.1)
                else:
                    click_pos_2(850, 190, cla)
                    time.sleep(0.1)
                    click_pos_2(850, 190, cla)
                    time.sleep(0.1)

                time.sleep(0.5)
                click_pos_reg(x_reg, y_reg, cla)
                time.sleep(0.1)

                #진입 버튼 누르면서 캐릭번호 저장하기
                save = False
                save_count = 0
                while save is False:
                    save_count += 1
                    if save_count > 15:
                        save = True
                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                save = True
                            else:
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(str(character_id))
                            time.sleep(0.3)
                    else:
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(character_id))

                # 대기 화면 있는지 확인하면서 진입확인하기
                joined = False
                joined_count = 0
                while joined is False:
                    joined_count += 1
                    if joined_count > 15:
                        joined = True

                    result_out = out_check(cla)
                    if result_out == True:
                        joined = True
                        cha_select = True

                        print("게임 접속 끝")
                        time.sleep(0.1)



                    else:
                        # # 로딩중 확인
                        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\action\\loding_1.PNG"
                        # img_array = np.fromfile(full_path, np.uint8)
                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        # imgs_ = imgs_set_(250, 920, 650, 1040, cla, img, 0.8)
                        # if imgs_ is not None and imgs_ != False:
                        #     loading(cla)
                        # else:
                        #     # 게임대기화면 확인
                        game_ready(cla)
                    time.sleep(1)
            else:
                # 캐릭 번호와 체인지 하려는 번호 비교하기

                same = False

                if os.path.isfile(file_path) == True:
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        read_id = file.read()
                        if str(character_id) == str(read_id):
                            # 메뉴 안 열어도 됨
                            same = True
                            cha_select = True
                if same == False:

                    # # 포션만 채우기(수집 분해도 함)
                    # maul_potion_small_only(cla)
                    #
                    # # 장비 빼기
                    # chango_action(cla, "jangbi_in")

                    # 메뉴 열기
                    menu_open(cla)
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\action\\menu_open\\menu_post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(620, 550, 740, 640, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(375, 1000, cla)
                else:
                    print("같은 번호의 캐릭이라서 체인지 안함")

    except Exception as e:
        print(e)
#
def game_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import out_check, confirm_all
    from stop_event18 import _stop_please

    try:
        print("game_ready")
        # 장시간일 경우

        # 접속대기일 경우 기다리기

        game_ready = False

        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\ready_cancle_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            game_ready = True
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\ready_cancle_btn2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                game_ready = True
        if game_ready == True:
            wait_game(cla)
        else:
            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\login_character_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(375, 410, 580, 470, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("login_character_title", imgs_)

                for i in range(3):
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\server_select_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 550, 580, 610, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("server_select_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)

                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\login_character_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 590, 580, 660, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("login_character_title", imgs_)
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    game_ready = True
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        _stop_please(cla)
                        click_pos_2(500, 400, cla)
                        game_ready = True
                if game_ready == True:
                    wait_game(cla)
                else:
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\down_load_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(300, 400, 660, 530, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        download_game(cla)
                        time.sleep(1)
    except Exception as e:
        print(e)

def wait_game(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import out_check, confirm_all
    from stop_event18 import _stop_please
    try:
        game_ready_count = 0
        game_play_count = 0
        game_ready = True
        while game_ready is True:

            game_ready_count += 1

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\ready_cancle_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                game_play_count = 0
                print("기다리는중", game_ready_count, "초")
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\ready_cancle_btn2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 500, 600, 700, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    game_play_count = 0
                    print("기다리는중", game_ready_count, "초")
                else:
                    # 로딩중 확인
                    full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(500, 400, cla)
                    else:
                        full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            _stop_please(cla)
                            click_pos_2(500, 400, cla)

                        else:
                            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(915, 1000, cla)
                            else:
                                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\character__select__btn2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(800, 950, 960, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(915, 1000, cla)
                                else:
                                    result_out = out_check(cla)
                                    if result_out == False:
                                        game_ready = True

                                    else:
                                        game_play_count += 1
                                        print("게임 3초 대기", game_ready_count)
                                        if game_play_count > 2:
                                            game_ready = False
            time.sleep(1)
    except Exception as e:
        print(e)

def download_game(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import out_check, confirm_all
    from stop_event18 import _stop_please
    from massenger import line_to_me
    try:
        game_ready_count = 0
        game_play_count = 0
        game_ready = True
        while game_ready is True:
            game_ready_count += 1
            confirm_all(cla)

            print("downloading 1", game_ready_count, "초")

            full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\logout2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 970, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                game_ready = False
                print("downloading 2", game_ready_count, "초")
                _stop_please(cla)
                click_pos_2(500, 400, cla)
            else:
                full_path = "c:\\my_games\\ymir\\data_ymir\\imgs\\character_start\\downloading.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 960, 500, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("downloading 3", game_ready_count, "초")
                    if game_ready_count % 600:
                        result_minute = game_ready_count // 600
                        if result_minute > 0 and int(result_minute) == result_minute:
                            result_ = 10 * result_minute

                            why = "다운로드 시간이 길다" + str(result_) + "분 걸렸다."
                            line_to_me(cla, why)
                else:
                    print("downloading 4", game_ready_count, "초")
                    _stop_please(cla)
            time.sleep(1)
    except Exception as e:
        print(e)