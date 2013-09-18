from setuptools import setup, find_packages
import os
from os.path import join


NAME = 'Solgema.PortletsManager'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(join(*PATH)).read().strip()


setup(name=NAME,
      version=VERSION,
      description="Solgema Portlets Manager",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Solgema',
      author='Martronic SA',
      author_email='martronic@martronic.ch',
      url='http://www.martronic.ch/plone_products/Solgema.PortletsManager',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Solgema'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.jqueryui',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
