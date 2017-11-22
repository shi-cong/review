## PYSTUDY
[pypi](https://pypi.python.org/pypi/PYSTUDY/0.1.0)
看书，学习。将平时遇到的一些经常要查资料的才能解决的代码全都封装在这里，以便日后能够大大提升开发的效率。
太多次重复的学习，重复的解决以前解决过的问题，那么，我现在累了，我以前解决过的问题，我不想再次继续。那
好，本项目，就是自己在学习的过程中，对学习的一些总结。在学习的过程中，本身就会写很多很多的测试代码，这
些代码在构建的过程中，如果你不保存，意味着，一段时间过后，你得重复学习。

重复学习这些毫无价值，但又很需要时间去学习的东西？这样太不划算了。
所以，这个项目，就是体现了本人对重复学习的急切不满。计算机知识大爆炸。一些技术，一段时间不用，完全忘记
，慢慢积累就是好的。

每隔一段时间，我就会对自己的代码很有嫌弃的感觉。每次都是改改改。不过每次都会进步。


[问题提交](https://github.com/shi-cong/PYSTUDY/issues?state=open)

## 博客
[planepython](http://planetpython.org/)
[图像处理牛人](http://blog.csdn.net/stdcoutzyx?viewmode=contents)

## 图像处理：
[PIL](http://pillow-cn.readthedocs.io/zh_CN/latest/guides.html)
[concept-modes](http://pillow.readthedocs.io/en/3.4.x/handbook/concepts.html)
[RGBA](https://zh.wikipedia.org/wiki/RGBA)
[三原色光模式](https://zh.wikipedia.org/wiki/%E4%B8%89%E5%8E%9F%E8%89%B2%E5%85%89%E6%A8%A1%E5%BC%8F)
[色彩空间](https://zh.wikipedia.org/wiki/%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%96%93)
[颜色空间](https://baike.baidu.com/item/%E9%A2%9C%E8%89%B2%E7%A9%BA%E9%97%B4/10834848?fr=aladdin)
[颜色通道](https://baike.baidu.com/item/%E9%A2%9C%E8%89%B2%E9%80%9A%E9%81%93)
[颜色列表](https://zh.wikipedia.org/wiki/%E9%A2%9C%E8%89%B2%E5%88%97%E8%A1%A8)
[原色](https://zh.wikipedia.org/wiki/%E5%8E%9F%E8%89%B2)
[网页颜色](https://zh.wikipedia.org/wiki/%E7%BD%91%E9%A1%B5%E9%A2%9C%E8%89%B2)
[直方图](https://zh.wikipedia.org/wiki/%E7%9B%B4%E6%96%B9%E5%9B%BE)
[图像滤波](https://baike.baidu.com/item/%E5%9B%BE%E5%83%8F%E6%BB%A4%E6%B3%A2)
[二值图像](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%80%BC%E5%9B%BE%E5%83%8F)

## 一些新思维
计算机实际上从应用的角度来说，是一个没有门槛的学科，从科学的角度来说，计算机软件发展了这么多年，不可能从
零开始实现，所以一般来说都是站在巨人的肩膀上，不要认为会编程就非常了不起，实际上没什么，只是别人不愿意去
学习和了解，很多做技术的人，都有这么一个缺点，就是恃才傲物，其实那些人会的这些东西，一些高材生只需要花很
少的时间就可以很快学会。当我了解到这些之后，我的思路有一些另外的变化，不再认为会编程很厉害。哦，只会编程
会被人看不起，你得学好基础学科，然后应用计算机来实现基础学科的内容，这样才会很了不起。

前几天，有一个生物信息工程师叫我去面试，我有一点恐慌，这几天休息的挺好，身体慢慢都恢复了，皮肤也变好了，
开始学习新的领域了。

## 一些新的工具
曾经抓了8个月的包，封装了selenium模块。

需要下载chromedriver，然后加到 path环境变量中。

## 框架
框架的代码写的好，但是，框架似乎不适合所有的业务场景。

## 新发现
chromedriver headless 并没想象中的那么好，配合selenium也是漏洞，比如，不能点击链接。

* 不能点击链接，能点击button提交表单，但是不能点击链接；

## 对异步的看法
有的人大谈爬虫的异步，实际上是做梦，为什么呢？因为你说grequests, gevent, 异步是吧？那mysql驱动说异步的吗？
其他消息中间件是异步的吗？就说现在的生态系统，你用异步，以后等着项目被重构吧。话说，爬虫需要异步吗？需要
那么快的速度吗？甚至有的人以为用grequests就能实现所有的爬虫，我看这是在痴心妄想，你以为你能搞定所有的抓包，
别人的反爬虫都是吃屎的？还http模拟，我说这些人都是只能处理简单的需求而已。也就能搞搞简单的爬虫。

陆陆续续的做了python的开发将近5年多了，个人使用时间3年多，主要是写点自己的小工具，工作使用2年，就这点使用经验，谈谈本人对python这门语言对一些看法。


# 5年python使用经验的一些感言（零基础接触编程，从入门到会）
## 0、python是一个对学计算机比较对入门语言

为什么说python是一门比较好对学计算机对入门语言呢？我最初一开始本来是在学校学的java语言，后来无意间接触到了一些黑客类型的人，就因为觉得他们特别厉害，所以，我感觉我学了java好像什么都不会，很多计算机基础都知识都不牢固，也不是我不努力，因为计算机的知识绝大多数不是从书本上学来的，特别是中国的计算机教材，本身就是一个问题，根本就不能吸引读者，那些毫无兴趣的东西，我一看就没想看，后来就是因为接触到这个黑客，所以，我就在网上找，什么语言学黑客比较好，后来我在2012年的冬天晚上12点多，我上晚班，无意间发现了python这门语言，从此就坚持下来了，由于python属于胶水类的语言，什么是胶水呢？谈谈我的看法，就是说，python很容易与c语言进行连接起来，就是说，你用python很容易就可以调用c语言写的函数，想象一下，你用java的 jni技术去做（为什么jni这么难学？因为java官方可能不想因为第三方去扩展从而降低了java的跨平台特性），基于这个原因，我用python搞懂了计算机网络，学会了icmp, arp, rarp, tcpip, udp， http, https, dns这些东西，想象一下，如果让你用java，你能学会吗？我感觉我肯定不会了解到这么多底层到东西。

上面说明了一个事情，就是说，如果作为计算机打基础，可以从python和c入手，用c学内存方面的编程，用python去学习网络编程，等把这些基础打好之后，后面就可以上更高级的东西了，比如java。

## 1、我为什么感觉python不适合长期学习，甚至不适合做大型应用？
因为我发现，第三方的库质量不一，就是说有的写的好，有的写的很差，有的过度设计，不利于扩展，失去了python的优点，python的特点就是小而美。

举个例子，写的比较好的python库有requests，我就只认为这个库可以，为什么呢？我没有理由。这个库第一代码写的够简单直观，第二，文档齐全。

写的比较烂的呢？pymongo，这个库大概是我见过写的最烂的库，我不是说这个库的代码写的烂，而是我觉得这库的设计原理存在很大的缺点。因为本人对动态语言的那些坑过我，所以我极度讨厌这种，不先定义，后使用的手法。

还有一个特点就是，python他没有自己的方向，大家都知道python3吧，自从我升级python3之后，我发现很多python2的库都不能用了。这给我的开发带来重重困难，虽然后来都被我解决了，但是现在我还是想骂。

scrapy这个框架如何呢？我不认为这个框架有多厉害，为什么呢？
因为我写爬虫的话，真正工作中，我居然没有用到这框架。因为这个框架的过度设计，导致，我无法扩展这个框架（我指的是那种优雅的扩展）。

mysqldb动不动不再维护，为了找一个能用的mysql库，花1天时间去找，这些都不容易。

想象一下，你的项目是2008年开发的，结果现在2017年了，你来维护，结果发现很多库都不存在了，你是一个什么样的心情，当时给我的感觉是我要死掉了。

基于上面的原因，本人认为，python不适合做大项目，向下兼容做的太烂，动不动就要依赖于很不负责的第三方开发者的开源库，然而很多开源作者到最后都不再维护了，因为开源，所以导致没有了收入来源。想想这里也 很可悲。

还有一个就是python都函数参数都省略写法，以及装饰语法，我在工作中我从来不用这种怪异都写法，当然那些用这种都人会觉得这种很漂亮，实际上我看过了那种装饰都语法，非常难维护，尤其是在业务逻辑很复杂都情况下。一点都不直观。

## 2、python的字典非常的害人
为什么说python的字典非常的害人呢？原因就是这个动态特性，字典里的value可以存储任意类型的值，这种事情，想想就很可怕，这样感觉非常的不严谨。知道这种情况会给我们带来一种坏习惯，就是不先声明后使用。这种情况很可怕，所以，我经常有时候会觉得c语言这种特性，在有时候是多么的可贵。但不好的情况是，有的人使用python，大多数是第一次使用，也就没有了先定义后使用了，字典由于任意类型这种特性，所以导致，我感觉我不需要创建数据对象，一开始还行，由于代码比较少，但 随着代码量和数据结构但复杂度不断增加，这种灾难就体现出来了。因为你无法知道这个变量的类型，这样给维护这个代码的人带来了空前的灾难。唯独重构才能搞定这种维护。我说的重构是重写。

其实这个字典，带来的缺点是很大的，给人的习惯非常不好，看起来好像代码写的少了，实际上，后面要用很大的时间去平衡这个少。看起来java好像很臃肿，实际上，只要是封装不是很深，维护起来一样很容易，为什么？先定义后使用。

这一点做的比较好的有django的orm，这里我只说django的orm写的不错，其它的，我感觉不是特别的友好，由于django的高度耦合，所以，很难拆开这些组建，所以，感觉， django不是特别适合我的个性（从这里看出，我是特别爱自由的编码者）。

## -1、最后
有的人说，python的代码超过10万行就不行了，而有的人说看我的代码就超过了10万行还不是照样。我想说，自己感受就行了，你花了时间搞定了这些难搞的，后面来维护你代码的那个人那我就不敢说了。生存不易，我是一个爱自由的人，对代码要求是严谨对习惯，可读性高，效率放后面。后来，我就感叹了，当年学的java是多么的好。虽然这一路走来，不知不觉就过去了，3，5年时间，都是在玩蟒蛇，但是，我学会了基础的理论，也是真的懂了软件。

对了，下次，我准备尝试下node，听说node的异步不错，而且node的语法我也感觉还行。今天就这样了。晚安!

## -2、更新
想说python 为什么这么让人不爽，有时候就是这种心情，可能有点喜新厌旧，可是又找不出一个能取代python的一个工具，让我去弄别的语言，我又没那个心情，有时候，放一放学习的进度，回头再看看那些框架其实感觉
还是可以的，无所谓了，为什么呢？偶尔会感叹人命运的不同就会导致不同的人生。我也就敢到墙外敢说说真话。

scrapy在对于那种简单的需求还是可以弄的，如果要实现复杂的需求就要学些了，当然我说这些都是废话。

最近再看了看我的那本scrapy的书籍，感觉有一种悟性，似乎人生对我们来说是不能选择的，有给你用的就不错了，有时候，我想，我是否该选择随遇而安，比如就这个框架而言，弄懂这些就够了憋，还要学什么呢？还要自己去弄框架，计算机软件发展这么多年，计算机出现的时候，我还没出生，而我却要用我有限的生命去探索计算机之前的历史，似乎有违科学。可能是我看问题的角度不同吧。

## -3、再更
似乎，解耦和可靠是互相矛盾的，追求解耦，就会降低可靠性，追求可靠性，耦合度就高了。
有计划是好的，可是，当实现计划时，就会发现，那只是纸上谈兵，做了架构之后，在编码的时候，就会发现，其中的各种变化。

## -4、何为机器学习的模型，一家之谈
在设计统计数据库的时候，似乎，这就是一个设计模型的过程，我一直认为的决策模型，现在就摆在我的眼前，决策模型从广义上来说，样本数据似乎就是模型，
这是我对模型的定义。学了几个月的机器学习，算法学了几个，但依然不知道什么是模型的概念。也没人跟我说，谁会教你？那，什么是模型呢，什么是机器学习算法呢？机器学习算法是根据样本数据（概率与统计里简称，样本空间），机器学习的算法既然是算法，那说明，算法可以选择很多种，那那些所谓的大公司招聘的模型岗是做什么的呢？我想，所谓的模型就是对统计数据的抽象，当然，这个抽象是需要很深的统计学（概率与统计）的知识，才能把模型设计的好的。否则，都是纸上谈兵，我说的纸上谈兵是什么意思呢？很简单，纸上谈兵就是，思考的不全面，往往，统计学学的不好的人设计的模型，肯定是不好的，一个好的模型必定能做更好的决策，我这里说更好的决策，却不是最好的，那是因为，还有更好的模型。

这就是我对模型的理解。

## -5、新思考
延续数千年的封建社会，农民（土地是租的），地主（拥有土地的人），农民想做地主，地主想保护自己不沦为农民，说白了，都是为了地盘。虽然，几千年的封建王朝轮询，农民不断的当地主，然后地主又不断的当农民，这只是一个历史的循环。没有任何人能改变这种规则，即使在原始深林，动物们也会为了守护自己的地盘，和占有地盘而战斗到底。想想，人和动物没什么本质的区别，区别在于，人可以接受教育变成有教养的人，动物就不知道了。

我不想当地主，但是，我就想在异地也有一个家。

但这也是一种奢望。因为社会的资源是有限的，不可能让所有的人都平均分配，一开始起跑线在前面的人，后面自然大多数一帆风顺。

所以，农民当家做主的时代永远不会到来，面临奔3，唯一的出路，就是拥有自己的产业。

以前，我认为成功是有钱，现在我认为的是当地主。

站在历史的规则里，无法自拔，这也是“丛林法则”，没有任何人能摆脱这种规则。

李白作为男人，说实话，他的诗，小时候只会背，但是大脑从来是不会去思考的，想想，因为没什么感觉，
可是到了一段时间之后，心里就特被感触了，豪迈，奔放，意境特别的朝圣。

## -6、我创造了属于自己的世界
毛主席说过一句话，“星星之火，可以燎原”，意思是说，只要有一点点希望，只要坚持下去，就能成功。
我创业了，做了别人不敢做的事情，可是，我又有什么选择呢。

## -7、实践中的一些经验

* [ ] 在函数中永远不要改变形式参数的值，什么意思呢？举个例子：

```python
def f(a):
    for a in range(10):
        print(a)
```
我说的就是这种，不要声明和形式参数一样的变量，后面会改变形式参数，导致很费时的错误。

* [ ] mysql集群优化方面的实践

今天在查看自己的数据中心时，发现爬虫的速度很慢，登上mysql的服务器一查看，mysqld cpu占用率98%，我就在想为什么会出现这么高的cpu使用率，最后
想了下，我的虫子是虫子20个线程并同时向数据中心推送数据过来，数据中心，mysql主服务器写入的时候，必须查询下mysql主数据库中是否有这行数据，就
是这一行数据就占用了大概2-3秒的时间，为什么呢？因为是用字符串查询，想象一下，由于这个时候，tornado其中一个连接正在写入主数据库，然而，我的
一部分表的引擎室inodb，然而，我还用到外键，意味着你每次插入一条数据，mysql本身就要去检查一下这个外键的值是否在所关联的表中是否存在，但由于
之前myiasm中遇到的坑，导致我不想用myiasm，所以，这里是绕不过去的坎，但是有一条是可以取消外键关联，但是，如果取消了外键关联，就会造成数据的
不稳定性，什么叫数据的不稳定性？感觉就是数据库中存在脏数据，到时候要花很多时间的去清楚这些脏数据，但是为了确保这一特性，mysql牺牲了速度，
这之前所说的，追求解耦，就会降低可靠性，这里的可靠性就是数据不存在脏数据了，但是为什么说解耦这里就变成了稳定性呢？软件的解耦是很重要的，为什么呢？你想想啊，软件解耦之后，相互之间变成了几个独立的组件，而这些组件之间通过互相通信来共同协作，为以后的软件的继续扩展提供了很好的保证，
但是一个解耦的系统不是那么好设计的，需要拥有丰富的经验，因为在想做一个解耦的系统的时候，会遇到各种各样的问题。刚才说到mysql innodb速度下降了，理由是它增加了数据的可靠性。另外一个原因，是因为，本来我的mysql做了主从复制，而我查询数据库的时候，确是用的主数据库，理论上来说，我应该
查询从数据库，而写主数据库，于是我回头看了下代码，果然是这样，但是出乎我意料之外的是，我修改了之后，速度反而降低了，我也在思考着，为什么会
这样呢？其实，用脑子想一下，想想啊，mysql主从复制也要插入数据库啊，这样不是也有文件锁吗？这能行吗？所以说，mysql的读写分离，是一种不可靠的
最可靠的是从程序代码，sql语句上优化。

虽然验证了自己的方法不可行，可还是有点不甘心的，于是关掉程序，把代码改回去，在看下速度。结果居然更慢了，说明，我前一种方案要优于现在的，为什么呢？我之前改了从从数据库查询，速度每秒钟 mysql主数据库能插入20左右数据，而现在，没秒只能插入2个，4个，这说明什么问题，证明我之前的想法是
对的。

由于，这个sql语句没法优化，所以，只能从数据库上集群进行优化，我写了一篇mysql读写分离的博客，但是遇到了问题，因为有些东西还没搞清楚。以后弄清楚后，再谈了。

* [ ] 谈谈对中国的音乐的看法

不喜欢，听到中国因为，直接关闭，为什么呢？觉得恶心。可能不对我的味，要么就是很没品味，要么就是像没教养一样在那里乱叫。要么就是吵死了，感觉
完全是噪音。

那么什么样的音乐能吸引我呢？不能太悲伤，往往那种淡淡的感觉就非常的吸引人，具体参考，可以考虑看看李白的诗句，有时候，遇到一些事情，你读读那个
诗句，非常的有意境，也很朝圣。

音乐不是制造噪音，不是洗脑，后面有了更深层次的见解再详谈。

* [ ] 谈谈对人工智能的看法

喜欢，但是，假如说，想用这个创业，但似乎又是很难的，为什么呢？作为码农，你有那个数据功底吗？其实，这就有点危言耸听了，据有关人士说，数学不是
问题，只要够努力，就能创造奇迹。但最后，数学还是要学的，但是，对我而言，如果不是为了解决一个问题，我没有那个动力。

谈到了，创业，就说说人工智能的前景。前景当然是有的，可是你有那个资本去烧钱吗？作为码农来说，就很难了，但是对我门这些即将老去的（转行的）码农来说，30岁就是个头了，转行相当于一无所有，创业是必然，继续坚持是困兽之斗。说个不好听的，30多之后还不退休，顶多成为了老的科学家，年轻人来了之后一说，哎呦，资金又被老的科学家给拿走了，年轻人需要资源，你说老的科学家一直没作为，创造力下降为什么不退出，不是不退出，是没有退路，想想退出之后，以后能做什么？可是人工智能怎么賺钱呢？机器人？自动编程？医生？

就商业领域来说，有多少门路能用到人工智能呢？

##### 医学：
医生机器人？可别想象，我先从简单的，我所理解的方向去思考，那么一生机器人首先具备一个内部的机器学习程序吧，假设由于为得到了国家的支持来研发
医学上的人工智能，所以我有权利收集所有的病例，我把这些病例收集过来之后，做一个汇总，然后收集所有的医学书籍，全部输入到机器数据库里，到时候
只要一个非常简单的人，只要会电脑打字就可以了，他将病人的特征输入到电脑里，一查询，首先从多种书籍中都查到，属于哪几种病，然后，在调用病例数据库
看这些特征的权重在这些病例中占多少，由于中国从来都是少数服从多数，（虽然美国是少数人可以和多数人抗衡，历史中的千古一帝也是经常做一个人坚持自己的意见和所有的大臣都反对他），那么少数服从多数，那么多数案例中都显示，哎呀，这个病人的症状，就是这个病。好了，确定了分类，那么，即将启动
治疗程序，该吃药的吃药，该动手术的动手术。

好了吧，这几乎就可以解放农村医务室了，因为农村医务室也就这点能力，农村医务室看大病能把你治死，当然这就是属于小病的范围了，但是效果出来了，
农村医务室的人员失业了，以后农村医务室，只需要一个电脑打字员。然而，政府引入了先进的（其实就是很简单的统计程序），然后政府每年花费几千万的
软件维护费用，而那些维护费用全让那些有关系所谓的老的科学家给拿走了。

然后说高端一点的，医学中的机器视觉，可以想象一下，假设能造一个机器人，就像一个清洁工，也是一个人体保卫者，首先呢，这个机器人，非常的小，美其名曰，美少女少男战士，因为他保护着你体内的任何发生异变的细胞，一旦发生了异变，那么不好意思，他就要干掉他，那么，美少女少男战士该如何生存下去呢？他的食物就是变异的细胞，一生的追求就是游走于人体的血管之中，人体内本来就有这种，可怕的是那种癌细胞，能伪装成正常的细胞，其它细胞认为癌细胞是自己的同类，癌细胞不断的发育就完蛋了，到时候就把人给法雨死了。那么美少女少男战士如何识别出癌细胞呢？可能就涉及到其他的技术了，除了视觉技术，可能还能搞点嗅觉，但是搞不好还会把人给搞死了。这不是我本意啊。所以，这个高端东西就需要大量的实验了。美少女少男战士。

记得，非典那一段时间，国家的检测仪就能检测出非典患者。这也是机器学习的范畴吧。

##### 谈谈历史吧
上文刚说到，朱元璋的后代有个儿子，被逼无奈只能篡位，但是面临失败，他们想了下必须先取南京，就是当时的大明朝的首都，但是那个王想了下，必须按照直接来搞，因为必须要经过山东，就要打山东，后来有个和尚给他提议，可以绕过山东直接取南京。

上文有历史说明了一个最短路径的问题，爬虫中也经常遇到这种问题，有时候是可以直接绕过中间环节，直接到达目的页面的，具体可以参考，浏览器就可以不访问主页就可以直接访问一些get请求的页面，但是，除了那种有用户验证的。之前没有登录就不能直接到达。这个就要先登录一下，然后直捣黄龙。

历史就是这么有意思，那个王的北军和我的虫子有异曲同工之妙。

管理员还以为我睡觉了，不断更换页面解析规则。后来被我的统计模型给报警了。被我发现了。

#### 谈谈远程控制
之前在远程控制的设计里面讲到，要实现远程控制，要么写tcp服服务器，要么在每个机器上安装远程控制服务，这两种方式的实现有一定的出路，第一种，一个服务器多个客户端，另一种方式，多个服务器，多个客户端，那么从软件开发的角度来说，显然第一种方式要好一点。为什么呢？

第一，写的代码少；
第二，方便后期维护；

为了实现软件的解耦，需要利用websocket来实现一个控制端服务器，然后在每台虫子上面实现一个客户端，这样的话基本就可以实现远程控制了。

虽然这是一种看起来比较好的方案，然而，却还有更好的。

专业做运维的兄弟就知道怎么做，不是有运维脚本自动化吗？对了，说对就是这个。但是，这样也有一个缺点，缺点就是需要配置每台vps，所以，对我来说，优选的还是第一种，第二种看起来简单，实际后期的开发和维护是比较复杂的。

那么远控的方案就这样确认下来了，就是利用websocket来做。

记得很久以前一个黑客朋友（我之所以说黑客称他，那是因为，那就是真正的黑客，没有那么浮夸的姿势，不像那些书本上写的那么天书，
人家解决问题的方式很简单），写了一个远控花了6年时间。别人跟就没学历。

而我这个远控是为了做什么呢？当然是为了自动化管理vps，为什么要自动化管理vps？这是为了我的爬虫系统能够方便调度。
我想当黑客吗？答案是否定的，其实当年想当黑客是因为社会对我的不认可。凭什么，我java学的那么好，为什么找不到工作？
由于社会的不认可，导致我只能揭竿而起，居然去学黑色产业链的技术。然而实际上更难。

一个服务器管理多个客户端的不利之处在于，由于多个客户端的生产环境不同，会导致一个客户端上面的大量报错直接会影响大脑的决策，之前就谈到过人工智能方面的东西，少数服从多数嘛，这样很容易造成大量报错，为什么国家要对港澳实行一国两制呢？爬虫不是个容易的事情，许多公司做的爬虫都是很垃圾的爬虫，很难说很完美，大量的都需要人工去操作。

那么总结这3种方式的优缺点了

第一种，websocket服务器控制多个爬虫客户端
* 易于管理，客户端只要写对服务器ip地址和身份验证信息就可以；
* 由于每个客户端的场景不同，导致一个客户端大量报错导致ai决策失败；
* 增加了ai层的复杂度（为了解决缺陷所以ai层必须设计更加复杂的决策模型）
* 由于是websocket连接，长连接，nginx的超时时间怎么搞定呢？这也是一个问题；

第二种，第三种我就不想说了，为什么呢？因为，第一种方案只要增加统计模型的复杂度就可以解决了。

这一切看起来是多么的完美。本来认为的难题，结果经过我这么写了一点文字，居然就迎刃而解。

一直以来我都不擅长思考，大概就是没有纸和笔。
因为社会的不稳定因素导致了我失去了这些正确的思维。
用笔和纸来思考看起来是多么的完美的一种方式。

那么我能用纸和笔来思考从而总结出一些方案，那么，相信我的机器人也一样能够做到。
那么，电脑已经够智能了，概率统计也是牛的不得了。那么，搞定应用方面的东西，那么机器如何像人类一样利用工具来思考呢？
下一篇，我将会谈到机器如何利用工具。
