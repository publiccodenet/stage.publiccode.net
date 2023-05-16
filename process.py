# This script is meant to be run on a full project HTML/CSS export from a Figma project exported from Anima. Be sure to select 'Absolute Positioning' and 'PX' length unit in the HTML export settings, then 'Export Code' -> 'Full Project' -> 'Dowload ZIP' https://projects.animaapp.com/team/maxs-team-ocll7ag/project/HKtYnxM/screen/00-process-codes-landing-page/omniview?mode=code.

import os
import re

# Rename index file
old_filename = '00-process-codes-landing-page.html'
new_filename = 'index.html'

os.rename(old_filename, new_filename)

# do string substitution for each pattern across all HTML files
directory = '.'

patterns = [
(r"""    <!--<meta name=description content="This site was generated with Anima. www.animaapp.com"/>-->
    <!-- <link rel="shortcut icon" type=image/png href="https://animaproject.s3.amazonaws.com/home/favicon.png" /> -->
    <meta name="viewport" content="width=1440, maximum-scale=1.0" />
    <link rel="shortcut icon" type="image/png" href="https://animaproject.s3.amazonaws.com/home/favicon.png" />""", '    <meta name="viewport" content="width=1440, maximum-scale=1.0" />'),
]

for root, dirs, files in os.walk(directory):
  for file in files:
    if file.endswith('.html'):
      filepath = os.path.join(root, file)
      with open(filepath) as f:
        s = f.read()
        for pattern, replacement in patterns:
          s = re.sub(pattern, replacement, s)
      with open(filepath, "w") as f:
        f.write(s)