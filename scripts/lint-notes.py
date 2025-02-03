import subprocess
import sys

result = subprocess.run(['markdownlint-cli2', '/notes/**/README.md'])
sys.exit(result.returncode)