from setuptools import setup

setup(name='matchreport',
      version='0.1',
      description='Creates KPI reports for GAA matches',
      url='https://github.com/moynihanrory/matchreport',
      author='Rory Moynihan',
      author_email='ruaraidho@gmail.com',
      license='MIT',
      packages=['matchreport'],
      zip_safe=False,
      test_suite='matchreport',
      tests_require=['matchreport'],
      entry_points={
            'console_scripts': ['matchreport=matchreport.matchreport:main'],
      })