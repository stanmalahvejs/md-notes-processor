import pytest
import os
import subprocess


def get_test_image_tag():
    if "TEST_TAG" in os.environ:
        result = os.environ["TEST_TAG"]
    else:
        result = "stanmalahvejs/md-notes-processor:test"
    return result


def run_test_image(test_case):
    test_tag = get_test_image_tag()
    result = subprocess.run(
        [
            "docker",
            "run",
            "-v",
            "./image-tests/test-cases/" + test_case + ":/notes",
            test_tag,
            "/scripts/lint-notes.py",
        ],
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result


def test_lint_nodes_found_issues():
    # arrange

    # act
    result = run_test_image("linting-issues")

    # assert
    assert result.returncode == 1
    assert (
        result.stdout
        == """markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)
Finding: /notes/**/README.md
Linting: 1 file(s)
Summary: 3 error(s)
"""
    )
    assert (
        result.stderr
        == """notes/test-note/README.md:1:1 MD018/no-missing-space-atx No space after hash on atx style heading [Context: "#foobar"]
notes/test-note/README.md:1 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading [Context: "#foobar"]
notes/test-note/README.md:1:7 MD047/single-trailing-newline Files should end with a single newline character
"""
    )


def test_lint_nodes_no_issues():
    # arrange

    # act
    result = run_test_image("linting-ok")

    # assert
    assert result.returncode == 0
    assert (
        result.stdout
        == """markdownlint-cli2 v0.17.2 (markdownlint v0.37.4)
Finding: /notes/**/README.md
Linting: 1 file(s)
Summary: 0 error(s)
"""
    )
    assert result.stderr == ""
