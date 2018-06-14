Please run this program on Yanshee. 

## Branch
git checkout master

## Install adb
sudo apt-get install -y adb

## Requirements
Tips: There is no need to do this step on some devices. You can do this step when error occur on the Run step.
* 有些机器人系统里可能安装过这些库，可以先跳过这一步，后面报错找不到库再回来安装。
```shell
pip install xxx
```
This project need the following libs
```shell
backports.functools-lru-cache==1.4
cycler==0.10.0
matplotlib==2.1.1
numpy==1.13.3
olefile==0.44
opencv-python==3.4.0.12
Pillow==4.3.0
pyparsing==2.2.0
python-dateutil==2.6.1
pytz==2017.3
six==1.11.0
tensorflow==1.4.0
pandas==0.22.0
scipy==1.0.0
scikit_learn==0.19.1
```

## Prepare
* Connect Android phone to Yanshee by USB.
    >用usb先连接机器人喝Yanshee
* Enable "USB debugging" on phone's settings.
    >打开手机-开发者选项-USB调试，弹出连接提醒时，记住并确认设备
* Execute "adb devices" on Yanshee, and ensure you can find in result.
    >在Yanshee上，用"adb devices"查看设备列表中是否有你的手机
* Open WeChat jump game("跳一跳") and start game.
    >启动跳一跳程序，点击开始。

## Run
```shell
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/1xrobot/lib
python wechat_jump_auto.py --start xxx --down xxx --up xxx --reset xxx
===========
args:
    --start: The action of start game for robot
    --down: Put down robot's hand
    --up: Put up robot's hand
    --reset: The action of finish game
```

## Stop
```shell
按ctrl+c退出程序(control + c to exit program)   
```

## Accuracy
如果需要修改精确度，不想每次都正中中心，可以修改代码
wechat_jump_auto.py中，对press_time加一个数。
```shell
def jump(distance):
    press_time = distance * press_coefficient + random.randint(1, 50)  # 1: min, 50: max
```

## Robot actions
>用Yanshee-APP创建四个动作，分别是准备姿势、按压屏幕、松开、复位
完成后，通过APP上的分享按钮，将动作推到Yanshee存储里。
>在Yanshee文件目录中确认有以上动作： /usr/local/recv/