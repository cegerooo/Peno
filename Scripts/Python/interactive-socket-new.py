from telnetlib import Telnet
with Telnet('localhost', 5000) as tn:
    tn.interact()
