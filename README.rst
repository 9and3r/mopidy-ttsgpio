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

It currently only says the song that is playing.

For example if you play "Rather Be - Clea Bandit" you will hear:

http://translate.google.com/translate_tts?tl=en&q=rather%20be%20by%20clean%20bandit

TTS (Text To Speech) is used from google translate (It is not documented but it works).

The idea is to develop with GPIO buttons something similar to `3rd generation Ipod shuffle control <http://youtu.be/TfZUcL700wQ?t=2m40s>`_




Installation
============

Not released. You can check the development (unstable):

    git clone https://github.com/9and3r/mopidy-ttsgpio/
    
    cd mopidy-ttsgpio
    
    sudo python setup.py develop


Currently not available in pipy

Install by running::

    pip install Mopidy-TtsGpio



Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-TtsGpio to your Mopidy configuration file::

    [ttsgpio]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/9and3r/mopidy-ttsgpio>`_
- `Issue tracker <https://github.com/9and3r/mopidy-ttsgpio/issues>`_
- `Development branch tarball <https://github.com/9and3r/mopidy-ttsgpio/archive/master.tar.gz#egg=Mopidy-TtsGpio-dev>`_


Changelog
=========

v0.1.0 (UNRELEASED)
----------------------------------------

- Initial release.
