#Debug apache2 server using strace and tmux.
#Problem found, phpp extemsion instead of php


exec {'fix 500 server error':
	command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path     => '/usr/local/bin/:/bin/'
}
