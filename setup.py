#from distutils.core import setup
from setuptools import setup

setup(
    name='dhl_delivery',
    version='2.0.5',
    author='Iván Salazar',
    author_email='ivangio.salazar@gmail.com',
    packages=['dhl_delivery'],
    url='http://pypi.python.org/pypi/dhl_delivery/',
    license='LICENSE.txt',
    description='DHL Capability - Quote, Pick Up, delivery, Label Creation, Tracking',
    long_description=open('README.md').read(),
    install_requires=[
        'xmltodict',
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
