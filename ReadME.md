# 只针对中文分词进行研究

### 分词原理：

https://blog.csdn.net/chaoshine/article/details/89814869

---

### 规则分词包含:

    正向最大匹配（MM.py）
    逆向最大匹配（RMM.py）
    双向最大匹配（Bi-MM.py）

###### 词料内容包括:

    商务国际辞书编辑部，《现代汉语词典（实用版）》[M]，商务印书馆国际有限公司，2018年06月 | 字头和词目67000余个 （simplified.utf8）
    商务印书馆辞书研究中心，《古代汉语词典（第2版）》[M]，商务印书馆，2014年03月 | 单字14200个（包括繁体字和异体字），复音词28000条 （traditional.utf8）
    说词解字辞书研究中心，《成语大词典》[M]，华语教学出版社，2017年12月 | 收词20000余条 （idiom.utf8）

---

### 混合分词包含：

    支持向量机（SVM.py）
    隐马尔科夫模型（HMM.py）
    最大熵马尔科夫模型（MEMM.py）
    条件随机场（CRF.py）

---

Python Version [![v3.6.5](https://www.python.org/downloads/)]
