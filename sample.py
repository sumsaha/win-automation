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

x, y = driver.get_center_of_vm_window()
print(x, y)
mouse = PyMouse()
mouse.move(x, y)

# os.system('/Applications/VMware\ Fusion.app/Contents/Public/vmrun start /Users/akshit/Virtual\ Machines.localized/macOS\ 10.14.vmwarevm')
# os.system(VM_PATH)
# print(os.path.expanduser("~"))

# print(pygetwindow.getActiveWindow())


# time.sleep(2)
# cmd = """osascript -e 'activate application "VMware Fusion"'"""
# os.system(cmd)
# cmd2 = """osascript -e 'tell application "System Events" to set visible of application process "VMware Fusion" to false'"""
# os.system(cmd2)
# os.system('/Applications/VMware\ Fusion.app/Contents/Public/vmrun start /Users/akshit/Virtual\ Machines.localized/Windows\ 10\ x64.vmwarevm')
# time.sleep(4)
# x, y = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + 'enter_pwd_textbox.png', confidence=0.7, grayscale=True)
# print(x, y)
# point = x / 2, y / 2
# pyautogui.click(point[0], point[1])
# pyautogui.typewrite('12345', 0.25)
# pyautogui.press('enter')
# x, y = pyautogui.size()
# print(x, y)
# pyautogui.click(x/2, y/2)
# time.sleep(1)
# pyautogui.click(x/2, y/2)


# driver.wait_for_image_visible('win_login_enter_pwd_textbox.png')
# driver.locate_and_click_element('win_login_enter_pwd_textbox.png')
# driver.type_text('12345')
# time.sleep(2)
#driver.locate_and_click_element('win_login_enter_arrow.png')
# pyautogui.press('enter')
# time.sleep(3)
# pyautogui.hotkey('command', 'ctrl')
# time.sleep(2)
# pyautogui.hotkey('command', 'g')
# print(pyautogui.position())
# mouse = PyMouse()
# mouse.click(673, 60)
# pyautogui.moveTo(673, 60)
# print(pyautogui.position())
# pyautogui.hotkey('tab')
# pyautogui.press('enter')
#print(pyautogui.displayMousePosition())
# pyautogui.click(button='left', clicks=3, interval=0.25)
# pyautogui.press('enter')


# cmd2 = """osascript -e 'tell application "System Events" to set visible of application process "VMware Fusion" to false'"""
# os.system(cmd2)
# pyautogui.hotkey('command', 'ctrl')
# print(pyautogui.position())
# pyautogui.move(-600, 0)

# time.sleep(5)
# cmd = """osascript -e 'activate application "VMware Fusion"'s"""
# os.system(cmd)




# time.sleep(2)
# pyautogui.typewrite(['esc'])
# # pyautogui.hotkey('command', 'ctrl')
# pyautogui.hotkey('command', 'ctrl')
# pyautogui.hotkey('command', 'g')



# driver.locate_and_click_element('win_prog_search_field.png')
# pyautogui.hotkey('command', 'ctrl')
# print(pyautogui.position())
# pyautogui.move(-600, 0)
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_doubleclick_element('win_prog_search_field.png')
# driver.wait_for_image_visible('win_quick_searches_text.png')
# time.sleep(2)
# driver.wait_for_image_visible_time('win_prog_search_field.png', 60)
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_click_element('win_prog_search_field.png')
# driver.locate_and_click_element('win_prog_search_field.png')

# print(ELEMENT_REPO_DIR + 'win_prog_search_field.png')
# x, y = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + 'win_prog_search_field.png', grayscale=True, confidence=.7)
# mouse = PyMouse()
# point = x / 2, y / 2
# mouse.click(point[0], point[1])
# time.sleep(1)
# mouse.click(point[0], point[1])
# time.sleep(1)
# mouse.click(point[0], point[1])

# driver.locate_and_doubleclick_element('win_prog_search_field.png')
# driver.wait_for_image_visible('win_quick_searches_text.png')
# pyautogui.typewrite('IdaptiveAgentinstaller', 0.4)
# driver.wait_for_image_visible('win_installer_icon.png')
# time.sleep(2)
# pyautogui.typewrite(['enter'])
# pyautogui.hotkey('ctrl', 'tab')
# driver.wait_for_image_visible('win_welcome_to_idaptive_text.png')
# driver.wait_for_image_visible('win_next_button_selected.png')
# pyautogui.typewrite(['enter'])
# driver.wait_for_image_visible('win_enter_enroll_params.png')
# driver.wait_for_image_visible('win_next_button_selected.png')
# pyautogui.typewrite(['enter'])
# driver.wait_for_image_visible('win_manuall_enroll.png')
# driver.wait_for_image_visible('win_next_button_selected.png')
# pyautogui.typewrite(['enter'])
# driver.wait_for_image_visible('win_install_button_selected.png')
# pyautogui.typewrite(['enter'])
# driver.wait_for_image_visible('win_permission_yes_button.png')
# driver.locate_and_click_element('win_permission_yes_button.png')
# driver.wait_for_image_visible_time('win_finish_button_selected.png', 60)
# pyautogui.typewrite(['enter'])
# driver.wait_for_image_invisible('win_finish_button_selected.png')

# pyautogui.hotkey('command', 'ctrl')
# pyautogui.hotkey('command', 'g')
# pyautogui.hotkey('ctrl', 'tab')

# driver.locate_and_click_element('window_icon.png')
# driver.locate_and_click_element('win_profile_icon_logout.png')
# driver.locate_and_click_element('win_sign_out.png')
# driver.wait_for_image_visible('win_signing_out_text.png')
# driver.wait_for_image_invisible('win_signing_out_text.png')
# time.sleep(2)
# x, y = pyautogui.size()
# print(x, y)
# pyautogui.click(x / 2, y / 2)
# time.sleep(1)
# pyautogui.click(x / 2, y / 2)
# driver.wait_for_image_visible('win_other_user.png')

# driver.validate_element_present('win_cmd_exec_launcher.png')
# pyautogui.hotkey('command', 'w')
# driver.wait_for_image_invisible('win_cmd_exec_launcher.png')