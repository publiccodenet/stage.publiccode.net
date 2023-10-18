#!/usr/bin/env bash

# This script is referenced by .github/workflows/test.yml which executes on
# each pull request.

# As part of reviewing a contribution, reviewers are responsible for checking
# that html is valid and conforms to the repository guidelines. This script is
# intended to aid in that process.

set -e # halt script on error

# if PAGES_REPO_NWO is not set then default to publiccodenet/process-code-software-procurement
# (jekyll defaults to "origin" if a remote of that name exists,
# which makes sense for a true fork, but not for most contributors)
if [ "_${PAGES_REPO_NWO}_" == "__" ]; then
export PAGES_REPO_NWO=publiccodenet/process-code-software-procurement
fi

# Build the site
bundle exec jekyll build

# Check for broken links and missing alt tags:
# jekyll does not require extentions like HTML
# deal with baseurl
# using the files in Jekylls build folder
bundle exec htmlproofer \
    --assume-extension \
    --disable-external \
    --url-swap '^/process-code-software-procurement[/]*:/' \
    ./_site
