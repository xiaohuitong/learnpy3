### 用ssh连接GitHub仓库：
1. 打开git bash并完成基本信息之后，首先用指令：mkdir <file>创建一个空目录，然后进入：cd <file>，在初始化一个空目录，把它变为一个库：git init，添加文件到git仓库分为两步：1：git add <file>  2:git commit -m "注释" 
2. 创建SSH key：查找用户主目录，会发现有一个.SSH目录，里面有两个id_rsa和id_rsa.pub这两个文件，前者是私钥，后者是公钥。然后登录自己的GitHub账户，打开‘account setting’，点击‘add SSH key’，自己任意命名title，把公钥代码复制粘贴在key文本框里面，然后点击‘add key’，就添加成功了。
3. 如果你在用户主目录里没有发现.SSH目录，那么就需要自己创建：ssh-keygen -t rsa -C "你的email地址"   然后一路回车，使用默认值，最后就会在主目录里面生成一个.SSH目录。
4. 创建SSH key完成之后，在GitHub中创建一个新仓库，要关联这个远程库，就要使用命令：git remote add origin git@github.com:[姓名]/[仓库名].git,关联后使用命令：git push -u origin master 第一次推送master的所有内容，此后的每一次提交，直接用：git push origin master 推送。
5. 从远程克隆一个本地库：git clone git@github.com:[姓名]/[仓库名].git,然后用cd进入克隆好的仓库工作
6. 创建并切换分支：git checkout -b <分支名>，把分支合并到master上：git merge <分支名>，合并后删除分支：git branch -d <分支名>
7. 抓取分支：当合作者克隆远程已推送的库时，默认情况下只显示master分支，这个时候如果想在其他分支创作，必须创建远程分支到本地：git checkout -b [分支名] origin/[分支名],这样就可以在分支上修改上传了。如果推送失败，说明有冲突，此时，先git pull,如果git pull失败，要执行git branch --set-upstream [分支名] origin/[分支名],然后再git pull,解决冲突后再push.

### 其它git指令 ： 


1. 查看工作区的状态：git status
2. 查看修改内容（工作区和暂存区的区别）：git diff
3. 查看修改内容（暂存区和分支比较）：git diff --cached
4. 查看提交（commit）历史：git log
5. 回退到上一个版本：git reset -- hard HEAD^
6. 查看当前版本内容：cat <file>
7. 在命令行没有关闭之前，可以用指令：git reset -- hard （ID号）把回退的版本找回来
8. 查看命令历史及ID号，确定要回到哪个版本
9. 把工作区的修改全部撤销：git checkout -- <file>
10. 把暂存区的修改全部撤销：git reset HEAD <file>
11. 从版本库中删除该文件：rm <file>  
12. 执行上述命令后，有两个选择：1.从版本库中删除该文件：git rm <file>，接着执行：git commit -m “注释”；2.把误删的文件恢复到最新版本：git checkout -- <file>
13. 查看当前分支：git branch
14. 团队合作时：查看远程详细信息：git remove -v  若看不到推送地址，则没有推送权限
