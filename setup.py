#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2012>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Setup script.
"""

from setuptools import setup, find_packages

with open('requirements.txt') as requirements, \
        open('test_requirements.txt') as test_requirements:
    setup(
        name='aloe_django',
        version='0.0.1',
        description='Package for testing Django applications with Aloe',
        author='Gabriel Falcao',
        author_email='gabriel@nacaolivre.org',
        url='https://github.com/koterpillar/aloe_django',
        long_description=open('README.md').read(),
        classifiers=[
            'License :: OSI Approved :: ' +
                'GNU General Public License v3 or later (GPLv3+)',
        ],

        packages=find_packages(exclude=['tests']),
        package_data={
            'aloe_django': [
                'README.md',
                'requirements.txt',
                'test_requirements.txt',
            ],
        },

        install_requires=requirements.read().splitlines(),

        test_suite='tests',
        tests_require=test_requirements.read().splitlines(),
    )
