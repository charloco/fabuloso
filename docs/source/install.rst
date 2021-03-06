Installation
============


From Apt
--------

*FABuloso* can be installed through the *StackOps* apt repos. Just add the repos to your ``sources.list``:

.. code-block:: bash

    echo 'deb http://repos.stackops.net/ folsom main' >> /etc/apt/sources.list
    echo 'deb http://repos.stackops.net/ folsom-updates main' >> /etc/apt/sources.list
    echo 'deb http://repos.stackops.net/ folsom-security main' >> /etc/apt/sources.list
    echo 'deb http://repos.stackops.net/ folsom-backports main' >> /etc/apt/sources.list

And now you can run ``update`` and install *python-fabuloso*:

.. code-block:: bash

    $ sudo apt-get update
    $ sudo apt-get install python-fabuloso


From PyPI
---------

Before install *FABuloso* from PyPI you need to meet some requirements in your system.

First you need the latest `distribute <https://pypi.python.org/pypi/distribute/>`_ version installed. To do so you can use *pip* as follows:

.. code-block:: bash

    $ pip install --upgrade distribute

Once the latest *distribute* version is installed in your system you should install the **mysql-client** development files, **python development headers** and **git** (here you can use your favorite package manager). For example, to install those requirements in ubuntu you can run:

.. code-block:: bash

    $ sudo apt-get install -y libmysqlclient-dev python-dev git

And finally you can install *FABuloso* using *pip* or *easy_install*:

.. code-block:: bash

    $ pip install fabuloso


From Github
-----------

We recommend to install *FABuloso* into a *virtualenv*:

.. code-block:: bash

    $ virtualenv .venv
    $ source .venv/bin/activate
    (.venv)$

You can install the latest *FABuloso* from the `github repo <https://github.com/StackOps/fabuloso>`_ using pip:

.. code-block:: bash

    (.venv)$ pip install -e git+git://github.com/StackOps/fabuloso.git#egg=fabuloso

Or manually:

.. code-block:: bash

    (.venv)$ git clone git://github.com/StackOps/fabuloso.git
    (.venv)$ cd fabuloso
    (.venv)$ python setup.py install
