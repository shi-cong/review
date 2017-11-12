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
