import sys

import pyautogui
import time
import pykeyboard
import keyboard
from wrappers.win_driver import WinDriver
driver = WinDriver()


def test_win_poc():

    # launch vm
    driver.launch_app(r"VMware\ Fusion", r"Windows\ 10\ x64.vmwarevm")
    driver.wait_for_image_visible('win_login_enter_pwd_textbox.png')
    print("vm launched")

    # admin login
    # driver.locate_element_and_wake_vm_window('win_login_enter_pwd_textbox.png')
    driver.locate_and_click_element('win_login_enter_pwd_textbox.png')
    driver.type_text('12345')
    pyautogui.press('enter')
    # pyautogui.hotkey('command', 'ctrl')
    # driver.locate_and_multipleclick_element('win_prog_search_field.png', 4)
    # driver.locate_and_click_element('win_prog_search_field.png')
    # driver.locate_and_click_element('win_prog_search_field.png')
    # driver.locate_and_click_element('win_prog_search_field.png')
    # driver.click_center_of_screen()
    print("admin logged in")

    # sys.exit(1)
    # launch idaptive agent and install without enrollment
    driver.wait_for_image_visible('win_prog_search_field.png')
    driver.locate_and_doubleclick_element('win_prog_search_field.png')
    driver.wait_for_image_visible('win_quick_searches_text.png')
    # driver.wait_for_image_visible('win_search_screen_load.png')
    # driver.locate_and_click_element('win_search_app_tab.png')
    # time.sleep(1)
    pyautogui.typewrite('app: agentinstaller.bat')
    # driver.wait_for_image_visible('win_installer_icon.png')
    # time.sleep(2)
    pyautogui.typewrite(['enter'])
    driver.wait_for_image_visible('win_welcome_to_idaptive_text.png')
    driver.wait_for_image_visible('win_next_button_selected.png')
    driver.locate_and_click_element('win_next_button_selected.png')
    # pyautogui.typewrite(['enter'])
    driver.wait_for_image_visible('win_enter_enroll_params.png')
    driver.wait_for_image_visible('win_next_button_selected.png')
    pyautogui.typewrite(['enter'])
    driver.wait_for_image_visible('win_manuall_enroll.png')
    driver.wait_for_image_visible('win_next_button_selected.png')
    pyautogui.typewrite(['enter'])
    driver.wait_for_image_visible('win_install_button_selected.png')
    pyautogui.typewrite(['enter'])
    # driver.wait_for_image_visible('win_permission_yes_button.png')
    # driver.locate_and_multipleclick_element('win_permission_yes_button.png', 4)
    # pyautogui.hotkey('command', 'ctrl')
    # driver.locate_and_doubleclick_element('win_permission_yes_button.png')
    driver.wait_for_image_visible_time('win_finish_button_selected.png', 60)
    driver.locate_and_click_element('win_finish_button_selected.png')
    driver.wait_for_image_invisible('win_finish_button_selected.png')
    driver.validate_element_present('window_icon.png')
    print("launched idaptive agent and installed without enrollment")

    # enroll cloud user by executing batch file
    driver.wait_for_image_visible('window_icon.png')
    driver.locate_and_doubleclick_element('win_prog_search_field.png')
    driver.wait_for_image_visible('win_quick_searches_text.png')
    driver.type_text('app: enrolluser.bat')
    pyautogui.typewrite(['enter'])
    # driver.wait_for_image_visible('win_permission_yes_button.png')
    # driver.locate_and_click_element('win_permission_yes_button.png')
    driver.wait_for_image_visible('win_cmd_enroll_launcher.png')
    driver.wait_for_image_invisible('win_cmd_enroll_launcher.png')

    # logout admin
    driver.locate_and_click_element('window_icon.png')
    driver.locate_and_click_element('win_profile_icon_logout.png')
    driver.locate_and_click_element('win_sign_out.png')
    driver.wait_for_image_visible('win_signing_out_text.png')
    driver.wait_for_image_invisible('win_signing_out_text.png')
    driver.click_center_of_screen()

    # cloud user login with mfa

    # cloud user logout


