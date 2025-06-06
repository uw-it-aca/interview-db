trap 'exit 1' ERR

#
# PRECONDITION: inherited env vars from application MUST include:
#      DJANGO_APP: django application directory name

# start virtualenv
source bin/activate

function run_test {
    echo "##########################"
    echo "TEST: $1"
    eval $1
}

#run_test "pycodestyle ${DJANGO_APP}/ --exclude=migrations,static"

if [ -d ${DJANGO_APP}/static/${DJANGO_APP}/js ]; then
    run_test "jshint ${DJANGO_APP}/static/${DJANGO_APP}/js --verbose"
elif [ -d ${DJANGO_APP}/static/js ]; then
    run_test "jshint ${DJANGO_APP}/static/js --verbose"
fi

run_test "python -Wd -m coverage run --source=${DJANGO_APP} '--omit=*/migrations/*' manage.py test ${DJANGO_APP}"

# put generated coverage result where it will get processed
cp .coverage.* /coverage

exit 0
