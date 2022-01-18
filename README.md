# Ansible Role: HAProxy

[![CI](https://github.com/geerlingguy/ansible-role-haproxy/workflows/CI/badge.svg?event=push)](https://github.com/geerlingguy/ansible-role-haproxy/actions?query=workflow%3ACI)

Installs HAProxy on RedHat/CentOS and Debian/Ubuntu Linux servers.

**Note**: This role _officially_ supports HAProxy versions 1.4 - 2.2. Future versions may require some rework.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see [defaults/main.yml](defaults/main.yml)):

    haproxy_socket: /var/lib/haproxy/stats
    haproxy_socket_level: admin
    haproxy_socket_params: ''

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
    haproxy_frontend_options: []

HAProxy frontend configuration directives.

    haproxy_backend_name: 'habackend'
    haproxy_backend_mode: 'http'
    haproxy_backend_balance_method: 'roundrobin'
    haproxy_backend_httpchk: 'HEAD / HTTP/1.1\r\nHost:localhost'
    haproxy_backend_options:
      - cookie SERVERID insert indirect
      - option forwardfor

HAProxy backend configuration directives.

    haproxy_backend_servers:
      - name: app1
        address: 192.168.0.1:80
        # params: defaults to 'cookie {{name}} check' if haproxy_backend_mode == 'http' for backward compatibility
      - name: app2
        address: 192.168.0.2:80
        params: maxconn 32 check

A list of backend servers (name and address) to which HAProxy will distribute requests.

    haproxy_defaults:
      - log global
      - mode http
      - option httplog
      - option dontlognull

HAProxy default settings.

    haproxy_connect_timeout: 5000
    haproxy_client_timeout: 50000
    haproxy_server_timeout: 50000

HAProxy default timeout configurations.

    haproxy_log:
      - "/dev/log  local0"
      - "/dev/log  local1 notice"

HAProxy global log directives.

    haproxy_global_vars:
      - 'ssl-default-bind-ciphers ABCD+KLMJ:...'
      - 'ssl-default-bind-options no-sslv3'

A list of extra global variables to add to the global configuration section inside `haproxy.cfg`.

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

This role was created in 2015 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
