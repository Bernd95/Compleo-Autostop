# Compleo Autostop
## The Problem
I use the wallbox Compleo ebox Professional with firmware v2.5.1. I have a photovoltaic system with a battery. To get through a night, I need about 50% of the battery capacity. Therefore, I would like to stop the charging process when the battery level drops below 50%.
## The Solution
I borrow ideas from my [Autostart solution](https://github.com/Bernd95/Compleo-Autostart). The solution uses [Home Assistant](https://www.home-assistant.io/). The basic idea is as follows:
1. The battery level is monitored; if it remains below 50% for more than 2 minutes, the HA automation starts.
1. A python script is started. The python scripts calls the web interface of the wallbox and stops the charging session.
1. A message is sent to my cell phone.
## The Documentation
Download the files `compleo_stop.py` and `automation.yaml`. First, you have to replace a placeholder by your password in `compleo_start.py`:
- `xxx_YOUR_ADMIN_PASSWORD` has to be replaced by the password to access the wallbox. It is usually the PUK written on the back of the manual.

And in `automation.yaml`:
- `notify.xxx_mobile_app_ON_YOUR_PHONE` has to be replaced by the correct HA entity for your cell phone. This might be something like `notify.mobile_app_Toms_iPhone`.

Now you have to copy the file `compleo_stop.py` to the directory config ➔ scripts on your HA server (so the scripts directory is in the same directory as the `configuration.yaml`) and you have to make it executable with `chmod +x ...`. You can use the HA Apps `Studio Code Server` and `Terminal & SSH` to do this. In the file `configuration.yaml`, add the following lines:
```
shell_command:
  compleo_stop: "python3 /config/scripts/compleo_stop.py >> /config/compleo.log 2>&1"
```
Don't forget to restart HA now. Then create an automation using the code in automation.yaml. That's it: Connect your car and have fun...
## The Open Point
When the charging is stopped using the automation, it is not possible to restart it using e.g. the myBMW app. The session has to restarted on the wallbox, either bei unplugging/plugging the car, or by calling the wallbox directly through the web interface.
