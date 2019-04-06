# CybTcrsAssister

## Requirement:
* Python 2.7 or above.
* Chrome browser has been installed and on Windows. 

## Installation

```pip install git+https://github.com/ClawInterspace/CybTcrsAssister.git#egg=CybTcrsAssister```

## Usage:
1. Create an "Profile.ini" for account and timecard configuration.
    * Activity option should refer to "./ProjectObject/loc/ActivityOption.py" and exactly the same to the activity name.
2. Execute:

    * ```python -m CybTcrsAssister.TcrsAssister.py```

## Extension:
* You can leverage "./PageObject/PageTcrs.py" to build your own controller.

## Limitation:
* Only support chrome on Windows/OSX


## Uninstall
* ```pip uninstall CybTcrsAssister```