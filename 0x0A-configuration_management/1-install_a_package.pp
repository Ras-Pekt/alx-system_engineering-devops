# installs flask

file { 'Flask':
  ensure  => '2.1.0',
  provide => 'pip3',
}