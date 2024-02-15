# This script is meant to be run on a full project HTML/CSS export from a Figma project exported from Anima. Be sure to select 'Absolute Positioning' and 'PX' length unit in the HTML export settings, then 'Export Code' -> 'Full Project' -> 'Dowload ZIP' https://projects.animaapp.com/team/maxs-team-ocll7ag/project/HKtYnxM/screen/00-process-codes-landing-page/omniview?mode=code.

import os
import re

# files to move to match existing site structure
files_to_move = [
    (r'home-u40desktopu41-all-breakpoints.html', 'index.html'),
    (r'codebase-stewardship.html', '/codebase-stewardship/index.html'),
    (r'the-standard.html', '/standard-for-public-code/index.html'),
    (r'codebases-we-work-with.html', '/codebases/index.html'),
    (r'digital-omgevingsbeleid.html', '/codebases/omgevingsbeleid.html'),
    (r'who-we-are-1.html', '/who-we-are/index.html'),
    (r'who-we-are-2.html', '/who-we-are/index-2.html'),
    (r'background.html', '/background/index.html'),
]


# do string substitution for each pattern across all HTML files
directory = '.'

urlpatterns = [
# TODO: where should this go?
# (r"""https://about.publiccode.net/""", """https://staging.publiccode.net/our-mission"""),
(r"""https://projects.publiccode.net/""", """/resources-and-projects.html"""),
(r"""https://projects.publiccode.net""", """/resources-and-projects.html"""),
(r"""https://about.publiccode.net/CONTRIBUTING.html""", """/contributing.html"""),
(r"""https://publiccode.net/team/""", """/who-we-are/"""),
# Links open in current window
(r' target="_blank"', ''),
(r"""https://publiccode.net/""", """/"""),
(r"""https://publiccode.net""", """/"""),
(r"""<link rel="stylesheet" type="text/css" href="css/""", """<link rel="stylesheet" type="text/css" href="/css/"""),
(r'" src="img/', '" src="/img/'),
]

urlpatterns += files_to_move

patterns = [
(r"""    <!--<meta name=description content="This site was generated with Anima. www.animaapp.com"/>-->
    <!-- <link rel="shortcut icon" type=image/png href="https://animaproject.s3.amazonaws.com/home/favicon.png" /> -->
    <meta name="viewport" content="width=1440, maximum-scale=1.0" />
    <link rel="shortcut icon" type="image/png" href="https://animaproject.s3.amazonaws.com/home/favicon.png" />""","""    <meta name="viewport" content="width=1440, maximum-scale=1.0" />"""),
(r"""  </body>""","""    <script src="/collapsible.js"></script>
  </body>"""),
(r"""  </head>""", """
    <link rel="icon" href="https://brand.publiccode.net/logo/mark-128w128h.png">
    <script async defer data-domain="publiccode.net" src="https://plausible.io/js/plausible.js"></script>
  </head>"""),
]
patterns += urlpatterns

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

cssdirectory = './css/'
csspatterns = [
(r"""@import url\("https://px.animaapp.com/6406baa484a3afe9c63921de.6406baa605cc73851b593804.*.hcp.png"\);""", ''),
]
csspatterns += urlpatterns
# process css
for root, dirs, files in os.walk(cssdirectory):
    for file in files:
        if file.endswith('.css'):
            filepath = os.path.join(root, file)
            with open(filepath) as f:
                s = f.read()
                for pattern, replacement in csspatterns:
                    s = re.sub(pattern, replacement, s)
            with open(filepath, "w") as f:
                f.write(s)

# Move files around to match the existing site
for old_filename, new_filename in files_to_move:
    if new_filename[0] == '/':
        new_filename = new_filename[1:]
    newpath = os.path.dirname(new_filename)
    if newpath:
        os.makedirs(newpath, exist_ok=True)
    os.rename(old_filename, new_filename)