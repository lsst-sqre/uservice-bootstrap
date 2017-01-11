#!/usr/bin/env python
def usage():
    print("Next steps (feel free to copy and paste the four-space-indented " +
          "lines):\n")
    print("    cd sqre-uservice-{{ cookiecutter.svc_name}}")
    print("    git init\n")
    print("  Create a Python 3 virtualenv from requirements.txt.")
    print("  (if virtualenvwrapper is installed, that's:\n")
    print("    mkvirtualenv -r requirements.txt -p $(which python3) " +
          "{{ cookiecutter.svc_name }}\n")
    print("  and if it isn't installed, that'll give you an error and you'll")
    print("  need to make a virtualenv the way you prefer.)\n")
    print("    python setup.py develop\n")
    print("  Add your service logic to " +
          "uservice_{{cookiecutter.svc_name}}/server.py.")
    print("  Get it working and tested.")
    print("  Tell SQuaRE it's ready for incorporation into api.lsst.codes.")

if __name__ == "__main__":
    usage()
