#!/usr/bin/env python


import sys
import time
from random import randint
from subprocess import Popen


def main(args):
    while True:
        Popen('dog metric post uploaded.file.size {} --tags "uploaded:filesize"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post active.connections {} --tags "connections:active"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post users.online {} --tags "users:online"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post files.transferred {} --tags "files:transferred"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post page.views {} --tags "page:views"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post files.remaining {} --tags "files:remaining"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post guild.messages.create {} --tags "guild:messageCreated"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post guild.messages.delete {} --tags "guild:messageDeleted"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post guild.messages.update {} --tags "guild:messageUpdated"'.format(randint(1, 150)), shell=True)
        Popen('dog metric post gateway.events.received {} --tags "gateway:eventsReceived"'.format(randint(1, 150)), shell=True)

        time.sleep(180)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
