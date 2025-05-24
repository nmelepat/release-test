# Release Please Monorepo Example

Welcome to the **Release Please Monorepo Example** repository! 
This repository showcase the usage of **release-please** in a monorepo setup.

## Overview

This example demonstrates how to automate versioning and changelog generation for multiple packages within a single repository using **release-please**. 

## Project Structure

This repository includes the following projects:

1. **Python Project**: Two Hello World python project  

## Key Files

- **[.release-please-manifest.json](.release-please-manifest.json)** - This file contains the version declarations for the packages in the repository.
- **[release-please-config.json](release-please-config.json)** - Configuration for release please.
- **[release-please.yml](.github%2Fworkflows%2Frelease-please.yml)** - GitHub workflow that triggers the automated release process. This action relies on the **.release-please-manifest.json** and **release-please-config.json** files.

If you're configuring release please for your project, check out [different strategy types](https://github.com/googleapis/release-please?tab=readme-ov-file#strategy-language-types-supported) for handling releases.
In this project `python` is used. 

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.