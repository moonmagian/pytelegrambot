from setuptools import setup
setup(name='pytelegrambot',
      version='0.11',
      description='Use telegram robot APIs easily in python',
      url='http://github.com/moonmagian/pytelegrambot',
      author='moonmagian',
      author_email='moonmagian@gmail.com',
      license='WTFPL',
      install_requires=[
          'requests',
      ],
      packages=['pytelegrambot'],
      zip_safe=False)