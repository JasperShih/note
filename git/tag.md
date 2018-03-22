
Git 使用两种主要类型的标签：轻量标签（lightweight）与附注标签（annotated）。

一个轻量标签很像一个不会改变的分支 - 它只是一个特定提交的引用。

然而，附注标签是存储在 Git 数据库中的一个完整对象。 它们是可以被校验的；其中包含打标签者的名字、电子邮件地址、日期时间；还有一个标签信息；并且可以使用 GNU Privacy Guard （GPG）签名与验证。 通常建议创建附注标签，这样你可以拥有以上所有信息；但是如果你只是想用一个临时的标签，或者因为某些原因不想要保存那些信息，轻量标签也是可用的。

lightweight
~~~bash
git tag v1.2 45f990c......
~~~

annotated
~~~bash
git tag -a v1.2 45f990c......
~~~

~~~bash
//show all tag
git tag

//show specific tag
git tag show v1.2

//delete tag
git tag -d v1.2

//push tag to remote
git push origin v1.2

//push all local tags to remote
git push origin --tags

//delete remote tag
git push origin -d v1.2

//check out branch on specific tag
git checkout -b version1_2 v1.2
~~~