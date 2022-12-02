from setuptools import setup, find_packages

setup(
    name='ngrok_connection',
    version='1.0.1',
    author='place author here',
    author_email='place email here',
    packages=find_packages(),
    description='Util to get ngrok url',
    extras_require={
        "sync": ["requests"],
        "async": ["aiohttp"],
    }
)
