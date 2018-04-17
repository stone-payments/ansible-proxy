stone-payments.proxy
============
Role for Ansible which configures the proxy client parameters in RHEL systems

## Usage
Just include the role and set the variables in the `defaults/main.yml` file:
```yaml
- name: configure proxy client
  hosts: all
  roles:
    - stone-payments.proxy
  vars:
    proxy_address: "some.server.example.com"
    proxy_port: "3128"
```

## Advanced usage
You may also setup another proxy protocol than HTTP (SOCKS or SOCKS5, maybe)
and setup authentication by using the following vars:

```yaml
proxy_proto: "http" #may be http, socks or socks5
proxy_address: ""
proxy_port: ""
proxy_auth: false
proxy_user: ""
proxy_pass: ""
proxy_whitelist:
  - "127.0.0.1"
  - "localhost"
```

If you're going to use authentication, you need both to inform the user/pass
and enable it by setting `proxy_auth` to true.

You may also pass a list in `proxy_whitelist` of names or IPs that you do not
want to use the proxy and access directly.

## License
This code is licensed under the MIT license.
