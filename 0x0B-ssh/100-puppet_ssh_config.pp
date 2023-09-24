# use puppet to change configuration file

file_line { 'passwd auth off':
	ensure => present,
	path   => '/etc/ssh/ssh_config',
	line   => 'PasswordAuthentication no',
	match  => '^#PasswordAuthentication',
}

file_line { 'declare private_key file':
	ensure => present,
	path   => '/etc/ssh/ssh_config',
	line   => 'IdentityFile ~/.ssh/school',
	match  => '^#IdentityFile',
}