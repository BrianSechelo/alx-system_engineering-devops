#!/usr/bin/pup
# install a specific version of flask (2.1.0)
package {'flask':
	ensure   => '2.1.0',
	provider => 'pip'
}

