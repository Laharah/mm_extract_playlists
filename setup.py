from setuptools import setup

setup(
    name='mm_extract_playlists',
    version='0.1.1',
    url='',
    license='MIT',
    author='laharah',
    author_email='laharah22+mmxp@gmail.com',
    description='Extract playlists from a MediaMonkey database',
    packages=['mm_extract_playlist'],
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=[],
    tests_require=[
        'pytest',
        ],
    entry_points={
        'console_scripts': [
            'extractPlaylists = mm_extract_playlist.__main__:entry_point',
            ]
    }

)
