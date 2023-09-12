# BattleBotMK2-Example
This is the code for the battlebot MK2 - 2023.
Feel free to use this code for reference for building battlebots this year. Don't just copy and paste, you should try to understand whats happening in the code, not to mention their are configs you should change. The code should be entirly self contained so it should run in default micropython. If you have any questions ask your build captain.

Language - Micropython

Processer - Raspberry Pi Pico W

Connection Type - Wifi UDP Packets are used to pass packets containing controller inputs

# How To Set UP
- You will have to change some contents like the ip address and the pins
- Go into "imports/secrets.py" and fill in the appropriate information "" and "", put in your wifi network's name and password respectivly
- secrets.py is highly unsecure and is an obvious security risk, do not share your secrets.py file as it is unhashed and not encrypted in the slightest
- Put the contents of the bot directory into the root of the Raspberry Pi Pico
  
- Running "runner.py" should result in a solid green light on the Pi, if there is any blinking the error codes are as follows
0 - Solid Light, no errors
1 -
2 -

If any of these errors are found, reset the Pi though a power cycle or other reset method


- Then you can run sender.py with the correct connection information to start sending controller signals to the pi
- computer and pi must be on same network
- Assuming everything is correct, you should get printouts from both the computer and the pi, with printouts being the same
- You can remap any controls in "computer/imports/controller.py" line , def mapper()
- For any questions ask current build captian

  

Here is the wiring diagram for BattleBotMK2

