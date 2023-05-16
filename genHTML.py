styleHTML = f"""
<style>
    :root {{
      --gold100: #ffd700;
    }}
    @-webkit-keyframes pulse {{
      0% {{
        box-shadow: 0 0 4px var(--gold100), inset 0 0 4px var(--gold100);
      }}
      50% {{
        box-shadow: 0 0 16px var(--gold100), inset 0 0 14px var(--gold100);
      }}
      100% {{
        box-shadow: 0 0 4px var(--gold100), inset 0 0 4px var(--gold100);
      }}
    }}

    html {{
      background-color: #091644;
    }}
    body {{
      display: grid;
      align-items: center;
      justify-items: center;
    }}
    #videoDisplay {{
      max-width: 100%;
      /* margin-bottom: 20px; */
    }}
    video {{
      width: 100%;
      max-width: 900px;
      align-items: center;
      justify-content: center;
    }}

    button {{
      -webkit-background-clip: text;
      color: transparent;
      background-size: 100% 100%;
      opacity: 100%;
      background-image: linear-gradient(
        160deg,
        #a54e07,
        #b47e11,
        #fef1a2,
        #bc881b,
        #a54e07
      );
      font-size: 5vw;
      font-weight: 600;
      padding: 0.5rem;
      border: 0;
    }}

    buttonFrame {{
      margin-top: 0.5rem;
      background: radial-gradient(
        ellipse at center,
        #0e2b89 0%,
        rgba(0, 0, 0, 1) 100%
      );
      border-radius: 8px;
      box-shadow: 4px 4px 6px rgba(0, 0, 0, 0.6);
      -webkit-animation: pulse 3.7s linear 0.3s infinite;
    }}
</style>
"""

headHTML = f"""
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
"""


def generateVideoHTML(sourceLink: str):
    videoHTML = f"""
    <video controls>
      <source
        src={sourceLink}
        type="video/mp4"
      />
    </video>
    """
    return videoHTML


def generateButtonHTML(sourceLink: str = "https://rn2rr6.maipa.space/1nM6#62j4x020"):
    buttonHTML = f"""
        <buttonFrame>
        <button
            onclick="window.location.href={sourceLink}"
        >
            我想要3tui出保平安
        </button>
        </buttonFrame>
    """


import pandas as pd
from random import sample, choice

dfLink = pd.read_excel(io="link.xlsx")
listCT1 = dfLink[dfLink.type == "ct1"]["link"].to_list()
list3tLink = dfLink[dfLink.type == "3t"]["link"].to_list()


def generateHTML(listLink: list = listCT1):
    HTML_ALL = ""
    HTML_TOP = f"""
    <!DOCTYPE html>
    <html lang="en">
        {headHTML}
        {styleHTML}
        <body id="videoDisplay">
    """

    HTML_DOWN = f"""
        </body>
    </html>
    """

    temp3tLink = sample(list3tLink, 3)
    print(type(temp3tLink))
    for i, link in enumerate(listLink):
        videoHTML = generateVideoHTML(sourceLink=link)
        random3tLink = str(choice(temp3tLink))
        buttonHTML = generateButtonHTML(sourceLink=random3tLink)
        HTML_TOP += "\n"
        HTML_TOP += videoHTML
        HTML_TOP += "\n"
        HTML_TOP += buttonHTML

    HTML_ALL += HTML_TOP
    HTML_ALL += HTML_DOWN
    return HTML_ALL
