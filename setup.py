from distutils.core import setup

from setuptools import find_packages
import sys
import os

src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)


def main():
    setup(
        name='CybTcrsAssister',
        version='1.0.0',
        description='Tool for Cybersoft Tcrs',
        author='Claw Interspace',
        author_email='alanliu71104@gmail.com',
        url='https://github.com/ClawInterspace/CybTcrsAssister',
        packages=[
            'CybTcrsAssister', 
            'CybTcrsAssister.Control',
            'CybTcrsAssister.PageObject',
            'CybTcrsAssister.PageObject.loc',
            'CybTcrsAssister.utils'
        ],
        package_dir={
            '': 'src',
        },
        scripts=['chromedriver'],
        install_requires=['numpy', 'selenium']
    )


if __name__ == "__main__":
    main()