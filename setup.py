#!/usr/bin/python3
'''
    import botogram
    bot = wgnbot.create("API-KEY")

    @bot.command("hello")
    def hello_command(chat, message, args):
        """Say hello to the world!"""
        chat.send("Hello world")

    if __name__ == "__main__":
        bot.run()


'''

import setuptools


setuptools.setup(
    name = "wgnbot",
    version = "0.6.2",
    url = "https://madewgn.my.id",

    license = "MIT",

    author = "The botogram authors",

    description = "A Python framework for Telegram bots",
    long_description = __doc__,

    packages = [
        "wgnbot",
        "wgnbot.objects",
        "wgnbot.runner",
        "wgnbot.utils",
    ],

    install_requires = [
        "logbook",
        "requests",
        "typing"
    ],

    include_package_data = True,
    zip_safe = False,

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
