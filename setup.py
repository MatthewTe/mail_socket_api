import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mail_data_transfer_api",
    version="0.1.1",
    author="MatthewTe",
    description="An API that facilitates small data transfers through SMTP and IMAP mail servers.",
    long_description=long_description,
    url="https://github.com/MatthewTe/mail_socket_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: - Alpha",
        "Topic :: Data Science :: Pipeline API",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Windows"]
    )
