.. raw:: html

    <embed>
        <p align="center">
            <img width="250" src="https://github.com/yngtodd/orbiter/blob/master/img/orbiter.png">
        </p>
    </embed>

--------------------------

=======
Orbiter
=======

Help mission control guide their Mars orbiter!

Orbiter is a simple control game created by `Lee Vaughan`_ using Kepler's laws of planetary motion.
The design of the game, along with its source code, was originally published in
Lee's excellent book, `Impractical Python Projects`_. I highly recommend Lee's book as well as many of
the other wonderful books offered by `No Starch Press`_.

This repository stands as a refactored version of Mr. Vaughan's source code. It was created with two aims:
one, to make it simple to extend the game, and, more importantly, two, to make the game into an environment
for reinforcement learning algorithms in the style of OpenAI's `gyms`_.

Documentation
--------------
 
For references, tutorials, and examples check out our `documentation`_.

Installation
------------

From Sources:

You can either clone the public repository:

.. code-block:: console

    git clone git://github.com/yngtodd/orbiter

Or download the `tarball`_:

.. code-block:: console

    curl  -OL https://github.com/yngtodd/orbiter/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    python setup.py install

.. _tarball: https://github.com/yngtodd/orbiter/tarball/master
.. _documentation: https://orbiter.readthedocs.io/en/latest

.. _Lee Vaughan: https://github.com/rlvaugh/Impractical_Python_Projects
.. _Impractical Python Projects: https://nostarch.com/impracticalpythonprojects
.. _No Starch Press: https://nostarch.com/
.. _gyms: https://gym.openai.com/
