from setuptools import setup

__version__ = 'development'
try:
    exec(open('viberbot/version.py').read())
except Exception as e:
    print('Could not read version, used "development". Error: %s' % e)


setup(
    name='viberbot',
    version=__version__,
    packages=[
        'viberbot',
        'viberbot.api',
        'viberbot.api.viber_requests',
        'viberbot.api.messages',
        'viberbot.api.messages.data_types',
    ],
    install_requires=['future', 'requests'],
    url='https://github.com/Viber/viber-bot-python',
)
