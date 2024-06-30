#!/usr/bin/env python

import subprocess
import optparse

# Create the option juggler
optionJuggler = optparse.OptionParser()

# Add options for the network interface and new MAC address
optionJuggler.add_option("-i", "--network-interface", dest="netInterface", help="Network interface to change its Ether ID")
optionJuggler.add_option("-m", "--mac-alias", dest="macAlias", help="New MAC address")

# Parse the command-line arguments
(macOptions, arguments) = optionJuggler.parse_args()

netInterface = macOptions.netInterface
macAlias = macOptions.macAlias

# Display the change operation
print("[+] Misdirecting Ether ID for " + netInterface + " to " + macAlias)

# Execute the commands to change the MAC address
subprocess.call(["ifconfig", netInterface, "down"])
subprocess.call(["ifconfig", netInterface, "hw ether", macAlias])
subprocess.call(["ifconfig", netInterface, "up"])
