import os
import shutil
import subprocess
import sys


def main() -> None:
    mirror = "{{ cookiecutter.mirror_to_github }}"
    role_name = "{{ cookiecutter.role_name }}"
    git_user = "{{ cookiecutter.git_user }}"
    git_host = "{{ cookiecutter.git_host }}"

    include_mirror = mirror == "yes" and git_host == "git.sr.ht"

    builds_dir = os.path.join(os.getcwd(), ".builds")
    if not include_mirror and os.path.exists(builds_dir):
        shutil.rmtree(builds_dir)
        return

    if not include_mirror:
        return

    repo = "{}/{}".format(git_user, role_name)
    try:
        subprocess.run(
            ["gh", "repo", "create", repo, "--public"],
            check=True,
            capture_output=True,
            text=True,
            input="\n",
        )
        print("Created GitHub mirror: https://github.com/{}".format(repo))
    except subprocess.CalledProcessError as err:
        msg = err.stderr.strip() if err.stderr else str(err)
        print("Warning: could not create GitHub repo ({})".format(msg), file=sys.stderr)
    except FileNotFoundError:
        print(
            "Warning: gh CLI not found. Install it to auto-create GitHub mirrors.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
