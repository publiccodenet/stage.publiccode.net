#!/usr/bin/env bash

# This script is referenced by .github/workflows/link-check.yml which executes
# executes daily.

# Failures reported by this script are addressed on a case-by-case basis.

set -e # halt script on error

# if PAGES_REPO_NWO is not set then default to publiccodenet/process-code-software-procurement
# (jekyll defaults to "origin" if a remote of that name exists,
# which makes sense for a true fork, but not for most contributors)
if [ "_${PAGES_REPO_NWO}_" == "__" ]; then
export PAGES_REPO_NWO=publiccodenet/process-code-software-procurement
fi

# Build the site
bundle exec jekyll build

# bundle exec htmlproofer --help | grep url-ignore
#  --url-ignore link1,[link2,...]  A comma-separated list of
#    Strings or RegExps containing URLs that are safe to ignore.
# * github.com/foo/edit/ : may reference yet-to-exist pages
# * docs.github.com/en : blocked by github DDoS protection
# * plausible.io/js/plausible.js : does not serve to scripts
# * belastingdienst.nl : regularly cries wolf with request timed out
# * www.bidnet.com : regularly cries wolf with request timed out
# * web.archive.org : sometimes too slow and fails from link check
URL_IGNORE_REGEXES="\
/github\.com\/.*\/edit\//\
,/docs\.github\.com\/en\//\
,/plausible\.io\/js\/plausible\.js/\
,/code\.gov\/agency-compliance\/compliance\/procurement/\
,/belastingdienst\.nl\/wps\/wcm\/connect\/bldcontenten\/belastingdienst\//\
,/www\.bidnet\.com\//\
,/www\.archive\.org\//\
"

# Check for broken links and missing alt tags:
# jekyll does not require extentions like HTML
# ignoring problem urls (see above)
# set an extra long timout for test-servers with poor connectivity
# ignore request rate limit errors (HTTP 429)
# deal with baseurl
# using the files in Jekylls build folder
bundle exec htmlproofer \
    --assume-extension \
    --url-ignore $URL_IGNORE_REGEXES \
    --typhoeus-config '{"timeout":60,"ssl_verifypeer":false,"ssl_verifyhost":"0"}' \
    --http_status_ignore "429" \
    --url-swap '^/process-code-software-procurement[/]*:/' \
    ./_site
