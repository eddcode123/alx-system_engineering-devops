# Creates a file in /tmp with specified permission, owner and group
file { '/tmp/school':
  ensure  => file,
  content => "I love Puppet.\n",
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
