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
- There are the following workflows:
    - Pull request workflow - builds the image locally, runs [Container image tests](#container-image-tests).
        - Inspired by [this example](https://docs.docker.com/build/ci/github-actions/test-before-push/).
    - `main` branch workflow - builds the multiplatform image, pushes to Dockerhub.
        - Inspired by [this example](https://docs.docker.com/build/ci/github-actions/multi-platform/).
