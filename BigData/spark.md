# Spark

Hadoop 是解决了大数据的可靠存储和处理。
- hdfs: 通过保存多副本在由单机组成的集群上提供可靠的文件存储。
- map-reduce: 通过mapper和reducer的抽象，将复杂的数据处理分解为多个job的有向无环图。mapper和reducer之间有shuffle操作，正是因为有了看不见的shuffle，mapReduce开发者才能感知不到分布式与并发的存在。

Hadoop 的局限：
1. 抽象层次低，需要手工编写代码来完成，使用上难以上手。
2. 处理逻辑隐藏在代码细节中，没有整体逻辑
3. 中间结果也放在HDFS文件系统中
4. ReduceTask需要等待所有MapTask都完成后才可以开始
5. 时延高，只适用Batch数据处理，对于交互式数据处理，实时数据处理的支持不够
   
因此，出现了很多相关的技术对其中的局限进行改进，如Pig，Cascading，JAQL，OOzie，Tez，Spark等。
  
Spark:
https://www.zhihu.com/question/26568496/answer/41608400 

Spark框架为批处理（Spark Core），交互式（Spark SQL），流式（Spark Streaming）, 机器学习（MLlib），图计算（GraphX）提供一个统一的数据处理平台。