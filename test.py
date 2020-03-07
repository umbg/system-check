import os
import subprocess




def main():


    pass


def is_connectable(host):
    ping = subprocess.Popen(["ping", "-w", "3", "-c", "1", host], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    ping.communicate()
    return ping.returncode == 0


if __name__ == '__main__'

    main()