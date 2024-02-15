# This script is meant to be run on a full project HTML/CSS export from a Figma project exported from Anima. Be sure to select 'Absolute Positioning' and 'PX' length unit in the HTML export settings, then 'Export Code' -> 'Full Project' -> 'Dowload ZIP' https://projects.animaapp.com/team/maxs-team-ocll7ag/project/HKtYnxM/screen/00-process-codes-landing-page/omniview?mode=code.

import os
import re

# Rename index file
old_filename = 'home-u40desktopu41-all-breakpoints.html'
new_filename = 'index.html'

os.rename(old_filename, new_filename)


# do string substitution for each pattern across all HTML files
directory = '.'

patterns = [
(r"""    <!--<meta name=description content="This site was generated with Anima. www.animaapp.com"/>-->
    <!-- <link rel="shortcut icon" type=image/png href="https://animaproject.s3.amazonaws.com/home/favicon.png" /> -->
    <meta name="viewport" content="width=1440, maximum-scale=1.0" />
    <link rel="shortcut icon" type="image/png" href="https://animaproject.s3.amazonaws.com/home/favicon.png" />""","""    <meta name="viewport" content="width=1440, maximum-scale=1.0" />"""),
(r"""  </body>""","""     <script src="collapsible.js"></script>
  </body>"""),
# Donate buttons in header
(r"""            <a href="https://publiccode.net/codebase-stewardship/" target="_blank"
              ><div class="stewardship mulish-medium-black-14px">Stewardship</div> </a
            >""", """            <a href="https://secure.infinitegiving.com/gift/foundation-for-public-code" target="_blank"
              ><div class="stewardship mulish-medium-black-14px">Donate</div> </a
            >
            <a href="https://publiccode.net/codebase-stewardship/" target="_blank"
              ><div class="stewardship mulish-medium-black-14px">Stewardship</div> </a
            >"""),
(r"""              <a href="https://publiccode.net/codebase-stewardship/" target="_blank"
                ><div class="link-1 mulish-medium-black-16px">Stewardship</div> </a
              >""", """              <a href="https://secure.infinitegiving.com/gift/foundation-for-public-code" target="_blank"
                ><div class="link-1 mulish-medium-black-16px">Donate</div> </a
              >
              <a href="https://publiccode.net/codebase-stewardship/" target="_blank"
                ><div class="link-1 mulish-medium-black-16px">Stewardship</div> </a
              >"""),

(r"""home-u40desktopu41-all-breakpoints.html""", """index.html"""),
(r"""the agile development process. <br />You will continue running""", """the agile development process. <br /><br />You will continue running"""),
(r"""expectations?<br />Throughout this process, you also have the crucial responsibility of ensuring that""", """expectations?<br /><br />Throughout this process, you also have the crucial responsibility of ensuring that"""),
(r"""and expertise doesn’t disappear with individuals.<br />Your""", """and expertise doesn’t disappear with individuals.<br /><br />Your"""),
(r"""  </head>""", """
    <link rel="icon" href="https://brand.publiccode.net/logo/mark-128w128h.png">
    <script async defer data-domain="publiccode.net" src="https://plausible.io/js/plausible.js"></script>
  </head>"""),
#Design?

# TODO: where should this go?
# (r"""https://about.publiccode.net/""", """https://staging.publiccode.net/our-mission"""),
(r"""https://publiccode.net/codebase-stewardship/""", """https://staging.publiccode.net/codebase-stewardship.html"""),
(r"""https://projects.publiccode.net/""", """https://staging.publiccode.net/resources-and-projects.html"""),
(r"""https://projects.publiccode.net""", """https://staging.publiccode.net/resources-and-projects.html"""),
(r"""https://about.publiccode.net/CONTRIBUTING.html""", """https://staging.publiccode.net/contributing.html"""),
(r"""https://publiccode.net/standard-for-public-code/""", """https://staging.publiccode.net/the-standard.html"""),
#TODO: slightly different pages?
(r"""https://publiccode.net/who-we-are/""", """https://staging.publiccode.net/who-we-are-1.html"""),
(r"""https://publiccode.net/team/""", """https://staging.publiccode.net/who-we-are-1.html"""),
(r' target="_blank"', ''),
(r"""https://publiccode.net/""", """https://staging.publiccode.net/"""),
(r"""https://publiccode.net""", """https://staging.publiccode.net/"""),
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

cssdirectory = './css/'
csspatterns = [
(r"""@import url\("https://px.animaapp.com/6406baa484a3afe9c63921de.6406baa605cc73851b593804.*.hcp.png"\);""", ''),
(r"""home-u40desktopu41-all-breakpoints.html""", """index.html"""),
]
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