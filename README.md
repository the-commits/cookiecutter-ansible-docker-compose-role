# cookiecutter-ansible-docker-compose-role

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for
scaffolding Ansible roles that deploy Docker Compose stacks, with built-in
resource limits.

## Usage

```bash
pip install cookiecutter
cookiecutter git@git.sr.ht:~the-commits/cookiecutter-ansible-docker-compose-role
```

You'll be prompted for:

| Prompt | Default | Description |
|---|---|---|
| `role_name` | `my_docker_compose_stack` | Role name (snake_case) |
| `role_short_description` | `Deploy My Docker Compose Stack` | Short display title |
| `namespace` | `tjenamors` | Galaxy namespace |
| `author` | `the-commits` | Maintainer name |
| `description` | `An Ansible role to deploy ...` | Description |
| `docker_image` | `example/app:latest` | Default Docker image |
| `container_name` | *(role_name)* | Default container name |
| `default_memory_mb` | `512` | Max memory for container |
| `default_cpus` | `1` | Max vCPU count |
| `min_ansible_version` | `2.14` | Minimum Ansible |
| `git_host` | `git.sr.ht` | Git hosting domain |
| `git_user` | *(author)* | User/org on git host |
| `license` | `AGPL-3.0` | License type |
| `create_molecule` | `yes` | Scaffold molecule tests |
| `mirror_to_github` | `yes` | Auto-create public GitHub mirror |
| `secret_uuid` | `e3464eed-...` | Sourcehut secret UUID for GitHub mirror auth |

When `mirror_to_github` is `yes`, the template generates a `.builds/push.yml`
for automated GitHub mirroring and runs `gh repo create --public` to set up
the mirror repo.

## Output

```
my_docker_compose_stack/
├── .builds/          # GitHub mirror build manifest (if mirror_to_github)
├── .github/          # Issue/PR redirects to sourcehut
├── defaults/        # Resource limits + deploy dir
├── handlers/        # Docker Compose restart handler
├── meta/            # Galaxy metadata + docker deps
├── tasks/           # Compose deploy + container lifecycle
├── templates/
│   └── docker-compose.yml.j2  # Compose file with deploy.resources
├── molecule/default/
├── galaxy.yml
├── AGENTS.md
├── CONTRIBUTING.md   # Points contributors to sourcehut
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Resource Limits

The generated `docker-compose.yml.j2` uses Docker Compose
`deploy.resources` to constrain containers:

| Variable | Default | Description |
|---|---|---|
| `{{ role_name }}_memory_max` | `512m` | Hard memory limit |
| `{{ role_name }}_memory_reservation` | `256m` | Soft memory reservation |
| `{{ role_name }}_cpus_max` | `1` | Hard CPU limit |
| `{{ role_name }}_cpus_reservation` | `0.5` | Soft CPU reservation |

Override at playbook level:

```yaml
vars:
  my_role_memory_max: 1024m
  my_role_cpus_max: "2"
```

## Related Templates

- **`cookiecutter-ansible-role`** — for standalone roles (system config, SSH, packages).
  Use this when your role does NOT deploy Docker Compose stacks.
- **`cookiecutter-ansible-docker-compose-role`** (this repo) — for Docker Compose stack roles.

## Requirements

- Python 3.8+
- [cookiecutter](https://cookiecutter.readthedocs.io/) (`pip install cookiecutter`)
- Molecule + vagrant-libvirt (for testing generated roles)
