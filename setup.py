import setuptools

with open('README.md', 'r') as fd:
    long_description = fd.read()

setuptools.setup(
    name='aws-mfa-util',
    version='0.0.1',
    author='hiroya akita',
    author_email='akky.develop@gmail.com',
    description='AWS CLIにMFA適用アカウントを作成・更新するためのツール',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['boto3', 'PyInquirer'],
    # url='comming soon',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
