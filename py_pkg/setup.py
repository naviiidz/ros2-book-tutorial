from setuptools import find_packages, setup
import os  
from glob import glob



package_name = 'py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2',
    maintainer_email='ros2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_installed_exec=py_pkg.first_py_node:main",
            "py_exec_publisher=py_pkg.py_publisher:main",
            "py_exec_subscriber=py_pkg.py_subscriber:main",
            "py_exec_server=py_pkg.server:main",
            "py_exec_client=py_pkg.client:main",
            "py_action_server=py_pkg.act_srv:main",
            "py_interface_sub=py_pkg.interface_sub:main",
            "py_interface_pub=py_pkg.interface_pub:main"
        ],
        
    },
)
