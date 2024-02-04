from setuptools import setup, find_packages

setup(
    name='iracing_monitor',
    version='1.0.0',
    author='Justin Makaila',
    author_email='justin@treehousetechnology.io',
    description='An iracing telemetry server',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'irsdk'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)