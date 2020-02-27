emwiki
====

Wiki for eco-Mizar

## Description
This Web application can write a TeX-format description in the Mizar Mathmatical Library (MML), and make the description follow the MML update. This Web application provides users with the function of adding, editing, and browsing description of MML on a Wiki format Web platform. If there is an update to the MML, link the description to the new MML by running the program on the server.

## Demo
![emwiki](https://user-images.githubusercontent.com/49423101/75423437-0c960400-5982-11ea-86e5-382c462a6fc7.png)

## Requirement
written on pipfile
+ Python
+ Django

## Install
### git clone
```
git clone https://github.com/mimosa-project/emwiki.git
```

### install Python
```
sudo apt install python3.7 python3.7-dev
```
### install pip3
```
sudo apt install python3-pip
```

### sync pipenv
```
cd <piplock folder>
```
```
pipenv sync
```

### make local_settings.py
```
pipenv shell
```
```
cd emwiki/emwiki
```
```
python generate_secretkey_setting.py > local_settings.py
```


## Licence

![MIT License](https://github.com/mimosa-project/emwiki/blob/master/LICENSE)

