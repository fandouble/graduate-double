# graduate-double
sxu-double-graduate

---
2018/4/2		

- 新建项目上传到github
- 学习大佬代码，发现一个[前端组件库](https://v4.bootcss.com/)可以学习利用
- 安装配置MySQL：具体过程，可参考此[链接](https://blog.csdn.net/hisense20112784/article/details/72909701)
- 学习workbench使用：参考此[链接](https://blog.csdn.net/z45689/article/details/54139396)

*本来考虑使用toad for mySQL，未果*

###bug:根据[廖雪峰的博客](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432338991719a4c5c42ef08e4f44ad0f293ad728a27b000#0)，一步步来连接数据库的。但是始终有个bug调不通：*TypeError: cannot 'yield from' a coroutine object in a non-coroutine generator*，参考[网友解决办法](https://www.liaoxuefeng.com/discuss/001409195742008d822b26cf3de46aea14f2b7378a1ba91000/0014611725866132bdd2a03a90a46e594eca722371a46b2000)，未果。
这里还介绍了async/await[新语法](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00144661533005329786387b5684be385062a121e834ac7000)

2018/4/3

- 今天要把昨天的那个bug搞明白

*的确是需要把async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：把@asyncio.coroutine替换为async；把yield from替换为await。我在这里把所有的async换成了@asyncio.coroutine，这样才能与yield from匹配，不会报错。*

- 研究一下怎么把.csv文件中的数据添加到数据库里面