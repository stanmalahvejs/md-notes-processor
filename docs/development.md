# Development

Table of contents:

- [Development](#development)
    - [Testing](#testing)
        - [Container image tests](#container-image-tests)
    - [CI](#ci)

## Testing

### Container image tests

High level container image tests are in the folder `image-tests`. These tests run the actual image against the test notes folders, and check the exit codes, standard output, and error output.

## CI

- CI tool is GitHub Actions.
- There is a single build workflow, that is used on both PRs and main branch builds.
    - This workflow is inspired by these examples: [test before push](https://docs.docker.com/build/ci/github-actions/test-before-push/), [multi platform image](https://docs.docker.com/build/ci/github-actions/multi-platform/).
    - The first part of the workflow build an image locally and runs image E2E tests. These tests run a container from the image and check the output of the image.
    - The seconf part of the workflow pushed the image to the Dockerhub registry, and created the release.
        - The steps in this part should only run on main branch build. This is acheved by `if` condition.