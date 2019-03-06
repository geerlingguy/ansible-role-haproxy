# Ansible Role: HAProxy

[![Build Status](https://travis-ci.org/socketwench/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/socketwench/ansible-role-haproxy)

A fork of [geerlingguy.haproxy](https://galaxy.ansible.com/geerlingguy/haproxy), this role installs HAProxy on RedHat/CentOS and Debian/Ubuntu Linux servers. This fork supports multiple frontends, backends, and TLS.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

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
        address: 192.168.0.1
        port: 80
      - name: app2
        address: 192.168.0.2
        port: 80

A list of backend servers (name and address) to which HAProxy will distribute requests.

    haproxy_global_vars:
      - 'ssl-default-bind-ciphers ABCD+KLMJ:...'
      - 'ssl-default-bind-options no-sslv3'

A list of default options to use.

    haproxy_default_options:
      - 'httplog'
      - 'dontlognull'

### Specifying multiple frontends

This role can also specify multiple frontends using the `haproxy_frontends` variable:

    haproxy_frontends:
      - name: 'hafrontend'
        bind_address: '*'
        bind_port: '80'
        mode: 'http'
        backend_name: 'habackend'
        vars:
          - 'reqadd X-Forwarded-Proto:\ http'
      - name: 'hafrontend_ssl'
        mode: 'http'
        bind_address: '*'
        bind_port: '443'
        bind_cert_path: '/path/to/my/cert.pem'
        backend_name: 'habackend'
        vars:
          - 'acl letsencrypt-acl path_beg /.well-known/acme-challenge/'
          - 'reqadd X-Forwarded-Proto:\ https'
          - 'use_backend letsencrypt-backend if letsencrypt-acl'

When using `haproxy_frontends` all `haproxy_frontend_*` variables are ignored.

### Specifying multiple backends

Likewise, you can also specify multiple backends using `haproxy_backends`:

    haproxy_backends:
      - name: 'habackend'
        mode: 'http'
        servers:
          - name: 'app1'
            address: '123.123.123.123'
            port: '80'
            params:
              - 'cookie'
              - 'app1'
              - 'check'
      - name: 'letsencrypt-backend'
        servers:
          - name: 'letsencrypt'
            address: '127.0.0.1'
            port: '54321'  

When using `haproxy_backends` all `haproxy_backend_*` variables are ignored.

### Other variables

A list of extra global variables to add to the global configuration section inside `haproxy.cfg`.

## Dependencies

None.

## Example Playbook

    - hosts: balancer
      sudo: yes
      roles:
        - { role: socketwench.haproxy }

## License

MIT / BSD

## Author Information

This role was originally created in 2015 by [Jeff Geerling](https://www.jeffgeerling.com/), and forked by [socketwench](https://deninet.com/).
