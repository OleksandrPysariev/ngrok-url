from setuptools import setup, find_packages

setup(
    name='ngrok_connection',
    version='1.0.2',
    author='Oleksandr Pysariev',
    author_email='apalexlife@gmail.com',
    packages=find_packages(),
    description='Util to get ngrok url',
    extras_require={
        "sync": ["requests"],
        "async": ["aiohttp"],
    }
)
