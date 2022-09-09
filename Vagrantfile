
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "private_network", ip: "192.168.56.10"
  
  config.vm.provider "virtualbox" do |vb|
    vb.name = "python-project"
    config.vm.synced_folder "app/", "/home/vagrant/app/"
  end
  config.vm.provision "shell", path: "env/script.sh"
end
