from setuptools import setup, find_packages

setup(
    name="translate_bookmark",
    version='1.0',
    description='自分がよくみるサイトの翻訳手助けツール',
    author='Kobori Akira',
    author_email='private.beats@gmail.com',
    url='https://github.com/koboriakira/translate-packerscom',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      packers = translate_bookmark.main:cli
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)
