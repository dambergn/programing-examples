#!/usr/bin/env python3

import os
import platform
operatingSystem=os.name
osPlatform=platform.system()
osRelease=platform.release()

print("OS: " + operatingSystem + " | Platform: " + osPlatform + " | Release: " + osRelease)