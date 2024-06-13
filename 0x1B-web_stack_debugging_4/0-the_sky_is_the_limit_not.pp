# increase the amount of traffic the nginx server can handle

# increase the ULIMIt of the default file
exec {'fix--for-nginx':
  # modify the ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # specify path cor the sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restart Nginx
exec { 'nginx-restart':
  # Restart nginx service
  command => '/etc/init.d/nginx restart',
  # Specify the path fir the init.d script
  path    => '/etc/init.d/',
}
