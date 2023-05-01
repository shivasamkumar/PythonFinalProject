from setuptools import setup
import os
from glob import glob 

package_name = 'mobile_robo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
        (os.path.join('share', package_name), glob('urdf/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shiva',
    maintainer_email='shiva@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ob_avoid = mobile_robo.ob_avoid:main',
            'wall_follow = mobile_robo.follow_wall:main'
        ],
    },
)
