"""Pylinting"""

import json, glob, subprocess, pytest

FILTER = "./**/.py"
PYTHON_FILES = glob.glob(FILTER, recursive=True)
@pytest.mark.parametrize('filepath', PYTHON_FILES)

def testpath(filepath):
    """
    Validates no pylint errors
    """

    # pylint: disable=consider-using-with
    proc = subprocess.Popen("pylint " + filepath + " -f json --persistent=n --score=y",
                            stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate

    lint_json = []
    if out and out.strip():
        lint_json = json.loads(out)
    
    assert len(lint_json) == 0
