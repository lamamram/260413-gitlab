## Toute commande doit-ere exécution dans le répertoire contenant le Vagrantfile
## UP / DOWN
# vagrant up : lance TOUT
# vagrant up <hostname>: lance hostname
# vagrant halt [<hostname>]: arête tout ou seulement hostname
# vagrant destroy [-f] [<hostname>] : détruit [-f sans confirmation] //
# vagrant reload [<hostname>]: halt && up
## CNX
# vagrant ssh [<hostname>]: connexion SSH sur le compte "vagrant" 
#                           via l'interface NAT (127.0.0.1 + redirection 2222 <=> 22)
# vagrant ssh-config: configuration du vagrant ssh
# vagrant global-config
##------------------------------------------------------------------

Vagrant.configure(2) do |config|

  ## VARS

  subject  = "gitlab"
  hostname = "#{subject}.lan.fr"
  image    = "ml-registry/#{subject}"
  memory   = 10000
  cpus     = 4

  # Configuration réseau "Bridge public"
  # interface réseau à utiliser: ipconfig /all (Windows) | ip a (Linux)
  # Windows: Get-NetAdapter | Where-Object {$_.Status -eq "Up"} | Select-Object -ExpandProperty InterfaceDescription
  # ip disponible pour la VM dans l'interface ci-dessus: ping | nslookup
  # CIDR: masque de sous réseau 24 <==> 255.255.255
  # interface = "Intel(R) Ethernet Connection (7) I219-V"
  # ip        = "192.168.1.140"
  # cidr      = "24"

  ## MAIN
  
  config.vm.define "#{hostname}" do |machine|
    machine.vm.provider "virtualbox" do |v|
      v.memory = "#{memory}"
      v.cpus = "#{cpus}"
      v.name = "#{hostname}"
      v.customize ["modifyvm", :id, "--ioapic", "on"]
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      ## configuration réseau NAT
      v.customize ["modifyvm", :id, "--natpf1", "https,tcp,127.0.0.1,8443,,443"]
      v.customize ["modifyvm", :id, "--natpf1", "http,tcp,127.0.0.1,8025,,8025"]
      v.customize ["modifyvm", :id, "--natpf1", "sonar,tcp,127.0.0.1,9000,,9000"]
    end
    machine.vm.box = "#{image}"
    machine.vm.hostname = "#{hostname}"
    # configuration réseau bridge
    # machine.vm.network "public_network",
    #   bridge: "#{interface}",
    #   ip: "#{ip}",
    #   netmask: "#{cidr}"
    machine.ssh.insert_key = false

  end
end
