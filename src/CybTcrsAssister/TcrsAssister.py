# -*- coding: utf-8 -*-

import getpass

from CybTcrsAssister.Control.TcrsAgent import Agent


office_pwd = getpass.getpass("Please input your domain password:")

agent = Agent("Profile.ini", office_pwd)
agent.navigate_to_timecard_page()
agent.run_steps()
