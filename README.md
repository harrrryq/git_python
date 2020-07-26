##########################\n
-- Remove the history from\n 
rm -rf .git

-- recreate the repos from the current content only\n
git init\n
git add .\n
git commit -m "Initial commit"\n

-- push to the github remote repos ensuring you overwrite history\n
git remote add origin git@github.com:<YOUR ACCOUNT>/<YOUR REPOS>.git\n
git push -u --force origin master\n
##########################\n


>>> Agenda:\n
>>> yoyaku - my first python script, to check the clinic room availability.\n 
