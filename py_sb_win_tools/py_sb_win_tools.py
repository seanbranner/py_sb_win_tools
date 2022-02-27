import subprocess


class PySbWinTools:

    def __init__(self):
        self.number_of_connected_devices = None

    def get_number_of_connected_devices(self):
        return self.number_of_connected_devices

    def get_screen_resolution(self):
        cmd = "wmic desktopmonitor get screenheight, screenwidth"
        screen_resolution = self.run_windows_cmd(cmd).split('\n')[4].split(' ')
        y_coord_max, x_coord_max = screen_resolution[0], screen_resolution[10]
        return y_coord_max, x_coord_max

    def get_all_devices_connected_to_wifi(self):
        cmd = "arp -a"
        list_of_ip_address_and_macs = self.run_windows_cmd(cmd).split('\n')
        print(list_of_ip_address_and_macs)

    def get_list_of_all_usb_devices_connected_to_pc(self):
        cmd = "Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }"
        list_of_ip_address_and_macs = self.run_powershell_cmd(cmd).split('\n')
        return list_of_ip_address_and_macs


    def run_windows_cmd(self,cmd):
        # import subprocess
        # proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
        # (out, err) = proc.communicate()
        # print "program output:", out
        #
        # print(p)
        ###### original working way
        # return os.popen(f'cmd /c {powershell_path} "{cmd}"').read()
        # running_command = subprocess.call(f'cmd /c "{cmd}"')
        ###### newest way

        cmd_as_list = cmd.split(' ')
        running_command = subprocess.check_output(
            cmd_as_list,
            text=True,
        )
        return running_command

    def run_powershell_cmd(self,cmd):
        powershell_path = "powershell" #Path("C:\Windows\System32\WindowsPowerShell").joinpath("v1.0\powershell.exe")
        return self.run_windows_cmd(f'{powershell_path} {cmd}')

    def pc_is_connected_to_all_external_devices(self):
        self.number_of_connected_devices = len(self.get_list_of_all_usb_devices_connected_to_pc())

        if self.number_of_connected_devices > 15:
            return True
        else:
            return False

    # import pyautogui as ptg
    #
    # class PySbWinTools:
    #
    #     def __init__(self):
    #         example = None
    #
    #     def close_window(self):
    #         # ptg.press(['alt','space','c'])  # hold down the shift key
    #         ptg.press(['altright','f4'])  # hold down the shift key
    #
    #         return True
    #
    #     def open_cmd_line(self):
    #         ptg.hotkey('win')
    #         ptg.typewrite('cmd', interval=0.25)
    #         ptg.typewrite(['enter'], interval=0.25)
    #         return True
    #
    #     def open_raid_game(self):
    #         ptg.hotkey('win')
    #         ptg.typewrite('raid', interval=0.25)
    #         ptg.typewrite(['enter'], interval=0.25)
    #         time.sleep(2)
    #         self.click_button("taskBar_raidIcon")
    #         time.sleep(.5)
    #         ptg.hotkey('win', 'up')
    #         time.sleep(10)
    #         self.exit_all_ads()
    #
    #
    #     def close_game(self):
    #         ptg.hotkey('Alt', 'F4')
    #         time.sleep(2)
    #         self.click_button("button_exit_ok")
