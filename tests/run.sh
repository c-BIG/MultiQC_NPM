#!/bin/bash


# make sure we are in the test directory
ls ../setup.py ../tests  >& /dev/null || { echo "ERROR: must run from MultiQC_NPM/tests directory"; exit 1; }


# define directories
projectdir=$(realpath "$(pwd)/..")
testdir="$1"
if [ -z "$testdir" ]; then
    echo "ERROR: Missing testdir argument, e.g.:" 1>&2
    echo "  testdir='/data/13000026/pipeline/dev/NPM-sample-qc/tests/<my_run>'" 1>&2
    echo "  ./run.sh \$testdir"
    exit 1
fi


# update installation
cd ${projectdir}
python setup.py clean
python setup.py develop
cd ${projectdir}/tests


# run tests
CMD="multiqc ${projectdir}/tests/test_data/test1 -o ${testdir} --force"
echo "# Running test: ${CMD}"; ${CMD}

CMD="multiqc ${projectdir}/tests/test_data/test1 -o ${testdir} --force --enable-npm-plugin"
echo "# Running test: ${CMD}"; ${CMD}

CMD="multiqc ${projectdir}/tests/test_data/test2 -o ${testdir} --force --enable-npm-plugin"
echo "# Running test: ${CMD}"; ${CMD}
