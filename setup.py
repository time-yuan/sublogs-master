from setuptools import setup

setup(
    name='aiologs',
    version='0.0.5',
    description=(
    '修改支持关键信息不分词',
    '纯异步的高性能日志组件，支持日志保存文件、mongo、elasticsearch',
    'Purely asynchronous high performance logging components，Support for writing files，mongo、elasticsearch'
     ),
    long_description=open('README.rst', 'rb').read(),
    author='yuanYW',
    author_email='1030327908@qq.com',
    maintainer='yuanYW',
    maintainer_email='1030327908@qq.com',
    license='MIT',
    packages=['sublogs'],
    platforms=["all"],
    url='https://github.com/time-yuan/sublogs-master',
    install_requires=[
        'uvloop',
        'motor',
        'elasticsearch-async',
        'ujson',
        'aiofiles',
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)