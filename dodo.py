DOIT_CONFIG = { "project_name": "pyrecipes" }


def task_build():
    return \
    {
        "actions": ["pylint " + DOIT_CONFIG["project_name"]],
        "verbosity": 2
    }
