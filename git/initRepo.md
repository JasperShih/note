# Adding an existing project to GitHub using the command line

https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/#further-reading

* Create New Repository drop-downCreate a new repository on GitHub. To avoid errors, do not initialize the new repository with README, license, or gitignore files. You can add these files after your project has been pushed to GitHub.

* Open Terminal.

* Change the current working directory to your local project.

* Initialize the local directory as a Git repository.
    ~~~bash
    git init
    ~~~

* Add the files in your new local repository. This stages them for the first commit.

    ~~~bash
    git add .
    # Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
    ~~~

* Commit the files that you've staged in your local repository.

    ~~~bash
    git commit -m "First commit"
    # Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
    ~~~

* At the top of your GitHub repository's Quick Setup page, click to copy the remote repository URL.

* In Terminal, add the URL for the remote repository where your local repository will be pushed.

    ~~~bash
    git remote add origin remote repository URL
    # Sets the new remote
    git remote -v
    # Verifies the new remote URL
    ~~~

* Push the changes in your local repository to GitHub.

    ~~~bash
    git push origin master
    # Pushes the changes in your local repository up to the remote repository you specified as the origin
    ~~~
    
# Replace existed repo with current project 

https://stackoverflow.com/questions/41605724/how-to-get-back-a-clean-git-repository

Shivkumar kondi

To Completely reset do this steps:

Delete the .git directory locally.

Recreate the git repostory:

~~~bash
$ cd (project-directory)
$ git init
$ (add some files)
$ git add .
$ git commit -m 'Initial commit'
~~~

Push to remote server, overwriting. Remember you're going to mess everyone else up doing this … you better be the only client.

~~~bash
$ git remote add origin <url>
$ git push --force --set-upstream origin master
~~~