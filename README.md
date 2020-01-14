# zeroWtempCode

Code for raspberry pi zero W temperature probe project


## Installation

On a clean installation of Rasbian Desktop:

1. [Create a SSH Key](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
2. [Add it to GitHub](https://github.com/settings/ssh/new)
3. Check out the repositories:
```
git clone git@github.com:alfalimajuliett/zeroWtempCode.git
git clone git@github.com:alfalimajuliett/QlabTempData.git
cd zeroWtempCode
```
4. From https://pimylifeup.com/raspberry-pi-temperature-sensor/
- `sudo nano /boot/config.txt` and add `dtoverlay=w1-gpio` to the bottom of the file
- Save and exit (ctrl x ; ctrl y)
- `sudo reboot`
- Wait ...
- `sudo modprobe w1-gpio; sudo modprobe w1-therm`
5. Run `./temp_update_code.py` and verify that the CSV is updated
6. `pip install python-crontab`
7. Run `install_temp_cron=True ./temp_update_code.py` to install a cron configuration to run the program every hour
