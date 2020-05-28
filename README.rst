====================
SLU Project
====================

This is source code for slution project

**Table of contents**

.. contents::
   :local:

Required for this repository
============================

#. repository/repos.yaml
#. addons.yaml
#. custom-addons

Required git & python library
==============================

Git::

    apt-get install git

Git Aggregator::

    pip3 install git-aggregator
    
Click Odoo Conrib::

    pip3 install click-odoo-contrib

Usage
=====

#. Define branch/pr/commit need to merge code from github remote in file repository/repos.yaml
#. Define module need to install in file addons.yaml
#. Define git config (git config --global user.email "you@example.com" && git config --global user.name "Your Name")
#. Go to folder repository and type command "gitaggregate -c repos.yaml" for merge code (Check error if there are any error please fix it in repos.yaml and type command again)
#. All repository will store in folder repository (you can check it by type command "ls")
#. Out from folder repository and type commend "python3 addons-link.py" for selected some module from folder repository defined in addons.yaml (the system will generate folder auto-addons automatically and all selected addons will be in this)
#. Project specific module will be in folder custom-addons
#. In odoo.conf please specific addons_path with custom-addons and auto-addons
#. Restart odoo service
#. Check for module code changed by type command "click-odoo-update -c <config file path> -d <database name> --ignore-core-addons --list-only --logfile /var/log/odoo-update.log" after that see in /var/log/odoo-update.log you will see all module need to update without actually updating them
#. If you need to update all module code changed just type command "click-odoo-update -c <config file path> -d <database name> --ignore-core-addons --logfile /var/log/odoo-update.log" after that see in /var/log/odoo-update.log you will see log for updating module

Reference
=========

https://github.com/acsone/git-aggregator

https://github.com/acsone/click-odoo-contrib
