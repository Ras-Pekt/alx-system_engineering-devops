# installs flask

file { 'flask':
  ensure  => '2.1.0',
  provide => 'pip3',
}