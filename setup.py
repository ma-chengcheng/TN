import setuptools

setuptools.setup(
    name='TN',
    version='0.0.6',
    license='Apache License 2.0',
    author='MaChengCheng',
    author_email='macheng@mail.ustc.edu.cn',
    description='g2pW',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ma-chengcheng/TN',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
