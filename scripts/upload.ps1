$current_directory = $pwd

cd $PSScriptRoot/..
python setup.py sdist upload

cd $current_directory

