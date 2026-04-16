---
description: mettre à jour le contexte d'un projet (AGENTS.md) - [commit]
agent: build
permission:
  edit:
    AGENTS.md: allow
  bash:
    "git log*": allow
    "git diff*": allow
    "git show*": allow
  glob: allow
  grep: allow

---

## overview

update the project context file AGENTS.md to reflect changes in the project life. 

## tasks

1.  analyze the codebase of the **app directory** to identify any updates related to the sections outlined e.g, new instructions, file structures, code style guidelines, or development workflows,  in AGENTS.md with 2 alternatives:
   + if $1 is provided and a commit hash or HEAD~n format, consider the modifications made since that commit
   + else, consider the entire codebase as is

2. update the AGENTS.md file to accurately reflect those found updates in `app/`,   be concise so that AGENTS.md does not exceed 150 lines.