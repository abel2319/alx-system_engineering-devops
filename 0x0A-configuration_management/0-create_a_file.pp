# Using Puppet, create a file in /tmp. file name scholl, permission 0744, owner zzz-data, group www-data, content 'I love Puppet'

file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
