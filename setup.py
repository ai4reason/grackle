from setuptools import setup, find_packages

setup(name='grackle',
      version='0.1',
      description='Grackle: Configuration Collection Invention System',
      url='http://github.com/ai4reason/grackle',
      author='cbboyan',
      license='GPL3',
      packages=find_packages(),
      scripts=['bin/fly-grackle.py','bin/grackle-wrapper.py'],
      zip_safe=False)

