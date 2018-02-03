# coding=utf8

from __future__ import unicode_literals

from setuptools import setup

lib_classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Framework :: Django",
    "Framework :: Django :: 2.0",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    'Operating System :: OS Independent'
]

packages = [
    'django_echarts',
    'django_echarts.conf',
    'django_echarts.datasets',
    'django_echarts.management',
    'django_echarts.management.commands',
    'django_echarts.plugins',
    'django_echarts.templatetags',
    'django_echarts.utils',
    'django_echarts.views',
]

setup(
    name='django-echarts',
    version='0.3.0b1',
    packages=packages,
    url='https://github.com/kinegratii/django-echarts',
    install_requires=['Django'],
    include_package_data=True,
    license='MIT',
    author='Kinegratii',
    author_email='kinegratii@gmail.com',
    description='A django app for Echarts integration with pyecharts as chart builder. ',
    classifiers=lib_classifiers
)
