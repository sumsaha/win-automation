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

driver.wait_for_image_visible('win_other_user.png')
driver.locate_and_click_element('win_other_user.png')
driver.locate_and_click_element('win_other_enter_username.png')
driver.type_text('win_suman@aaq0142')
pyautogui.press('enter')
driver.locate_and_click_element('win_other_enter_pwd.png')
driver.type_text('12345')
pyautogui.press('enter')
driver.wait_for_image_visible('win_other_enter_sq_mfa.png')
driver.locate_and_click_element('win_other_enter_pwd.png')
driver.type_text('12345')
pyautogui.press('enter')
driver.wait_for_image_visible_time('win_prog_search_field.png.png', 180)
print("got it")
