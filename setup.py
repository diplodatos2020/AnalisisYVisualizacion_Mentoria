# -*- coding: utf-8 -*-

"""
Set-up
-----------------
"""

from distutils.core import setup


setup(
    name='mentoria-ayv',
    version='1.0',
    description='Analisis y visualizacion de datos',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'jupyterlab',
        'scipy',
        'xlrd'
    ]
)
