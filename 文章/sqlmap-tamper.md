# Sqlmap tamper 对照表

> ### All
>> |dba|        Script         |Function                                     |
>> |:---:|:---------------------:|:--------------------------------------------|
>> |All|apostrophemask         |用utf8代替引号                                 |
>> |   |base64encode           |用base64编码替换                               |
>> |   |multiplespaces         |围绕SQL关键字添加多个空格                        |
>> |   |space2plus             |用+替换空格                                    |
>> |   |nonrecursivereplacement|双重查询语句。取代predefined SQL关键字with表示    |
>> |   |space2randomblank      |代替空格字符（“”）从一个随机的空白字符可选字符的有效集|
>> |   |unionalltounion        |替换UNION ALL SELECT UNION SELECT             |
>> |   |securesphere           |追加特制的字符串                                |
> ### MSSQL
>> |        Script         |Function|
>> |:---------------------:|:----------------|
>> |space2hash             |绕过过滤‘=’ 替换空格字符（”），（’ – ‘）后跟一个破折号注释，一个随机字符串和一个新行（’ n’）|
>> |equaltolike            |like 代替等号|
>> |space2mssqlblank       |空格替换为其它空符号|
