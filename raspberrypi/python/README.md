# rpi-py-test-code
Raspberry Pi Python Test Code
### To test python
```
./python1_test.py
```

### to test python3
```
./python3_test.py
```

### Common commands
```
default user/pass - pi/raspberry

sudo raspi-config
 - expand_rootfs (expands fs to ocupy all of the SD card)
 - overscan (extends the display to use whole screen)
 - change_pass (changes the password to the pi user)
 - overclock (use for pi1, use with pi2 unknown)
 - ssh (enable to SSH into pi)
 - boot_behaviour (enable to boot to GUI)

startx (starts the GUI from CLI)

sudo apt-get install rpi-update
sudo rpi-update
sudo apt-get install python3-pip
pip install rpi.gpio
```

### Common Python code
```
message = input("Type a message to yourself: ")
print("You said:", message)


number = int(input("Type a number:"))
print("You entered:", number)
```

### LED

### Input

### Servo
- https://www.youtube.com/watch?v=SGwhx1MYXUs

### Stepper
- https://www.youtube.com/watch?v=LUbhPKBL_IU&t=1203s
- https://www.youtube.com/watch?v=Dc16mKFA7Fo&t=450s
- https://www.youtube.com/watch?v=bkqoKWP4Oy4


### Links
- https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all
- https://www.youtube.com/playlist?list=PLGs0VKk2DiYypuwUUM2wxzcI9BJHK4Bfh