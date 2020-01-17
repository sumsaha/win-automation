import vmrun
import os
import subprocess
import pygetwindow
import pyautogui
import time
# import pymouse
# import mouse
from pymouse import PyMouse
from wrappers.win_driver import WinDriver
driver = WinDriver()

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELEMENT_REPO_DIR = ROOT_DIR + '/win-automation/image_objects_repo/image_repo/'
VM_PATH = r'/Applications/VMware\ Fusion.app/Contents/Public/vmrun start ' + os.path.expanduser("~") + '/Virtual\ Machines.localized/Windows\ 10\ x64.vmwarevm'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

time.sleep(2)
cmd = """osascript -e 'activate application "VMware Fusion"'"""
os.system(cmd)

driver.wait_for_image_visible('win_login_enter_pwd_textbox.png')
driver.locate_and_click_element('win_login_enter_pwd_textbox.png')
driver.type_text('12345')
# driver.locate_and_click_element('win_login_enter_arrow.png')
pyautogui.press('enter')
driver.wait_for_image_visible('win_prog_search_field.png')
pyautogui.hotkey('command', 'ctrl')
pyautogui.hotkey('command', 'g')
pyautogui.hotkey('command')
time.sleep(2)

pyautogui.typewrite('IdaptiveAgentinstaller', 0.4)
driver.wait_for_image_visible('win_installer_icon.png')
# time.sleep(2)
pyautogui.typewrite(['enter'])
# pyautogui.hotkey('ctrl', 'tab')
driver.wait_for_image_visible('win_welcome_to_idaptive_text.png')
driver.wait_for_image_visible('win_next_button_selected.png')
pyautogui.typewrite(['enter'])
driver.wait_for_image_visible('win_enter_enroll_params.png')
driver.wait_for_image_visible('win_next_button_selected.png')
pyautogui.typewrite(['enter'])
driver.wait_for_image_visible('win_manuall_enroll.png')
driver.wait_for_image_visible('win_next_button_selected.png')
pyautogui.typewrite(['enter'])
driver.wait_for_image_visible('win_install_button_selected.png')
pyautogui.typewrite(['enter'])
# driver.wait_for_image_visible('win_permission_yes_button.png')
# driver.locate_and_click_element('win_permission_yes_button.png')
driver.wait_for_image_visible_time('win_finish_button_selected.png', 60)
pyautogui.typewrite(['enter'])
driver.wait_for_image_invisible('win_finish_button_selected.png')

# pyautogui.hotkey('command', 'ctrl')
# pyautogui.hotkey('command', 'g')
# pyautogui.hotkey('ctrl', 'tab')

# enroll cloud user by executing batch file
pyautogui.hotkey('command', 'ctrl')
pyautogui.hotkey('command', 'g')
pyautogui.hotkey('command')
time.sleep(2)
driver.type_text('enrolluser.bat')
pyautogui.typewrite(['enter'])
driver.wait_for_image_visible('win_cmd_enroll_launcher.png')
driver.wait_for_image_invisible('win_cmd_enroll_launcher.png')
time.sleep(2)

pyautogui.hotkey('ctrl', 'option', 'delete')
driver.wait_for_image_visible('win_switch_user_option.png')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
time.sleep(1)
pyautogui.hotkey('enter')
driver.wait_for_image_visible('win_signout_success.png')


