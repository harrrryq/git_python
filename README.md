# Agenda:
yoyaku - my first python script, to check the clinic room availability.

# DeleteHistory
##########################
-- Remove the history from 
rm -rf .git

-- recreate the repos from the current content only
git init
git add .
git commit -m "Initial commit"

-- push to the github remote repos ensuring you overwrite history
git remote add origin git@github.com:<YOUR ACCOUNT>/<YOUR REPOS>.git
git push -u --force origin master
##########################
