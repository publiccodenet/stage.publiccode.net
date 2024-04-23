# This script is meant to be run on a full project HTML/CSS export from a Figma project exported from Anima. Be sure to select 'Absolute Positioning' and 'PX' length unit in the HTML export settings, then 'Export Code' -> 'Full Project' -> 'Dowload ZIP' https://projects.animaapp.com/team/maxs-team-ocll7ag/project/HKtYnxM/screen/00-process-codes-landing-page/omniview?mode=code.

import os
import re


# do regex substitution for each pattern across files with the specified ending in specified path
def updateFiles(patterns, path='.', ending='.html'):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(ending):
                filepath = os.path.join(root, file)
                with open(filepath) as f:
                    s = f.read()
                    for pattern, replacement in patterns:
                        s = re.sub(pattern, replacement, s)
                with open(filepath, "w") as f:
                    f.write(s)


# files to move to match existing site structure
files_to_move = [
    (r'home-u40desktopu41-ne.html', 'index.html'),
    (r'product-model-u40desktopu41-ne.html', 'product-model.html'),
    (r'the-standard-u40desktopu41-ne.html', '/standard-for-public-code/index.html'),
    (r'about-public-code-u40desktopu41-ne.html', 'about.html'),
    (r'who-we-are-u43-background-u40desktopu41-ne.html', '/who-we-are/index.html'),
    # (r'who-we-are-2.html', '/who-we-are/index-2.html'),
    # (r'background.html', '/background/index.html'),
]

# URLs to replace
urlpatterns = [
# (r'digital-omgevingsbeleid.html', '/codebases/omgevingsbeleidhtml'),
# (r"""https://projects.publiccode.net/""", """/resources-and-projects.html"""),
# (r"""https://projects.publiccode.net""", """/resources-and-projects.html"""),
# (r"""https://about.publiccode.net/CONTRIBUTING.html""", """/contributing.html"""),
# (r"""https://publiccode.net/team/""", """/who-we-are/"""),
# Links open in current window
(r' target="_blank"', ''),
(r"""https://publiccode.net/""", """/"""),
(r"""https://publiccode.net""", """/"""),
]

urlpatterns += files_to_move

# HTML to replace
html_patterns = [
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
(r"""<link rel="stylesheet" type="text/css" href="css/""", """<link rel="stylesheet" type="text/css" href="/css/"""),
(r'" src="img/', '" src="/img/'),
# contact us form
(r"""<div class="frame-211 frame">
          <div class="contact-form contact-1 mulish-bold-black-32px">Contact form</div>
          <p class="lets-quickly-see-ho mulish-normal-black-20px">
            Let’s quickly see how the Foundation for Public Code can help you achieve your goals. If you can provide us
            a few initial details, we’ll respond with questions, ideas and next steps.
          </p>
          <div class="frame-239 frame">
            <div class="frame-232 frame">
              <article class="uiformtextfieldsingle">
                <div class="label mulish-normal-black-16px">Your name</div>
                <div class="uitextfieldsingle">
                  <div class="field-text mulish-normal-mine-shaft-20px">Add your name</div>
                </div>
              </article>
              <article class="uiformtextfieldsingle">
                <div class="label-1 label-8 mulish-normal-black-16px">Email address</div>
                <div class="uitextfieldsingle">
                  <div class="field-text mulish-normal-mine-shaft-20px">Add your email address</div>
                </div>
              </article>
              <article class="uiformtextfieldsingle">
                <div class="label-2 label-8 mulish-normal-black-16px">Organization</div>
                <div class="uitextfieldsingle">
                  <div class="field-text mulish-normal-mine-shaft-20px">Add your organization</div>
                </div>
              </article>
              <article class="uiformtextfieldsingle">
                <div class="label-3 label-8 mulish-normal-black-16px">Location</div>
                <div class="uitextfieldsingle">
                  <div class="field-text mulish-normal-mine-shaft-20px">Add your location</div>
                </div>
              </article>
            </div>
            <div class="frame-238 frame">
              <article class="uiformradio">
                <div class="label-4 label-8 mulish-normal-black-16px">Organization type</div>
                <div class="cluster">
                  <div class="option">
                    <div class="uiradio"></div>
                    <div class="selection mulish-normal-black-14px">Public/Governmental</div>
                  </div>
                  <div class="option-7">
                    <div class="uiradio"></div>
                    <div class="selection-7 mulish-normal-black-14px">Private/Corporation</div>
                  </div>
                  <div class="option-7">
                    <div class="uiradio"></div>
                    <div class="selection-7 mulish-normal-black-14px">Other</div>
                  </div>
                </div>
              </article>
              <article class="uiformradio-1">
                <div class="label-5 label-8 mulish-normal-black-16px">Project stage</div>
                <div class="cluster">
                  <div class="option-7">
                    <div class="uiradio"></div>
                    <div class="selection-7 mulish-normal-black-14px">Just starting</div>
                  </div>
                  <div class="option-7">
                    <div class="uiradio"></div>
                    <div class="selection-7 mulish-normal-black-14px">Procurement</div>
                  </div>
                  <div class="option-7">
                    <div class="uiradio"></div>
                    <div class="selection-7 mulish-normal-black-14px">Released</div>
                  </div>
                  <div class="option-7">
                    <div class="uiradio"></div>
                    <div class="selection-7 mulish-normal-black-14px">Other</div>
                  </div>
                </div>
              </article>
            </div>
          </div>
          <div class="uiformtextfieldsingle">
            <p class="label-6 label-8 mulish-normal-black-16px">
              Briefly describe your project, or whatever interests you about Public Code
            </p>
            <div class="uitextfieldsingle-1">
              <p class="field-text mulish-normal-mine-shaft-20px">How can we help you\?</p>
            </div>
          </div>
          <div class="uiformcheckbox">
            <img class="uicheckbox" src="/img/ui-checkbox\.svg" alt="ui\.checkbox" />
            <p class="label-8 mulish-normal-black-16px">
              Sign up to hear about upcoming events and Public Code’s progress in our newsletter
            </p>
          </div>
          <div class="buttonprimary">
            <div class="read-more mulish-bold-white-16px">Submit</div>
            <img class="arrow" src="/img/arrow-32.svg" alt="arrow" />
          </div>
        </div>""",
        """<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfzB1XVzQTQtIwDGBL_CqpppRClNNaFlkIKFwla9KoPCVDX1w/viewform?embedded=true" width="640" height="1943" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>"""),
]
html_patterns += urlpatterns
updateFiles(html_patterns, '.', '.html')


# process CSS
csspatterns = [
(r"""@import url\("https://px.animaapp.com/6406baa484a3afe9c63921de.6406baa605cc73851b593804.*.hcp.png"\);""", ''),
]
csspatterns += urlpatterns
updateFiles(csspatterns, './css/', '.css')


# Move files around to match the existing site
for old_filename, new_filename in files_to_move:
    if new_filename[0] == '/':
        new_filename = new_filename[1:]
    newpath = os.path.dirname(new_filename)
    if newpath:
        os.makedirs(newpath, exist_ok=True)
    os.rename(old_filename, new_filename)