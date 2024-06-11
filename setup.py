from distutils.core import setup

setup(
  name='sentinel1decoderCustom',
  url='https://github.com/lusCombeNCut/sentinel1decoderCustom.git',
  author='Rich Hall',
  author_email='sv22482@bristol.ac.uk',
  packages=['sentinel1decoderCustom',],
  install_requires=['numpy', 'pandas'],
  version='0.1',
  license='GPL-3.0',
  description='A python decoder for ESA Sentinel-1 Level0 files',
  long_description=open('README.md').read()
)
