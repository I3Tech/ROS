from setuptools import setup

package_name = 'test_pkg'

setup(
    name=package_name,
    version='0.7.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Skanda Naglapur Ramamurthy',
    author_email='skanda.naglapur-ramamurthy@man.eu',
    maintainer='Skanda Naglapur Ramamurthy',
    maintainer_email='skanda.naglapur-ramamurthy@man.eu',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of action clients using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_node = test_pkg.test_node:main'
        ],
    },
)
