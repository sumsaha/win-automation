import os
import subprocess
import pyautogui
from pymouse import PyMouse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELEMENT_REPO_DIR = ROOT_DIR + '/win-automation/utilities/get_app_bounds.scpt'
mydir = ROOT_DIR + '/win-automation/utilities/'
cmd = """osascript -e 'activate application "VMware Fusion"'"""
script = '''
     tell application "System Events"
          set _P to a reference to (processes whose name = "VMware Fusion")
          set _W to a reference to windows of _P
          [_P's name, _W's size, _W's position]
     end tell
'''


def stupidtrick():
     # os.system(script)
     # os.system('osascript ' + ELEMENT_REPO_DIR)
     var = str(os.popen('osascript ' + ELEMENT_REPO_DIR).read())
     print(var)
     var = var.split(',')
     x = int(var[1])/2
     y = int(var[2])/2
     x1 = int(x + int(var[3]))
     y1 = int(y + int(var[4]))
     print(x1, y1)
     # mouse = PyMouse()
     # mouse.move(int(var[3]), int(var[4]))
     pyautogui.screenshot(mydir + 'myimg.png', region=(int(var[3])*2, int(var[4])*2, int(var[1])*2, int(var[2])*2))
     # pyautogui.screenshot(mydir + 'myimg.png', region=(269*2, 24*2, 300, 400))


cmd = """osascript -e 'activate application "VMware Fusion"'"""
os.system(cmd)
stupidtrick()