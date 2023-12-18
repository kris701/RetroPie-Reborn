# RetroPie-Reborn
This is a project to make a handheld console, that can run games from around PlayStation 1 and down.

![image](https://github.com/kris701/RetroPie-Reborn/assets/22596587/457b64c3-be7e-4017-ac84-7944155a2cc2)
![image](https://github.com/kris701/RetroPie-Reborn/assets/22596587/91f9d0c1-ea45-422b-b058-9d67b8009737)

Its basically a Raspberry Pi 4 that runs on RetroPie. It has small icons that show up in the corner, to give info in things such as how much battery is left or if the Pi is connected to Wifi.
Hardware wise, it has a 7' LCD screen, two small speakers, AUX output, USB-A output and USB-C charging port.
It has two 5000mAh batteries inside of it, giving it ~4 hours of normal usage before running out (but it really depends on what you use it for).
The console also has a little fan, that automatically turns on and off depending on the internal temperature of the Pi.

I originally designed it to include build in controllers on the side, however making the PCBs for the button pads didnt work out.
As a backup, i build in a connector on the two sides of the console, that can be used for future controller additions. 
Each side is basically mirrored, pinout wise, where each side supports up to 11 buttons (or 9 buttons and 2 analog inputs). Each side also have a GND and +5V pin.
