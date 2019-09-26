# Belkin WeMo

The Python package used to communicate with WeMo devices, [ouimeaux](https://ouimeaux.readthedocs.io/en/latest/), only works with Python version 3.5.7 and lower

Tested with [2nd gen Mini Smart Plug F7C063](https://www.belkin.com/us/support-article?articleNum=268606)

[Official site](https://www.wemo.com/)

[Device Setup instructions](https://www.belkin.com/us/support-article?articleNum=8218)

```
pip3 install -r wemo/requirements.txt

gardnr add driver wemo1 wemo.driver:Wemo -c device_name="My Wemo"
```
