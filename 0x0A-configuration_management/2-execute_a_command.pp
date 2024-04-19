# Execute a commad
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
  refreshonly => true,
  notify      => File['/path/to/triggering_file'],
}

