# {{ cookiecutter.role_short_description }}

{{ cookiecutter.description }}

## Requirements

- Ansible {{ cookiecutter.min_ansible_version }}+
- Root/sudo access on target hosts
- Linux (x86_64 or aarch64)
- Docker Engine and Docker Compose installed on target hosts
- Minimum server resources:
  - 512 MB RAM
  - 1 vCPU
  - 10 GB disk space

## Installation

### From Ansible Galaxy (once published)

```bash
ansible-galaxy install {{ cookiecutter.namespace }}.{{ cookiecutter.role_name }}
```

### From source

Add to your `requirements.yml`:

```yaml
---
roles:
  - name: {{ cookiecutter.role_name }}
    src: git@{{ cookiecutter.git_host }}:{{ cookiecutter.git_user }}/{{ cookiecutter.role_name }}
    scm: git
    version: main
```

Then install:

```bash
ansible-galaxy install -r requirements.yml -p roles/
```

## Role Variables

All variables are prefixed with `{{ cookiecutter.role_name }}_`. See [`defaults/main.yml`](defaults/main.yml) for the full list.

| Variable | Default | Description |
|---|---|---|
| `{{ cookiecutter.role_name }}_base_dir` | `/opt/{{ cookiecutter.role_name }}` | Installation directory |
| `{{ cookiecutter.role_name }}_image` | `{{ cookiecutter.docker_image }}` | Docker image to use |
| `{{ cookiecutter.role_name }}_container_name` | `{{ cookiecutter.container_name }}` | Container name |
| `{{ cookiecutter.role_name }}_docker_network` | `{{ cookiecutter.role_name }}` | Docker network name |
| `{{ cookiecutter.role_name }}_memory_max` | `{{ cookiecutter.default_memory_mb }}m` | Max memory for container |
| `{{ cookiecutter.role_name }}_memory_reservation` | `{{ cookiecutter.default_memory_mb // 2 }}m` | Memory reservation |
| `{{ cookiecutter.role_name }}_cpus_max` | `{{ cookiecutter.default_cpus }}` | Max CPU count |
| `{{ cookiecutter.role_name }}_cpus_reservation` | `{{ (cookiecutter.default_cpus | float / 2) | round(1) }}` | CPU reservation |

## Dependencies

Requires Docker Engine and Docker Compose. See
[`tjenamors-se-docker`](https://git.sr.ht/~the-commits/tjenamors-se-docker) and
[`tjenamors-se-docker-compose`](https://git.sr.ht/~the-commits/tjenamors-se-docker-compose).

## Example Playbook

```yaml
- hosts: all
  become: true
  vars:
    {{ cookiecutter.role_name }}_base_dir: /opt/{{ cookiecutter.role_name }}
  roles:
    - role: docker
    - role: docker_compose
    - role: {{ cookiecutter.role_name }}
```

## Resource Limits

By default, containers are limited to {{ cookiecutter.default_memory_mb }} MB RAM and {{ cookiecutter.default_cpus }} vCPU.
Adjust via role variables:

```yaml
{{ cookiecutter.role_name }}_memory_max: 1024m
{{ cookiecutter.role_name }}_cpus_max: "2"
```

## Service Management (systemd)

On systemd-based distros, manage the service like any other:

```bash
sudo systemctl status {{ cookiecutter.role_name }}
sudo systemctl start {{ cookiecutter.role_name }}
sudo systemctl stop {{ cookiecutter.role_name }}
sudo systemctl restart {{ cookiecutter.role_name }}
sudo journalctl -u {{ cookiecutter.role_name }}
```

## Local Development

### Prerequisites

```bash
pip install molecule molecule-plugins[vagrant]
vagrant plugin install vagrant-libvirt
```

### Running Tests

```bash
molecule test
```

## License

{{ cookiecutter.license }} — see [LICENSE](LICENSE) for details.
