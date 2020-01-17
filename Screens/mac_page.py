import os
from bases.mac_base import MacBase


class MacPage(MacBase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    IMAGE_REPO_DIR = ROOT_DIR + '/image_repo/'

    def __init__(self):
        page_definition = {
            "MAC_LOGIN_WHITE_ARROW": self.IMAGE_REPO_DIR + 'mac_login_white_arrow.png'

        }
        super().__init__(page_definition)