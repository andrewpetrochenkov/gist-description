import setuptools

setuptools.setup(
    name='gist-description',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/gist-description']
)
