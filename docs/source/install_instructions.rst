Installation Instructions
=========================

The package can be installed from its `GitHub repository <https://github.com/MatthewTe/mail_socket_api>`_ using
the pip package manager:
::

 pip install git+https://github.com/MatthewTe/mail_socket_api.git

The necessary dependencies should also be installed via python's setuptools. However if they do not they can be
installed via pip using the requirements.txt file:
::

 pip install -r requirements.txt


pyzmail
*******
The pyzmail default package installer will throw an error if it is installed using the default method on python > 3.5.2.
This is why the pyzmail36 package is listed in the requirements.txt file. If for some reason you need to used an older version of
pyzmail, you must install it using easy install:
::

 easy_install pyzmail

This should not be done normally however as the project was written to support pyzmail36 and is not officially compatible with previous versions.
