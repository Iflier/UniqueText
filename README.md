# UniqueText
往前推一个多月的时间，实习去了，GitHub也很久都没有更新内容了。根据工作中遇到的某些问题，想出如下两个解决方法：<br>
##问题：JSON文本去重<br>
###方法一：<br>
在Ubuntu系统下使用sort命令对json格式的文本进行排序，显然，如果不对sort命令使用任何选项进行控制的话，会打乱原有的文本内容的顺序的<br>
不过我这问题，不对排序有要求，反正也是保存到数据库中的。<br>
然后，一个一个的查询元素，个数大于的元素逐个删除，一直删除到个数为一
###方法二：<br>
同上这个方法也是会用到经过sort命令排序后的json。这里使用了Python的标准库difflib，比较这一行和下一行的相似度。
#Note:Windows OS 下的文本排序命令比较难用，没做深入讨论