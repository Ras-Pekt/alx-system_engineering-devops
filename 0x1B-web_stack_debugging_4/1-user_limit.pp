# fix soft and hard user limits

exec { 'hard_limit':
  command => '/bin/sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf',
}

exec { 'soft_limit':
  command => '/bin/sed -i "s/holberton soft nofile 4/holberton soft nofile 5000/" /etc/security/limits.conf',
}
