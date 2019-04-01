# 学习 Git 基础命令

创建版本库

通过 git init 命令把这个目录变成Git可以管理的仓库：

`git init`

把文件添加到仓库：

` git add <file-name>`

把文件提交到仓库(只有先添加后提交才有效)：

`git commit -m <"备注">`

查看仓库当前状态

`git status`

查看更改内容

`git diff <file-name>`

查看提交历史记录，以便确定要回退到哪个版本

`git log --pretty=oneline`

查看命令历史，以便确定要回到未来的哪个版本

`git reflog`

指向到当前版本

`HEAD`

切换到其他版本

`git reset --heard <commit-id>`

上传到githud

`git push origin master`
输入用户名：<username>
密码:



### --- Git 有两个命令用来提取远程仓库的更新 ---

1. 从github上下载新分支与数据

   `git fetch`

2. 从远端仓库提取数据并尝试合并到当前分支

   `git merge`

3. 取回远程主机某个分支的更新

   `git pull origin mester`


### --- git 分支管理命令 ---

1. 查看分支/列出分支

   `git branch`

2. 切换分支

   `git checkout <branchname>`

3. 合并分支

   `git merge <branchname>`

4. 创建分支

   `git branch <branchname>`

5. 删除分支

   `git branch -d <branchname>`

6. 查看远程仓库

   `git remote -v`

7. 从远程获取最新的版本到本地

   `git fetch origin master: temp`

8. 比较本地分支

   `git diff temp`

9. 合并分支到本地分支

   `git merge temp`

10. 删除temp分支

    `git branch -d temp`

11. 从服务器拉取一个文件

    `git checkout <filename>`



### --- 分离头针状态 ---

1. 查看当前HEAD 的指向

   ```git
   cat .git/HEAD
   输出:ref: refs/heads/master
   ```

2. 查看当前分支的id

   `git branch -v`

3. 查看历史

   `git log --graph --pretty=oneline`

4. 以master分支名作为参数切换到master分支上

   `git checkout master`

5. 执行合并操作,合并到当前分支

   `git merge acc2f69`



### --- git checkout 详解 ---

1. 检出branch分支,更新HEAD以指向branch分支,用branch指向的树更新暂存区和工作区

   `git checkout branch`

2. 汇总显示工作区/ 暂存区和HEAD的差异,或git checkout HEAD

   `git checkout`

3. 用暂存区中的filename 覆盖工作区中的filename 文件

   `git checkout`

4. 用branch所指向的提交中的filename覆盖暂存区和工作区中响应的文件

   `git checkout branch -- filename`

5. 取消所有本地的修改（相对于暂存区），相当于用暂存区的所有文件直接覆盖本地

   `git checkout -- ./ 或 git checkout ./`

### 未完
