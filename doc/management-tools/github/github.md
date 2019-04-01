# 在本地创建Git 仓库连接到GitHub 下载库

1. 在本地创建sshKey

   `ssh-keygen -t rsa -C joker_zzp@163.com` 一路回车

2. 查看公钥

   cat ~/.ssh/id_rsa.pub

3. 将公钥添加到 [GitHub 官网](https://github.com/) settings --> SSH Key 中

4. 测试sshKey是否成功

   `ssh -T git@github.com` 

   ps：如果是第一次会让你保存 ssh 公钥，输入 `yes` 即可

5. 从远程克隆一份到本地

   `git clone <GitHub地址>`

6. 本地库关联远程库

   `git remote add origin <GitHub地址>`

7. 推送master分支

   `git push -u origin master`

   ps: 第一次加-u 是推送内容并关联分支

8. 推送成功后 下一次推送就不用加 -u

   `git push origin master`

9. test

   创建文件并上传测试一下是否上传成功
