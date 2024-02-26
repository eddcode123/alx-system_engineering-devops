# create a file and with specified permission, owner and group
file { '/tmp/example.txt':
  ensure  => file,
  content => "I love Puppet.\n",
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
