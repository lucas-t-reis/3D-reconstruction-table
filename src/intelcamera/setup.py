from setuptools import setup, find_packages

setup(
    name='intelcamera',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyrealsense2',
        'numpy',
        'opencv-python'
    ]
)
