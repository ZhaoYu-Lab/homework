"""
#z2的欧氏距离项目筛选结果

目标项目为ant-1.3
取欧式距离最近的k个其他版本项目
k=3时，取jedit_4_2 jedit_4_1 jedit_4_3
k=5时，取jedit_4_2 jedit_4_1 jedit_4_3 jedit_4_0 synapse_1_0
k=10时，取jedit_4_2 jedit_4_1 jedit_4_3 jedit_4_0 synapse_1_0 jedit_3_2 camel_1_4 log4j_1_1 log4j_1_2 xalan_2_7
"""
"""
目标项目为ant-1.4
取欧式距离最近的k个其他版本项目
k=3时，取jedit_4_3 jedit_4_1 jedit_4_2
k=5时，取jedit_4_3 jedit_4_1 jedit_4_2 synapse_1_0 camel_1_4
k=10时，取jedit_4_3 jedit_4_1 jedit_4_2 synapse_1_0 camel_1_4 log4j_1_1 log4j_1_2 jedit_4_0 xalan_2_7 ivy_1_1
"""

"""
目标项目为ant-1.5
取欧式距离最近的k个其他版本项目
k=3时，取xalan_2_7 xalan_2_6 camel_1_4
k=5时，取xalan_2_7 xalan_2_6 camel_1_4 jedit_4_3 log4j_1_2
k=10时，取xalan_2_7 xalan_2_6 camel_1_4 jedit_4_3 log4j_1_2 xalan_2_4 camel_1_2 xalan_2_5 ivy_1_1 camel_1_6

"""
"""
目标项目为ant-1.6
取欧式距离最近的k个其他版本项目
k=3时，取jedit_4_3 xalan_2_7 camel_1_4 
k=5时，取jedit_4_3 xalan_2_7 camel_1_4 xalan_2_6 log4j_1_2
k=10时，取jedit_4_3 xalan_2_7 camel_1_4 xalan_2_6 log4j_1_2 jedit_4_1 log4j_1_1 jedit_4_2 ivy_1_1 camel_1_2

"""
"""
目标项目为ant-1.7
取欧式距离最近的k个其他版本项目
k=3时，取camel_1_4 xalan_2_7 jedit_4_3
k=5时，取camel_1_4 xalan_2_7 jedit_4_3 xalan_2_6 camel_1_2
k=10时，取camel_1_4 xalan_2_7 jedit_4_3 xalan_2_6 camel_1_2 log4j_1_2 xalan_2_4 camel_1_6 log4j_1_1 ivy_1_1

"""
"""
目标项目为camel-1.0
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_1 ant_1_7 ivy_1_4
k=5时，取ivy_1_1 ant_1_7 ivy_1_4 ant_1_5 log4j_1_2
k=10时，取ivy_1_1 ant_1_7 ivy_1_4 ant_1_5 log4j_1_2 xalan_2_6 xalan_2_4 ant_1_6 xalan_2_7 xalan_2_5

"""
"""
目标项目为camel-1.2
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_7 ivy_1_4 xalan_2_6
k=5时，取ant_1_7 ivy_1_4 xalan_2_6 xalan_2_4 xalan_2_5
k=10时，取ant_1_7 ivy_1_4 xalan_2_6 xalan_2_4 xalan_2_5 log4j_1_2 ant_1_5 xalan_2_7 ivy_1_1 ant_1_6

"""
"""
目标项目为camel-1.4
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_7 ant_1_5 ant_1_6
k=5时，取ant_1_7 ant_1_5 ant_1_6 ivy_1_1 jedit_4_3
k=10时，取ant_1_7 ant_1_5 ant_1_6 ivy_1_1 jedit_4_3 log4j_1_2 xalan_2_7 xalan_2_6 ant_1_4 log4j_1_1

"""
"""
目标项目为camel-1.6
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_1 ant_1_7 ant_1_5
k=5时，取ivy_1_1 ant_1_7 ant_1_5 jedit_4_3 log4j_1_2
k=10时，取ivy_1_1 ant_1_7 ant_1_5 jedit_4_3 log4j_1_2 ant_1_6 log4j_1_1 ant_1_4 tomcat xalan_2_7

"""
"""
目标项目为ivy-1.1
取欧式距离最近的k个其他版本项目
k=3时，取log4j_1_2 log4j_1_1 camel_1_4
k=5时，取log4j_1_2 log4j_1_1 camel_1_4 jedit_4_3 camel_1_6
k=10时，取log4j_1_2 log4j_1_1 camel_1_4 jedit_4_3 camel_1_6 camel_1_2 xalan_2_7 ant_1_5 xalan_2_6 ant_1_6

"""
"""
目标项目为ivy-1.4
取欧式距离最近的k个其他版本项目
k=3时，取camel_1_2 xalan_2_5 xalan_2_4
k=5时，取camel_1_2 xalan_2_5 xalan_2_4 ivy_1_1 log4j_1_2
k=10时，取camel_1_2 xalan_2_5 xalan_2_4 ivy_1_1 log4j_1_2 log4j_1_0 xalan_2_6 camel_1_0 xalan_2_7 lucene_2_0

"""
"""
目标项目为ivy-2.0
取欧式距离最近的k个其他版本项目
k=3时，取camel_1_2 log4j_1_0 log4j_1_2
k=5时，取camel_1_2 log4j_1_0 log4j_1_2 xalan_2_5 xalan_2_4
k=10时，取camel_1_2 log4j_1_0 log4j_1_2 xalan_2_5 xalan_2_4 lucene_2_4 lucene_2_0 camel_1_0 lucene_2_2 xalan_2_6

"""
"""
目标项目为jedit-3.2
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_3 ant_1_4 synapse_1_2
k=5时，取ant_1_3 ant_1_4 synapse_1_2 synapse_1_0 xerces_1_3
k=10时，取ant_1_3 ant_1_4 synapse_1_2 synapse_1_0 xerces_1_3 tomcat xerces_1_2 ant_1_6 velocity_1_5 ant_1_5

"""
"""
目标项目为jedit-4.0
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_3 ant_1_4 synapse_1_2
k=5时，取ant_1_3 ant_1_4 synapse_1_2 synapse_1_0 tomcat
k=10时，取ant_1_3 ant_1_4 synapse_1_2 synapse_1_0 tomcat ant_1_6 xerces_1_3 xerces_1_2 ant_1_5 ant_1_7

"""
"""
目标项目为jedit-4.1
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_4 ant_1_3 ant_1_6
k=5时，取ant_1_4 ant_1_3 ant_1_6 synapse_1_0 ant_1_5
k=10时，取ant_1_4 ant_1_3 ant_1_6 synapse_1_0 ant_1_5 ant_1_7 synapse_1_2 tomcat camel_1_4 log4j_1_1

"""
"""
目标项目为jedit-4.2
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_4 ant_1_3 ant_1_6
k=5时，取ant_1_4 ant_1_3 ant_1_6 synapse_1_0 ant_1_5
k=10时，取ant_1_4 ant_1_3 ant_1_6 synapse_1_0 ant_1_5 synapse_1_2 ant_1_7 tomcat log4j_1_1 camel_1_4

"""
"""
目标项目为jedit-4.3
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_4 ant_1_6 ant_1_5
k=5时，取ant_1_4 ant_1_6 ant_1_5 ant_1_7 log4j_1_2
k=10时，取ant_1_4 ant_1_6 ant_1_5 ant_1_7 log4j_1_2 ivy_1_1 synapse_1_0 camel_1_4 log4j_1_1 ant_1_3

"""

"""
目标项目为log4j-1.0
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_4 xalan_2_5 xalan_2_4
k=5时，取ivy_1_4 xalan_2_5 xalan_2_4 camel_1_2 ivy_2_0
k=10时，取ivy_1_4 xalan_2_5 xalan_2_4 camel_1_2 ivy_2_0 xalan_2_6 xalan_2_7 ivy_1_1 camel_1_0 ant_1_7

"""
"""
目标项目为log4j-1.1
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_1 jedit_4_3 ant_1_6
k=5时，取ivy_1_1 jedit_4_3 ant_1_6 ant_1_4 ant_1_7
k=10时，取ivy_1_1 jedit_4_3 ant_1_6 ant_1_4 ant_1_7 ant_1_5 camel_1_4 tomcat camel_1_6 xalan_2_7

"""
"""
目标项目为log4j-1.2
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_1 xalan_2_7 jedit_4_3
k=5时，取ivy_1_1 xalan_2_7 jedit_4_3 xalan_2_6 ant_1_6
k=10时，取ivy_1_1 xalan_2_7 jedit_4_3 xalan_2_6 ant_1_6 ant_1_5 ant_1_7 camel_1_4 camel_1_2 xalan_2_4

"""
"""
目标项目为lucene-2.0
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_4 xalan_2_5 xalan_2_4
k=5时，取ivy_1_4 xalan_2_5 xalan_2_4 ivy_2_0 camel_1_2
k=10时，取ivy_1_4 xalan_2_5 xalan_2_4 ivy_2_0 camel_1_2 log4j_1_0 camel_1_0 xalan_2_6 xalan_2_7 log4j_1_2

"""
"""
目标项目为lucene-2.2
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_4 xalan_2_5 xalan_2_4
k=5时，取ivy_1_4 xalan_2_5 xalan_2_4 ivy_2_0 camel_1_2
k=10时，取ivy_1_4 xalan_2_5 xalan_2_4 ivy_2_0 camel_1_2 camel_1_0 log4j_1_0 xalan_2_6 xalan_2_7 ivy_1_1

"""
"""
目标项目为lucene-2.4
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_4 ivy_2_0 xalan_2_5
k=5时，取ivy_1_4 ivy_2_0 xalan_2_5 xalan_2_4 log4j_1_0
k=10时，取ivy_1_4 ivy_2_0 xalan_2_5 xalan_2_4 log4j_1_0 camel_1_2 xalan_2_6 camel_1_0 xalan_2_7 ivy_1_1

"""
"""
目标项目为poi-1.5
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_4 velocity_1_5 xerces_1_3
k=5时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2
k=10时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2 jedit_4_0 velocity_1_6 jedit_4_2 jedit_4_1 xerces_1_4

"""
"""
目标项目为poi-2.0
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_4 velocity_1_5 xerces_1_3
k=5时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2
k=10时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2 jedit_4_0 velocity_1_6 jedit_4_2 jedit_4_1 xerces_1_4

"""
"""
目标项目为poi-2.5
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_4 velocity_1_5 xerces_1_3
k=5时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2
k=10时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2 jedit_4_0 velocity_1_6 jedit_4_2 jedit_4_1 xerces_1_4

"""
"""
目标项目为poi-3.0
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_4 velocity_1_5 xerces_1_3
k=5时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2
k=10时，取velocity_1_4 velocity_1_5 xerces_1_3 xerces_1_2 jedit_3_2 jedit_4_0 velocity_1_6 jedit_4_2 xerces_1_4 jedit_4_1

"""
"""
目标项目为synapse-1.0
取欧式距离最近的k个其他版本项目
k=3时，取jedit_4_3 ant_1_4 jedit_4_1
k=5时，取jedit_4_3 ant_1_4 jedit_4_1 jedit_4_2 ant_1_6
k=10时，取jedit_4_3 ant_1_4 jedit_4_1 jedit_4_2 ant_1_6 ant_1_5 ant_1_3 ant_1_7 log4j_1_1 log4j_1_2

"""
"""
目标项目为synapse-1.1
取欧式距离最近的k个其他版本项目
k=3时，取tomcat synapse_1_0 jedit_3_2
k=5时，取tomcat synapse_1_0 jedit_3_2 jedit_4_0 jedit_4_2
k=10时，取tomcat synapse_1_0 jedit_3_2 jedit_4_0 jedit_4_2 jedit_4_1 jedit_4_3 xerces_1_3 ant_1_4 log4j_1_1

"""
"""
目标项目为synapse-1.2
取欧式距离最近的k个其他版本项目
k=3时，取tomcat synapse_1_0 jedit_4_2
k=5时，取tomcat synapse_1_0 jedit_4_2 jedit_4_1 jedit_4_3
k=10时，取tomcat synapse_1_0 jedit_4_2 jedit_4_1 jedit_4_3 jedit_4_0 ant_1_4 jedit_3_2 log4j_1_1 ant_1_3

"""
"""
目标项目为tomcat
取欧式距离最近的k个其他版本项目
k=3时，取jedit_4_3 synapse_1_2 log4j_1_1
k=5时，取jedit_4_3 synapse_1_2 log4j_1_1 ivy_1_1 ant_1_4
k=10时，取jedit_4_3 synapse_1_2 log4j_1_1 ivy_1_1 ant_1_4 camel_1_6 jedit_4_2 log4j_1_2 jedit_4_1 camel_1_4

"""
"""
目标项目为velocity-1.4
取欧式距离最近的k个其他版本项目
k=3时，取poi_3_0 poi_2_5 xerces_1_3
k=5时，取poi_3_0 poi_2_5 xerces_1_3 xerces_1_2 jedit_3_2
k=10时，取 poi_3_0 poi_2_5 xerces_1_3 xerces_1_2 jedit_3_2 jedit_4_0 poi_1_5 xerces_1_4 jedit_4_2 jedit_4_1

"""
"""
目标项目为velocity-1.5
取欧式距离最近的k个其他版本项目
k=3时，取xerces_1_3 xerces_1_2 poi_3_0
k=5时，取xerces_1_3 xerces_1_2 poi_3_0 xerces_1_4 jedit_3_2
k=10时，取xerces_1_3 xerces_1_2 poi_3_0 xerces_1_4 jedit_3_2 jedit_4_0 jedit_4_2 jedit_4_1 ant_1_3 tomcat

"""
"""
目标项目为velocity-1.6
取欧式距离最近的k个其他版本项目
k=3时，取xerces_1_4 xerces_1_3 xerces_1_2
k=5时，取xerces_1_4 xerces_1_3 xerces_1_2 camel_1_6 camel_1_4
k=10时，取xerces_1_4 xerces_1_3 xerces_1_2 camel_1_6 camel_1_4 jedit_4_2 jedit_4_1 jedit_4_0 jedit_4_3 tomcat

"""

"""
目标项目为xalan-2.4
取欧式距离最近的k个其他版本项目
k=3时，取camel_1_2 ant_1_5 ivy_1_4
k=5时，取camel_1_2 ant_1_5 ivy_1_4 log4j_1_2 ant_1_7
k=10时，取camel_1_2 ant_1_5 ivy_1_4 log4j_1_2 ant_1_7 ant_1_6 camel_1_4 ivy_1_1 camel_1_0 log4j_1_0

"""
"""
目标项目为xalan-2.5
取欧式距离最近的k个其他版本项目
k=3时，取ivy_1_4 camel_1_2 ant_1_5
k=5时，取ivy_1_4 camel_1_2 ant_1_5 log4j_1_2 ant_1_7
k=10时，取ivy_1_4 camel_1_2 ant_1_5 log4j_1_2 ant_1_7 ant_1_6 camel_1_4 ivy_1_1 log4j_1_0 camel_1_0

"""
"""
目标项目为xalan-2.6
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_5 ant_1_6 log4j_1_2
k=5时，取ant_1_5 ant_1_6 log4j_1_2 ant_1_7 camel_1_2
k=10时，取ant_1_5 ant_1_6 log4j_1_2 ant_1_7 camel_1_2 camel_1_4 ivy_1_1 jedit_4_3 ivy_1_4 log4j_1_1

"""
"""
目标项目为xalan-2.7
取欧式距离最近的k个其他版本项目
k=3时，取ant_1_5 ant_1_6 ant_1_7
k=5时，取ant_1_5 ant_1_6 ant_1_7 log4j_1_2 camel_1_4
k=10时，取ant_1_5 ant_1_6 ant_1_7 log4j_1_2 camel_1_4 camel_1_2 jedit_4_3 ivy_1_1 ant_1_4 ivy_1_4

"""

"""
目标项目为xerces-1.2
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_5 velocity_1_6 jedit_4_0
k=5时，取velocity_1_5 velocity_1_6 jedit_4_0 jedit_3_2 tomcat
k=10时，取velocity_1_5 velocity_1_6 jedit_4_0 jedit_3_2 tomcat jedit_4_2 jedit_4_1 ant_1_4 poi_3_0 ant_1_3

"""
"""
目标项目为xerces-1.3
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_5 velocity_1_6 jedit_4_0
k=5时，取velocity_1_5 velocity_1_6 jedit_4_0 jedit_3_2 tomcat
k=10时，取velocity_1_5 velocity_1_6 jedit_4_0 jedit_3_2 tomcat jedit_4_2 jedit_4_1 ant_1_4 ant_1_3 poi_3_0

"""
"""
目标项目为xerces-1.4
取欧式距离最近的k个其他版本项目
k=3时，取velocity_1_6 tomcat ant_1_4
k=5时，取velocity_1_6 tomcat ant_1_4 camel_1_4 jedit_4_3
k=10时，取velocity_1_6 tomcat ant_1_4 camel_1_4 jedit_4_3 jedit_4_2 camel_1_6 ant_1_5 jedit_4_1 velocity_1_5

"""