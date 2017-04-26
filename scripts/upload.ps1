$current_directory = $pwd

cd $PSScriptRoot/..

# run "python setup.py register" if the project has not been register with pypi.python.org

python setup.py sdist upload

cd $current_directory

