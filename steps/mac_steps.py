import pyautogui
from wrappers.win_driver import WinDriver
import time
import pykeyboard
import keyboard
driver = WinDriver()


class MacSteps:

    def __init__(self):
        pass

    def launch_vm(self):
        app = r"VMware\ Fusion"
        vm_platform = r"macOS\ 10.14.vmwarevm"
        driver.launch_app(app, vm_platform)
        driver.wait_for_image_visible('x_mark_restoring_vm_state.png')
        driver.wait_for_image_invisible('x_mark_restoring_vm_state.png')
        driver.locate_and_doubleclick_element('admin_login_name.png')


