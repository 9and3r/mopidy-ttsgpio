****************************
Mopidy-TtsGpio
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-TtsGpio.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-TtsGpio/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-TtsGpio.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-TtsGpio/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/9and3r/mopidy-ttsgpio/master.png?style=flat
    :target: https://travis-ci.org/9and3r/mopidy-ttsgpio
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/9and3r/mopidy-ttsgpio/master.svg?style=flat
   :target: https://coveralls.io/r/9and3r/mopidy-ttsgpio?branch=master
   :alt: Test coverage

Controll mopidy without screen using GPIO and TTS

For example if you play "Rather Be - Clean Bandit" you will hear:

http://translate.google.com/translate_tts?tl=en&q=rather%20be%20by%20clean%20bandit

TTS (Text To Speech) is used from google translate (It is not documented but it works).

The idea is to develop with GPIO buttons something similar to `3rd generation Ipod shuffle control <http://youtu.be/TfZUcL700wQ?t=2m40s>`_

Features
========

- Play/Pasue
- Next/Previous track
- Select playlist
- Hear the song name (Text To Speech)
- Exit mopidy
- Shutdown
- Restart
- Check IP


Installation
============

To use this extension you need an internet conection for the tts.

Install by running::

    pip install Mopidy-TtsGpio

To access the GPIO pins in the raspberry pi you have to run mopidy with sudo::
	
	sudo mopidy



Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-TtsGpio to your Mopidy configuration file::

    [ttsgpio]
    debug_gpio_simulate = false # Set true to emulate GPIO buttons with on screen buttons
    pin_button_main = 17
    pin_button_next = 22
    pin_button_previous = 23
    pin_button_vol_up = 24
    pin_button_vol_down = 25
    
You can set the pins you would like to use. The numbers are in BCM mode. You can check `here <http://raspberrypi.stackexchange.com/a/12967>`_ to see the numbers for your board.
The buttons must be connected to GROUND.

Example:

[pin 17] - [Button] - [Ground]

Controls
========

- main: play/pause. In menu select item
- main longpress: enter/exit menu
- vol_up longpress: repeat last sentence
- vol_down longpress: set the volume 0
- next: in menu navigate to next item
- previous: in menu navigate to next item

Project resources
=================

- `Source code <https://github.com/9and3r/mopidy-ttsgpio>`_
- `Issue tracker <https://github.com/9and3r/mopidy-ttsgpio/issues>`_
- `Development branch tarball <https://github.com/9and3r/mopidy-ttsgpio/archive/master.tar.gz#egg=Mopidy-TtsGpio-dev>`_


Changelog
=========

v1.0.1
----------------------------------------

- GPIO will be disabled if not enough permission

v1.0.0
----------------------------------------

- First working version

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.
