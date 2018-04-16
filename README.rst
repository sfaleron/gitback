Given a git repository that is shared with a mobile and at least one fixed device. Multiple remote devices are not supported at this time. Think "hub and spokes"

`gitback` is a system for permitting the git repository on the mobile/spoke device to access a git repository at a fixed/hub location, and for the repository on the fixed/hub device to access the repository on the mobile/spoke device, whether that device is on the local network or accessed remotely via the internet, by using port forwarding, rather than a clunky VPN.

The remote repositories have urls to local ports, which are forwarded as appropriate by ssh. When the mobile device is local to the fixed repository, an ssh session is opened from the fixed device to the mobile device, using gitback-f2m, and when the mobile device is being used away from the fixed device, a session is opened from the mobile device to the fixed device using gitback-m2f.

The intent is to piggyback the port forwarding onto ssh sessions that would probably be in use anyway.
