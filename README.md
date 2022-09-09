# python-vagrant-project

Welcome to my Vagrant Python Project.

This Vagrant file will allow you to spin up a Virtual Machine and play my adventure-game.py.

To run this virtual machine you will need to have Vagrant installed and have Virtual Box installed.

If you have a Mac with a M1 or M2 chip you will need Vagrant and VMware installed.

If you are using a Mac M1, in the Vagrantfile, you need to comment out the Virtutal Box configuration and un-comment the VMware configuration. As of now the Vagrantfile is configured to run on Windows computers and Mac's with the Intel chip.

1. you will need to clone this repo and then in the terminal open directory where repo lives.
2. type vagrant up & press enter.
3. type vagrant ssh & press enter
4. cd into app & press enter.
5. type python3 adventure-game.py & press enter.

enjoy
