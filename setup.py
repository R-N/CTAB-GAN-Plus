from setuptools import setup

setup(
    name='ctab_gan_plus',
    version='0.1.0',    
    description='',
    url='https://github.com/R-N/CTAB-GAN-Plus',
    author='',
    author_email='',
    license='',
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy>=1.25.0",
        "scikit-learn>=0.24.1",
        "dython~=0.6.4.post1",
        "torch>=1.9.1",
        "pandas>=1.2.4",
        "scipy>=1.4.1",
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)