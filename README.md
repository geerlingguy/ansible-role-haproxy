# Ansible Role: HAProxy

[![CI](https://github.com/geerlingguy/ansible-role-haproxy/actions/workflows/ci.yml/badge.svg)](https://github.com/geerlingguy/ansible-role-haproxy/actions/workflows/ci.yml)

Installs HAProxy on RedHat/CentOS and Debian/Ubuntu Linux servers.

**Note**: This role _officially_ supports HAProxy versions 1.4 or 1.5. Future versions may require some rework.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
haproxy_socket: /var/lib/haproxy/stats
```

The socket through which HAProxy can communicate (for admin purposes or statistics). To disable/remove this directive, set `haproxy_socket: ''` (an empty string).

```yaml
haproxy_chroot: /var/lib/haproxy
```

The jail directory where chroot() will be performed before dropping privileges. To disable/remove this directive, set `haproxy_chroot: ''` (an empty string). Only change this if you know what you're doing!

```yaml
haproxy_user: haproxy
haproxy_group: haproxy
```

The user and group under which HAProxy should run. Only change this if you know what you're doing!

```yaml
haproxy_ca_base: /etc/ssl/certs
haproxy_crt_base: /etc/ssl/private
```

Assigns a default directory to fetch SSL CA certificates and SSL certificates.

```yaml
haproxy_default_log_format: ''
haproxy_default_options:
  - 'option  httplog'
  - 'option  dontlognull'
```

HAProxy default configuration directives.

```yaml
haproxy_frontend_name: 'hafrontend'
haproxy_frontend_bind_address: '*'
haproxy_frontend_port: 80
haproxy_frontend_mode: 'http'
```

HAProxy frontend configuration directives.

```yaml
haproxy_backend_name: 'habackend'
haproxy_backend_mode: 'http'
haproxy_backend_balance_method: 'roundrobin'
haproxy_backend_httpchk: 'HEAD / HTTP/1.1\r\nHost:localhost'
haproxy_backend_cookie_insert: true
haproxy_backend_default_server: ''
```

HAProxy backend configuration directives.

```yaml
haproxy_backend_servers:
  - name: app1
    address: 192.168.0.1:80
  - name: app2
    address: 192.168.0.2:80
```

A list of backend servers (name and address) to which HAProxy will distribute requests.

```yaml
haproxy_connect_timeout: 5000
haproxy_client_timeout: 50000
haproxy_server_timeout: 50000
```

HAProxy default timeout configurations.

```yaml
haproxy_prometheus_metrics: false
haproxy_prometheus_metrics_bind_address: '*'
haproxy_prometheus_metrics_port: 8405
haproxy_prometheus_metrics_path: /metrics
```

HAProxy prometheus-exporter configuration directives.

```yaml
haproxy_global_vars:
  - 'ssl-default-bind-ciphers ABCD+KLMJ:...'
  - 'ssl-default-bind-options no-sslv3'
```

A list of extra global variables to add to the global configuration section inside `haproxy.cfg`.

```yaml
haproxy_template: haproxy.cfg.j2
```

Use this variable to override the configuration template used by this role. Copy out the template file from this role's `templates` folder into your own playbook's `templates` folder to override.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: balancer
  sudo: yes
  roles:
    - { role: geerlingguy.haproxy }
```

## License

MIT / BSD

## Author Information

This role was created in 2015 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
