#!/bin/bash
set -ex

function create_venv {
  python3 -m venv $1
  source $1/bin/activate
  pip install --upgrade pip
  pip install \
  --index-url 'http://nexus.wdf.sap.corp:8081/nexus/content/groups/build.milestones.pypi/simple/' \
  --trusted-host=nexus.wdf.sap.corp \
  -r requirements.txt \
  --ignore-installed

  # install Centaur wheel package which is contained in centaur base image
  pip install /opt/centaur/centaur-*-py3-none-any.whl
  deactivate
}

mkdir -p /venvs
create_venv /venvs/churn
