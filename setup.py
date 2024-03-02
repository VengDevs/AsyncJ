from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='asyncj',
  version='1.1.2',
  author='VengDevs',
  description='Python module for fast asynchronous work with JSON files',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/VengDevs/AsyncJ',
  packages=find_packages(),
  install_requires=['aiofiles', 'ujson'],
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='async json',
  python_requires='>=3.8',
  license="MIT License"
)