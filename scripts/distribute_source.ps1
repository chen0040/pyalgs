$current_directory = $pwd

cd $PSScriptRoot/..
python setup.py sdist

cd $current_directory

