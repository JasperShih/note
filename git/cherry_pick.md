//single commit
git cherry-pick <commit id>

//some commits(start-commit-id not including. If we want to include it, use '^' sign.)
git cherry-pick <start-commit-id>..<end-commit-id>

//mix form
git cherry-pick <commit-id1>..<commit-id2> <commit-id3> <commit-id4>..<commit-id5>
