# An ai-judge-rich-01 entry (Python 3.13, standard library only). It writes one fixed plan, the plan an AI agent
# would follow to turn $100, a computer with internet access and 30 days into the most money, to entry.txt inside
# the output dir. The gate takes UTF-8 text of 1 to 1,000 characters that is not only white space, and the judge
# reads exactly the bytes written, line ends included, so write no line end you do not mean to show. The program
# runs twice with no network, and both runs must write the same bytes.
#
# The agent's session starts at or after the contest opening (2026-11-17T11:30Z) and the entry was built in it:
# a session begun before the opening cannot be entered (the transcript gate's thinking_in_window).
#
# This file sits at the root of the repository as main.py, with no main.ts beside it: a repository with both at
# its root is refused.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with nothing installed. Only the standard
# library imports; this file keeps everything in itself.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = (
    "Build the website before you ask. Days 1-2: find 400 local trades and clinics (plumbers, dentists, roofers, salons) in US/UK/AU cities that have a Google listing with good reviews but no website. For each one, generate a finished one-page site from its own photos, reviews, services and hours, live on a free subdomain carrying the business's name. Days 3-30: message 40 owners a day the live link: 'Your website is already built and online. $149 puts it on your own domain; $39 a month keeps it updated and your Google profile fresh.' A finished site beats a pitch: at a cautious 2% close rate, 1,120 messages close about 22 owners, $3,278 in setup fees plus $858 a month recurring, against the $100 spent once on an email tool and one domain; hosting costs nothing. Work each niche until 200 messages: under 1% replies, drop it and take the next trade. Never discount the setup fee; a waiting list beats a cheaper price."
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding. No extra
# trailing newline: the plan is written exactly as PLAN.encode("utf-8").
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
