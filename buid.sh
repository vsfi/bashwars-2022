#!/usr/bin/env bash


TASKS=$(jq -r '.[] | .name' tasks.json)

REPO_URL="registry.vsfi.org/bashwars"
for task in ${TASKS}
do
    echo "#### Processing ${task}"

    TASK_PATH=$(jq -r --arg task ${task} '.[] | select(.name | contains($task)) | .path' tasks.json)

    echo $TASK_PATH
    pushd ${TASK_PATH}
    docker build -t ${REPO_URL}/${task}:latest .
    docker push ${REPO_URL}/${task}:latest 
    popd
done
