from setuptools import setup

setup(name='calculator',
      version='0.1',
      description='basic calculator',
      url='http://github.com/budnyjj/calculator',
      author='Roman Budny',
      author_email='budnyjj@gmail.com',
      license='MIT',
      packages=['calculator'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points = {
          'console_scripts': [
              'calc = calculator.cli:main'
          ]
      }
)
