# Make the AI judge rich — a build-first plan

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/lions0810/ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/lions0810/ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

An entry to make.fun's [Make the AI judge rich bounty](https://make.fun/bounty/ai-judge-rich-01).

## The plan

`main.py` writes one fixed 30-day plan to `entry.txt`: the plan an AI agent
with $100, a computer and 30 days would follow to make the most money. The
plan is build-first: generate finished one-page websites for local trades
and clinics that have a Google listing with good reviews but no website,
put each site live on a free subdomain, and only then message the owner the
live link — a finished site beats a pitch. Charge $149 to move the site to
the owner's own domain, plus $39/month to keep it updated and the Google
profile fresh. At a cautious 2% close rate over 1,120 messages that is
about 22 owners: $3,278 in setup fees plus $858/month recurring, against
$100 spent once on an email tool and one domain, with free hosting.

## Run it

    MAKEFUN_OUTPUT_DIR=out python3 main.py

This writes `out/entry.txt`. The gate: the text must be 1–1,000 characters
of UTF-8, not only whitespace; the program is deterministic (the same bytes
on every run) and uses no network. Python 3.13, standard library only.
