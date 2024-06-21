Aspects Extension Example Tutor Plugin
######################################

Example tutor plugin for extending Aspects functionality with custom Superset Assets. This plugin does nothing special, it's just a way of illustrating how you can do this yourself.


Installation
************

.. code-block:: bash

    pip install git+https://github.com/bmtcril/tutor-contrib-aspects-extension

Usage
*****

.. code-block:: bash

    tutor plugins enable aspects_extension
    tutor local|dev|k8s import-assets


After this you should have a new "Example Dashboard" in your Superset instance with one chart in it showing the most recent xAPI events.

License
*******

This software is licensed under the terms of the Apache 2.0.
