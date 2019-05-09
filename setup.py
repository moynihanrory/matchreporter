from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='matchreporter',
      version='0.2',
      description='Creates analysis reports for GAA matches',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.5',
            'Natural Language :: English',
            'Topic :: Text Processing :: Linguistic',
      ],
      url='https://github.com/moynihanrory/matchreporter',
      author='Rory Moynihan',
      author_email='ruaraidho@gmail.com',
      license='MIT',
      packages=['matchreporter'],
      install_requires=[
            'pandas',
            'xmltodict',
            ],
      keywords='matchreporter',
      zip_safe=False,
      test_suite='tests',
      tests_require=['matchreporter'],
      entry_points={
            'console_scripts': ['matchreporter=matchreporter.matchreporter_cli:main'],
      })