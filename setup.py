from setuptools import setup, find_packages

setup(
    name="core",  # ім'я пакета, яким користувачі будуть його встановлювати
    version="0.1.0",
    packages=find_packages(),  # автоматично знайде всі пакети (core і Fields)
    install_requires=[
        # сюди додай залежності, якщо вони є, наприклад:
        # "requests>=2.28.0",
        "mysql-connector-python>=8.0.36"
    ],
    author="bogdanAntonjuk",
    author_email="bogdan.antonjuk@gmail.com",
    description="Core package for your project",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/test_package/core",  # якщо будеш публікувати на GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)