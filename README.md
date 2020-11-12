# Ansible Role: HAProxy

[![Build Status](https://travis-ci.org/justereseau/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/justereseau/ansible-role-haproxy)

Installs HAProxy on RedHat/CentOS and Debian/Ubuntu Linux servers, but Molecule say not. So RIP Molecule...

**Note**: This role _officially_ supports HAProxy versions 1.x and 2.x.

**Note 2**: We highly recommand to build your own `haproxy.cfg` by adapting it to your needs.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    haproxy_version: 2.2.5

The HAProxy version to install. If < 2.0.0, the latest 1.x.x availlable in the packet manager will be installed. If >=2.0.0, it will be built from HAProxy source.

    haproxy_socket: /var/lib/haproxy/stats

The socket through which HAProxy can communicate (for admin purposes or statistics). To disable/remove this directive, set `haproxy_socket: ''` (an empty string).

    haproxy_chroot: /var/lib/haproxy

The jail directory where chroot() will be performed before dropping privileges. To disable/remove this directive, set `haproxy_chroot: ''` (an empty string). Only change this if you know what you're doing!

    haproxy_user: haproxy
    haproxy_group: haproxy

The user and group under which HAProxy should run. Only change this if you know what you're doing!

    haproxy_frontend_name: 'hafrontend'
    haproxy_frontend_bind_address: '*'
    haproxy_frontend_port: 80
    haproxy_frontend_mode: 'http'

HAProxy frontend configuration directives.

    haproxy_backend_name: 'habackend'
    haproxy_backend_mode: 'http'
    haproxy_backend_balance_method: 'roundrobin'
    haproxy_backend_httpchk: 'HEAD / HTTP/1.1\r\nHost:localhost'

HAProxy backend configuration directives.

    haproxy_backend_servers:
      - name: app1
        address: 192.168.0.1:80
      - name: app2
        address: 192.168.0.2:80

A list of backend servers (name and address) to which HAProxy will distribute requests.

    haproxy_global_vars:
      - 'ssl-default-bind-ciphers ABCD+KLMJ:...'
      - 'ssl-default-bind-options no-sslv3'

A list of extra global variables to add to the global configuration section inside `haproxy.cfg`.

    haproxy_custom_config_template: 'haproxy.cfg.j2'

Specify your own `haproxy.cfg` template file.

## Dependencies

None.

## Example Playbook

    - hosts: balancer
      sudo: yes
      roles:
        - { role: geerlingguy.haproxy }

## License

MIT / BSD

## Author Information

This role was a fork of the one created in 2015 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).

This role was edited by [Lucas Maurice (Sonic)](lmaurice@justereseau.ca), member of [JusteReseau](https://justereseau.ca/)
