import os
import subprocess

if __name__ == '__main__':
    print("beginning modem restarterator protocol")
    with open(os.devnull, 'w') as DEVNULL:
        while True:
            try:
                subprocess.check_call(
                    ['ping', 'cnn.com'],
                    stdout=DEVNULL,  # suppress output
                    stderr=DEVNULL
                )
                is_up = True

            except subprocess.CalledProcessError:
                print("Connection dropped, rebooting modem")
                is_up = False
                subprocess.check_call(
                    ['python', "tplink_smartplug.py", '-t', '192.168.4.69', '-c', 'reboot'],
                    stdout=DEVNULL,  # suppress output
                    stderr=DEVNULL
                )

            while not is_up:
                try:
                    subprocess.check_call(
                        ['ping', 'cnn.com'],
                        stdout=DEVNULL,  # suppress output
                        stderr=DEVNULL
                    )
                    is_up = True
                    print("We're Back")

                except subprocess.CalledProcessError:
                    is_up = False
