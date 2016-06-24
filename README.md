# healthcare_ASEAN
Open data project: Healthcare ASEAN<br />
Trello board: https://trello.com/b/NtM7qDC5/project-healthcare-asean<br />
Slack Channel on DataKindSG team: #healthcare_asean<br />

### Some steps to follow if you are using ipython notebooks
A script has been added to ignore prompt numbers and program outputs for ipython notebooks (ipynb). To enable this functionality if you are using ipython or jupyter notebooks, follow the steps below.
1. Make sure the script - ipynb_ignore_prompt_output in scripts/ is both executable and on the system path by executing the following command
```
chmod u+x ~/path_to_repo/healthcare_ASEAN/scripts/ipynb_drop_output
```
2. Run the following command anywhere inside the git repository so that git knows to look at the .gitconfig file
```
git config --add include.path /path_to_repo/.gitconfig
```
