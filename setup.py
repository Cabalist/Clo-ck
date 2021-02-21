#!/usr/bin/env python3

"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

setup(
        name="clo²ck",
        app=["clolock.py"],
        options={'py2app': {'iconfile': 'clock.icns',

                            'plist': {
                                'CFBundleShortVersionString': '1.0.0',
                                'CFBundleVersion': "1.0.0",
                                'CFBundleIdentifier': 'com.technoloft.clolock',
                                'CFBundleName': 'clo²ck',
                                'CFBundleDisplayName': 'clo²ck',
                            },

                            'includes': [
                                'clolock.py'

                            ]
                            }},

)
