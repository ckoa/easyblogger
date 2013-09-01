import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "EasyBlogger",
        version = "0.0.4",
        author = "Raghu Rajagopalan",
        author_email = "raghu.nospam@gmail.com",
        description = ("A (very) easy CLI interface to Blogger blogs"),
        license = "BSD",
        keywords = "blogger, cli",
        url = "https://bitbucket.org/raghur/vim-blogger",
        packages=['blogger'],
        install_requires = [
            'pypandoc',
            'google-api-python-client',
            'python-gflags',
            'httplib2'
            ],
        scripts = ['blogger/easyblogger'],
        long_description='see https://bitbucket.org/raghur/vim-blogger',
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: OSI Approved :: BSD License",
            ],
)