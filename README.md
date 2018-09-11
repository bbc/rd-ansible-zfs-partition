rd-ansible-zfs-partition [![Build Status](https://travis-ci.org/bbc/rd-ansible-zfs-partition.svg?branch=master)](https://travis-ci.org/bbc/rd-ansible-zfs-partition)
=========

This role creates and manages ZFS Zpools, it exits if anything already exists in the way of LVM, MDADM or partitions on the disks.
It also allows for specifying ZFS Raid type, options and spare disks

Requirements
------------

This role requires Ansible 2.6 or greater

Role Variables
--------------

See defaults for variables and descriptions

Dependencies
------------

This role has no dependencies

Example Playbook
----------------

Example to call:

    - hosts: all
      roles:
         - { role: rd-ansible-zfs-partition }
