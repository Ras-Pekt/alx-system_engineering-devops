# installs flask

package { 'Flask':
  ensure  => '2.1.0',
  provide => 'pip3',
}
