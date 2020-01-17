

class MacBase(object):
    def __init__(self, page_definition):
        self.MAC_LOGIN_WHITE_ARROW = page_definition['MAC_LOGIN_WHITE_ARROW']

    def launch_mac_vm(self):
        app = "VMware\ Fusion"
        vm_platform = "macOS\ 10.14.vmwarevm"