from starcluster.clustersetup import ClusterSetup
from starcluster.logger import log

class MASSInstaller(ClusterSetup):

	def __init__(self, username, password, version):
		log.debug("Username %s Password %s Version %s " % (username, password, version))
		self.username = username
		self.password = password
		self.version = version

	def run(self, nodes, master, user, user_shell, volumes):
		#install code
		log.debug("CLONING: git clone https://%s:%s@bitbucket.org/mass_library_developers/mass_cpp_core.git /home/MASS" % (self.username, self.password))
		master.ssh.execute("git clone https://%s:%s@bitbucket.org/mass_library_developers/mass_cpp_core.git /home/MASS" % (self.username, self.password))
		
		#construct machinefile
		master.ssh.execute("touch machinefile.txt")

		#skip the first node when constructing the machinefile	
		iternodes = iter(nodes)
		next(iternodes)
		for node in iternodes:
			master.ssh.execute("echo %s >> /home/machinefile.txt" % node.alias)
			log.info("Username: %s Password: %s" % (self.username, self.password))

		#update bash
		master.ssh.execute("echo \"export MASS_DIR=/home/MASS\" >> ~/.bashrc")
		master.ssh.execute("echo \"export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/MASS/ubuntu/ssh2/lib:/home/MASS/ubuntu\" >> ~/.bashrc")

		master.ssh.execute("echo \"function setup { \n ln -s /home/MASS/ubuntu/mprocess mprocess \n ln -s /home/MASS/ubuntu/killMProcess.sh killMProcess.sh}\" >> ~/.bashrc")
