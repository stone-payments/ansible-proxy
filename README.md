# Stone Payments - Proxy

Role for Ansible which configures the proxy client parameters in GNU/Linux and Windows systems.

## Requirements

None.

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

You may also setup another proxy protocol than HTTP (SOCKS or SOCKS5, maybe) and setup authentication by using the following vars:

```yaml
# May be http, socks or socks5
proxy_proto: "http"
proxy_address: ""
proxy_port: ""

# To use proxy with authentication
proxy_auth: false
proxy_user: ""
proxy_pass: ""

# Configure yum and RHSM to use the proxy
proxy_redhat: false

# Used to set or remove proxy settings for Windows INet which includes Internet Explorer
proxy_win_inet: true

# Used to set, remove, or import proxy settings for Windows HTTP Services WinHTTP
proxy_win_http: false

# Sets the list of hosts that will bypass the set proxy when being accessed
proxy_whitelist:
  - "127.0.0.1"
  - "localhost"
```

- If you're going to use authentication, you need both to inform the user/pass and enable it by setting `proxy_auth` to true.
- You may also pass a list in `proxy_whitelist` with names or IPs that you do not want to use the proxy and access directly.

## Dependencies

None.

## Testing

This role to use [`molecule`](https://molecule.readthedocs.io/en/latest/) to execute your local tests and check ansible syntax. Notice that we only support Molecule 2.0 or greater. You can install molecule with:

```shell
pipenv install --dev --three
```

After having Molecule setup, you can run the tests with this steps:

```sh
molecule test [-s scenario_name]
```

Where `scenario_name` is the name of a test case under `molecule`.

## Contributing

Just open a PR. We love PRs!

## License

This code is licensed under the MIT license.
