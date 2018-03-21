
~~~bash
git stash

//do not clean working directory but save stash record
git stash -k

//includ untracked files
git stash -u

git stash list

//delete stash record
git stash pop

//do not delete stash record
git stash apply

git stash drop
~~~