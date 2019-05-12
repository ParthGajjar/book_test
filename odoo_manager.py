from subprocess import Popen


def kill_odoo():
    with open('odoo.pid', 'r') as f:
        try:
            pid = f.read()
            pid = pid.strip()
            Popen(['/bin/kill', '-9', pid], shell=False)
        except Exception as e:
            print("ERROR: ", e)
    with open('running_recipe', 'r+') as f:
        f.truncate(0)


def get_running_recipe():
    name = ""
    with open('running_recipe', 'r') as f:
        name = f.read()
    return name


def run_odoo(path):
    kill_odoo()
    command = [
            "/usr/local/bin/python3",
            "/Users/pga/odoo/community/odoo-bin",
            "--addons=/Users/pga/odoo/community/addons,%s" % path,
            "--database=%s" % 'test-12',
            "--db-filter=%s" % 'test-12',
            "--init=%s" % 'my_library,my_module',
            "--dev=all"
        ]
    odoo_process = Popen(command, shell=False)
    with open('running_recipe', 'w') as f:
        f.write(path)
    with open('odoo.pid', 'w') as f:
        f.write(str(odoo_process.pid))

