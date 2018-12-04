# sql-injecton

### 找网站中的注入点
1. 判断网站使用的动态语言
  + 一般常用的都是php, jsp, asp 的，可以通过修改网页的后缀名即可判断
    > 例如:
    > `http://***.com/index.html` 将`index.html` 修改成`index.php` 如果页面没有报错正确显示了 说明网站使用的是php语言，其他语言也如此判断即可
2. 找出有可能出现的注入点
  + 寻找有没有网址尾部是 `http://***.com/index/doc?id=1` 这样的页面
  + 页面伪静态 `/index/doc/id/1.html` 这样的页面也是通过给id传值在把路径处理一下显示的，实际和 `/index/doc?id=1` 是一样的，修改成这样的路径也可以正常访问的
3. 判断有可能出现的注入点有没有注入漏洞
  + 在网页 /index/doc?id=1 后面加上自己写的sql语句，通过页面返回的是不是正确的就可以判断出网站有没有sql注入漏洞
    > 例如：
    > http://***.com/index/doc/id/1.html 修改网址 http://***.com/index/doc?id=1 页面没有报错这是一个可以尝试注入的注入点
    > 测试简单的注入 `index/doc?id=1 and 1=1` 也面应该返回正确的页面 `index/doc?id=1 and 1=2` 页面如果返回一个错误的页面说明这里有注入的漏洞
