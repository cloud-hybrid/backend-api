find "${PWD}" -name "*.pyc" -exec rm -f {} \;
find "${PWD}" -name "*.whl" -exec rm -f {} \;
find "${PWD}" -type f -name "*.py[co]" -exec rm -f {} \;
find "${PWD}" -type d -name "__pycache__" | xargs rm -rf

find "${PWD}" -name "*.DS_Store" -exec rm -f {} \;

rm -r -f "$(git rev-parse --show-toplevel)/Artifact/Build"
rm -r -f "$(git rev-parse --show-toplevel)/Artifact/Source"
rm -r -f "$(git rev-parse --show-toplevel)/Artifact/Distribution"

