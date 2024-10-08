# Initial Setup
1. Get image the [RetroPie Image](https://retropie.org.uk/download/)
2. Use rofus to write to SD card
3. Ket first boot happen.
4. Go to settings and then retropie settings.
5. Set wifi SSID and password manually
     (wait for a few seconds for it to connect to the wifi)
6. Click on update and let it all update
7. Reboot

# Keyboard Language 
1. F4 to exit emulationstation to the console.
2. Cd all the way to root (i.e. `cd ..`, `cd ..` etc.)
3. Type `sudo nano /etc/default/keyboard` and change the `XKBLAYOUT="gb"` to `XKBLAYOUT="{LANGUAGE}"`
4. Reboot

# Screen Setup
1. F4 to exit emulationstation to the console
2. Cd all the way to root
3. Type `sudo nano /boot/config.txt` and enter the following:
  ```
hdmi_group=2
hdmi_mode=87
hdmi_cvt=1024 600 60 6 0 0 0
hdmi_force_hotplug=1
hdmi_drive=2
```
4. Reboot

# Hide boot code log
1. F4 to exit emulationstation to the console
2. Cd all the way to root
3. Type `sudo nano /boot/cmdline.txt`
4. Do the following:
	a. Replace `console=tty1` with `console=tty3`
	b. Add `loglevel=3`
	c. Add `logo.nologo`
5. Save and exit
6. Type `sudo nano /boot/config.txt`
7. Add `disable_splash=1` at the end of the file
8. Save and exit
9. Reboot

# Add custom bootscreen (Assuming this repo is in home)
1. F4 to exit emulationstation to the console
2. Type `cp RetroPie-Reborn/Bootscreens/bootscreen_short.mp4 RetroPie/splashscreens/video/bootscreen_short.mp4`
3. Go back to the emulationstation
4. Go to settings
5. Go to retropie settings
6. Select a custom splashscreen, being the MP4 file
7. Reboot

# Run the background runner at boot (Assuming this repo is in home)
1. F4 to exit emulationstation to the console
2. Type `crontab -e`
3. Go to the end of the file, and write `@reboot sleep 10 && python3 RetroPie-Reborn/Backround-Runner/Backround_Runner.py`
4. Reboot

# Run rclone every minute (if you have rclone setup)
1. F4 to exit emulationstation to the console
2. Type `crontab -e`
3. Go to the end of the file, and write `* * * * * rclone sync /home/pi/RetroArch remote:"Real Documents/RetroArch"`
4. Reboot

