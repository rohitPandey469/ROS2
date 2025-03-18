from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'talker_listener'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch/'), glob('launch/*launch.[pxy][yma]')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rohit-pandey',
    maintainer_email='rd8614196@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talkerNode = talker_listener.talker_node:main',
            'listenerNode = talker_listener.listener_node:main',
        ],
    },
)
