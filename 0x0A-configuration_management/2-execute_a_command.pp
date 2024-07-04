# using puppet to create a manifest that kills a process named kllmenow.

exec { 'pkill killmenow':
    path => 'usr/bin:/usr/sbin:/bin',
}
