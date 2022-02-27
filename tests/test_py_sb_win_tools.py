import unittest
from py_sb_win_tools import py_sb_win_tools

py_windows = py_sb_win_tools.PySbWinTools()

class TestPySbWinTools(unittest.TestCase):

    def test_get_screenshot_dir(self):
        actual = py_windows.get_screen_resolution()
        expected = '1080','1920'
        self.assertEqual(expected, actual)

    def test_powershell_cmd(self):
        actual_connected = py_windows.pc_is_connected_to_all_external_devices()
        actual_number_of_connected = py_windows.get_number_of_connected_devices()
        expected_connected = True
        expected_number_of_connected = 37
        self.assertEqual(expected_number_of_connected, actual_number_of_connected)
        self.assertEqual(actual_connected, expected_connected)

    def get_example_usb_devices_list(self):
        example_string = """
        Status     Class           FriendlyName                                                                     InstanceId     
        ------     -----           ------------                                                                     ----------     
        OK         USB             USB Root Hub (USB 3.0)                                                           USB\ROOT_HUB...
        OK         USB             USB Root Hub (USB 3.0)                                                           USB\ROOT_HUB...
        OK         Bluetooth       Intel(R) Wireless Bluetooth(R)                                                   USB\VID_8087...
        OK         USB             USB Composite Device                                                             USB\VID_0B05...
        OK         HIDClass        USB Input Device                                                                 USB\VID_0B05...
        OK         HIDClass        USB Input Device                                                                 USB\VID_0B05...
        OK         HIDClass        USB Input Device                                                                 USB\VID_0B05...
        """
        return example_string