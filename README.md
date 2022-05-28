### Install

***This module only works for Python3+***
> You need to install these packages for this module to work properly.

```
$ pip install python-dateutil
$ pip install pytz
$ pip install pendulum
```

*After installing the packages, **please clone or download the repository.***

### Usage

> Try yourself with a sample code.

***Based on the date of 9/24/2020.***

```
>>> from DTFinder import FindDT as fdt
>>> text = 'We are meeting next Thursday at 15:45, right?'
>>> get = fdt(text)
>>> get.checkDate()
2020-10-01 15:45:00+00:00
```
