try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'My Project',
  'author': 'Mark Stoecker',
  'url': 'URL to get it at.',
  'download_url': 'Where to download it.',
  'author_email': 'webmaster@desertwebdesigns.com',
  'version': '0.1',
  'install_requires': ['nose'],
  'packages': ['NAME'],
  'scripts': [],
  'name': 'projectname'
}

setup(**config)
