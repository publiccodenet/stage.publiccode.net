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
(r"""<div class="iconpathvendor-oss-LaQMVA">
                    <div class="paper-AURMxU paper">
                      <img class="union-QGxxzp union" src="img/union-16@2x.png" alt="Union" />
                      <img class="union-8fzHDA union" src="img/union-11@2x.png" alt="Union" />
                      <img class="union-8NkbQB union" src="img/union-12@2x.png" alt="Union" />
                    </div>
                    <div class="x-AURMxU">
                      <img class="vector-kehPhm vector" src="img/vector-15@2x.png" alt="Vector" />
                      <img class="line-10" src="img/line-10@2x.png" alt="Line 10" />
                      <img class="line-11" src="img/line-11@2x.png" alt="Line 11" />
                    </div>
                    <div class="fork-standard-AURMxU">
                      <div class="ellipse-192-fmmRzO"></div>
                      <div class="ellipse-193-fmmRzO"></div>
                      <img class="vector-6-fmmRzO" src="img/vector-6-1@2x.png" alt="Vector 6" />
                      <img class="vector-fmmRzO vector" src="img/vector-16@2x.png" alt="Vector" />
                      <img class="vector-H8u4P1 vector" src="img/vector-17@2x.png" alt="Vector" />
                    </div>
                  </div>""","""<img
                    class="iconpathoff-the-shelf-6tRMEp"
                    src="img/icon.path.vendor.png"
                    alt="icon.path.off-the-shelf"
                  />"""),
(r"""<div class="iconpathvendor-xJm1MO">
                    <div class="group-146-FfxTRb">
                      <div class="paper-4ChY5a paper">
                        <img class="union-Rf9Og4 union" src="img/union-17@2x.png" alt="Union" />
                        <img class="union-mcmxHP union" src="img/union-13@2x.png" alt="Union" />
                        <img class="union-34gfT2 union" src="img/union-14@2x.png" alt="Union" />
                      </div>
                      <img class="code-4ChY5a" src="img/code@2x.png" alt="code" />
                      <div class="x-4ChY5a">
                        <img class="vector-5jjppE vector" src="img/vector-15@2x.png" alt="Vector" />
                        <img class="line-10" src="img/line-10@2x.png" alt="Line 10" />
                        <img class="line-11" src="img/line-11@2x.png" alt="Line 11" />
                      </div>
                    </div>
                  </div>""","""<img
                    class="iconpathoff-the-shelf-6tRMEp"
                    src="img/icon.path.vendor-oss.png"
                    alt="icon.path.off-the-shelf"
                  />"""),
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