from setuptools import setup, find_packages

setup(name='grackle',
      version='0.1',
      description='Grackle: Configuration Collection Invention System',
      url='http://github.com/ai4reason/grackle',
      author='cbboyan',
      license='GPL3',
      packages=find_packages(),
      scripts=[
         'bin/fly-grackle.py',
         'bin/grackle-wrapper.py',
         'paramils/param_ils_2_3_run.rb',
         'paramils/algo_specifics.rb',
         'paramils/global_helper.rb',
         'paramils/param_reader.rb',
         'paramils/stats_ils.rb'
      ],
      zip_safe=False)

