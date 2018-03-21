try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Exercise 47',
  'author': 'Mark Stoecker',
  'url': '',
  'download_url': '',
  'author_email': 'webmaster@desertwebdesigns.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'Exercise 47'
}

setup(**config)
