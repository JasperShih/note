
~~~bash
//show all branches
git branch -a

//checkout branch
git checkout new_branch

//create new_branch which clone old_branch
//and checkout new_branch
git checkout -b new_branch old_branch

//create new branch and checkout
//below command is similar to
//git checkout -b new_branch HEAD 
git checkout -b new_branch

//delete branch
git branch -d new_branch
~~~

~~~bash
//just clone a repo and checkout another branch
git checkout -b serverfix origin/serverfix
~~~

~~~bash
//create serverfix branch and bind pull&push
git checkout --track origin/serverfix
~~~

~~~bash
//explicitly set upstream
git branch -u origin/serverfix

//show all branches tracking
git branch -vv
~~~