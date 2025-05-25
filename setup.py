from setuptools import setup

setup(name='dpsctl',
      version='0.1',
      description='Python utility to interact with OpenDPS firmware for DPS5005 power supplies',
      url='https://github.com/kanflo/opendps',
      author='Johan Kanflo',
      author_email='watski@bitfuse.net',
      license='MIT',
      packages=['dpsctl'],
      entry_points = {
            'console_scripts': [
                  'dpsctl = dpsctl:main',
            ],
      },
      zip_safe=False)
