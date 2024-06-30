#!/usr/bin/env python

import subprocess
import optparse


def fetch_options():
    option_juggler = optparse.OptionParser()
    option_juggler.add_option("-i", "--interface", dest="net_interface", help="Network interface to change its MAC")
    option_juggler.add_option("-m", "--mac", dest="mac_alias", help="New MAC address")
    return option_juggler.parse_args()


def mac_morph(net_interface, mac_alias):
    print("[+] Misdirecting Ether ID for " + net_interface + " to " + mac_alias)
    subprocess.call(["ifconfig", net_interface, "down"])
    subprocess.call(["ifconfig", net_interface, "hw", "ether", mac_alias])
    subprocess.call(["ifconfig", net_interface, "up"])


(mac_options, arguments) = fetch_options()
mac_morph(mac_options.net_interface, mac_options.mac_alias)
