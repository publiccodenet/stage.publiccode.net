# This script is meant to be run on a full project HTML/CSS export from a Figma project exported from Anima. Be sure to select 'Absolute Positioning' and 'PX' length unit in the HTML export settings, then 'Export Code' -> 'Full Project' -> 'Dowload ZIP' https://projects.animaapp.com/team/maxs-team-ocll7ag/project/HKtYnxM/screen/00-process-codes-landing-page/omniview?mode=code.

import os
import re

# Rename index file
old_filename = '00u46-process-codes-landing-page.html'
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
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:3580815,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>
</body>"""),
(r"""00u46-process-codes-landing-page.html""", """index.html"""),
(r"""the agile development process. <br />You will continue running""", """the agile development process. <br /><br />You will continue running"""),
(r"""expectations?<br />Throughout this process, you also have the crucial responsibility of ensuring that""", """expectations?<br /><br />Throughout this process, you also have the crucial responsibility of ensuring that"""),
(r"""and expertise doesn’t disappear with individuals.<br />Your""", """and expertise doesn’t disappear with individuals.<br /><br />Your"""),
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
(r"""@import url\("https://px.animaapp.com/6406baa484a3afe9c63921de.6406baa605cc73851b593804.HKtYnxM.hcp.png"\);""", ''),
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