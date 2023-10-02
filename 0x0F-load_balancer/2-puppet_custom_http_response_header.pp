# manifest file to configure a brand new ubuntu machine

exec { 'update':
	command  => 'sudo apt-get update',
	provider => shell
}

package { 'nginx':
	ensure  => installed,
	require => Exec['update']
}

exec { 'add_header':
	command => 'sudo sed -i "/server_name _;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;'
	require => Package['nginx']
}

exec { 'nginx_reload':
	command => 'sudo service nginx reload',
	require => Package['nginx']
}
