stone-payments.proxy
====================
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

You may also pass a list in `proxy_whitelist` with names or IPs that you do not
want to use the proxy and access directly.

## Testing
This role implements unit tests with [Molecule](https://molecule.readthedocs.io/) on Vagrant for Windows tests. Notice
that we only support Molecule 2.0 or greater. You can install Molecule inside a virtual environment with the following
command:
```sh
virtualenv .venv
.venv/bin/activate
pip install molecule
```
You can install Vagrant with your distro package-manager (out of scope), but you will also need some plugins to
interact with Windows trough the WinRM interface:
```sh
vagrant plugin install winrm{,-fs,-elevated}
```

After having Molecule setup within the virtualenv, you can run the tests with:
```sh
molecule converge [-s scenario_name]
```
Where `scenario_name` is the name of a test case under `molecule`. The test case for Windows is `windows`.

## Contributing
Just open a PR. We love PRs!

## License
This code is licensed under the MIT license.
