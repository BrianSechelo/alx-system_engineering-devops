# Execute a commad
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  notify      => File['/path/to/triggering_file'],
}

