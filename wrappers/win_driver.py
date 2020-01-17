import pyautogui
import pygetwindow
from pymouse import PyMouse
import time
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import vmrun


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ELEMENT_REPO_DIR = ROOT_DIR + '/image_objects_repo/image_repo/'
UTILITIES_DIR = ROOT_DIR + '/utilities/'
print(ROOT_DIR)
SCREENSHOT_REPO_DIR = ROOT_DIR + '/image_objects_repo/screenshot_repo/'
print(ELEMENT_REPO_DIR)
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
VM_PATH = r'/Applications/VMware\ Fusion.app/Contents/Public/vmrun start ' + os.path.expanduser("~") + '/Virtual\ Machines.localized/'
# VM_PATH = r'/Applications/VMware\ Fusion.app/Contents/Public/vmrun start ' + os.path.expanduser("~") + '/Virtual\ Machines.localized/Windows\ 10\ x64.vmwarevm'


class WinDriver:

    def launch_app(self, app_name, app_platform):
        os.system(VM_PATH + app_platform)
        while True:
            if "\\" in app_name:
                app_name = app_name.replace("\\", "")

            if app_name not in pygetwindow.getActiveWindow():
                time.sleep(1)
            else:
                break

    def locate_and_click_element(self, obj_name):
        WinDriver.wait_for_image_visible(self, obj_name)
        x, y = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + obj_name, grayscale=True, confidence=.7)
        point = x / 2, y / 2
        pyautogui.click(point[0], point[1])

    def locate_and_doubleclick_element(self, obj_name):
        WinDriver.wait_for_image_visible(self, obj_name)
        x, y = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + obj_name, grayscale=True, confidence=.7)
        point = x / 2, y / 2
        pyautogui.click(point[0], point[1])
        pyautogui.sleep(1)
        pyautogui.click(point[0], point[1])

    def locate_and_multipleclick_element(self, obj_name, num):
        WinDriver.wait_for_image_visible(self, obj_name)
        x, y = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + obj_name, grayscale=True, confidence=.7)
        point = x / 2, y / 2
        i = 0
        while i < num:
            WinDriver.locate_and_click_element(self, obj_name)
            i += 1

    def locate_and_click_element_accuracy(self, obj_name, accuracy):
        WinDriver.wait_for_image_visible(self, obj_name)
        x, y = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + obj_name, grayscale=True, confidence=accuracy)
        point = x / 2, y / 2
        pyautogui.click(point[0], point[1])

    def click_element(self, pointx, pointy):
        print()
        point = pointx / 2, pointy / 2
        pyautogui.click(point[0], point[1])

    def click_center_of_screen(self):
        time.sleep(2)
        x, y = pyautogui.size()
        print(x, y)
        pyautogui.click(x / 2, y / 2)
        time.sleep(1)
        pyautogui.click(x / 2, y / 2)

    def type_text(self, content):
        # WinDriver.locate_and_click_element(self, obj_name)
        pyautogui.typewrite(content, 0.25)

    def locate_and_type_text(self, obj_name, content):
        WinDriver.locate_and_click_element_accuracy(self, obj_name, 0.9)
        pyautogui.typewrite(content, 0.25)

    def validate_element_present(self, output):
        i = 1
        while i < 20:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + output, confidence=0.8, grayscale=True)
                print('Found the element, ' + output + '!')
                mouse = PyMouse()
                imgpoint = imgx / 2, imgy / 2
                mouse.click(imgpoint[0], imgpoint[1])
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                break
            except Exception:
                time.sleep(1)
                i += 1
                pass

    def wait_for_image_visible(self, imagefile):
        i = 1
        while i < 20:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + imagefile, confidence=0.8,
                                                            grayscale=True)
                print('Found the element, ' + imagefile + '!')
                imgpoint = imgx / 2, imgy / 2
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                break
            except Exception:
                time.sleep(1)
                i += 1
                pass

    def wait_for_image_visible_time(self, imagefile, timelimit):
        i = 1
        while i < timelimit:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + imagefile, confidence=0.7,
                                                            grayscale=True)
                print('Found the element, ' + imagefile + '!')
                imgpoint = imgx / 2, imgy / 2
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                break
            except Exception:
                time.sleep(1)
                i += 1
                print('Waiting for object')
                pass

    def wait_for_image_visible_accuracy(self, imagefile, accuracy):
        i = 1
        while i < 20:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + imagefile, confidence=accuracy,
                                                            grayscale=True)
                print('Found the element, ' + imagefile + '!')
                imgpoint = imgx / 2, imgy / 2
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                break
            except Exception:
                time.sleep(1)
                i += 1
                pass

    def wait_for_image_invisible(self, imagefile):
        i = 1
        while i < 20:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + imagefile, confidence=0.8,
                                                            grayscale=True)
                imgpoint = imgx / 2, imgy / 2
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                time.sleep(1)
                i += 1
            except Exception:
                print('Element, ' + imagefile + ' invisible!')
                break

    def wait_for_image_invisible_accuracy(self, imagefile, accuracy):
        i = 1
        while i < 20:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + imagefile, confidence=accuracy,
                                                            grayscale=True)
                imgpoint = imgx / 2, imgy / 2
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                time.sleep(1)
                i += 1
            except Exception:
                print('Element, ' + imagefile + ' invisible!')
                break

    def find_img_based_on_text_and_click(self, base_img, new_img_name, text_str, left_offset, top_offset):
        print(pyautogui.locateOnScreen(ELEMENT_REPO_DIR + base_img, grayscale=True, confidence=.7))
        l, t, w, h = pyautogui.locateOnScreen(ELEMENT_REPO_DIR + base_img, grayscale=True, confidence=.7)
        print(l, t, w, h)
        pyautogui.screenshot(SCREENSHOT_REPO_DIR + new_img_name, region=(l + left_offset, t + top_offset, w, h))
        im = Image.open(SCREENSHOT_REPO_DIR + new_img_name)  # the second one

        new_size = tuple(2 * x for x in im.size)
        im = im.resize(new_size, Image.ANTIALIAS)

        # im = im.filter(ImageFilter.MedianFilter())
        # enhancer = ImageEnhance.Contrast(im)
        # im = enhancer.enhance(2)
        # im = im.convert('L')
        # im = ImageOps.invert(im)
        # im = im.point(lambda m: 0 if m < 100 else 255)
        # im = im.filter(ImageFilter.SMOOTH_MORE)
        # im.save(SCREENSHOT_REPO_DIR + text_str + '_temp.jpg')

        text = pytesseract.image_to_string(im)
        print(text)
        if text_str in text:
            x, y = pyautogui.locateCenterOnScreen(SCREENSHOT_REPO_DIR + new_img_name, grayscale=True, confidence=.7)
            mouse = PyMouse()
            point = x / 2, y / 2
            mouse.click(point[0], point[1])
            mouse.click(point[0], point[1])
        else:
            print("Text not found on screen")

    def click_center_of_vm_window(self):
        var = str(os.popen('osascript ' + UTILITIES_DIR + 'get_app_bounds.scpt').read())
        var = var.split(',')
        x = int(var[1]) / 2
        y = int(var[2]) / 2
        x1 = int(x + int(var[3]))
        y1 = int(y + int(var[4]))
        pyautogui.click(x1, y1)
        time.sleep(1)
        pyautogui.click(x1, y1)

    def locate_element_and_wake_vm_window(self, imagefile):
        i = 0
        found_flag = False
        while i < 1:
            try:
                imgx, imgy = pyautogui.locateCenterOnScreen(ELEMENT_REPO_DIR + imagefile, confidence=1, region=(666, 0, 200, 200), grayscale=True)
                print('Found the element, ' + imagefile + '!')
                imgpoint = imgx / 2, imgy / 2
                # pyautogui.moveTo(imgpoint[0], imgpoint[1])
                found_flag = True
                break
            except Exception:
                # time.sleep(1)
                i += 1
                print('Waiting for object')
                pass
        if found_flag is False:
            WinDriver.click_center_of_vm_window(self)
        else:
            print("VM display didn't sleep")
