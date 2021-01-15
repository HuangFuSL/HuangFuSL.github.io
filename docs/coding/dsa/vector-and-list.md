# 向量与列表

主要的基础线性数据结构是向量与列表。在本合集中，向量指以数组方式组合并封装通用抽象接口的数据类型；列表指以链表方式组合并封装通用抽象接口的数据类型。

较为高级的数据结构——栈与队列建立在向量与列表的基础上。提供了一些受限制的操作接口。

## 线性数据结构

对于基础的线性数据结构，以下的接口可以视为通用：

| 操作         | 描述                               | 通用性                 |
| ------------ | ---------------------------------- | ---------------------- |
| `size()`     | 获取对象中元素的数目               |                        |
| `get()`      | 获取对象中某个元素的值             |                        |
| `set()`      | 修改对象中某个元素的值             |                        |
| `insert()`   | 向对象中的某个位置插入元素         |                        |
| `remove()`   | 移除对象中的某个元素               |                        |
| `traverse()` | 遍历对象中的所有元素，并执行某操作 |                        |
| `find()`     | 在对象中查找某个元素的位置         |                        |
| `search()`   | 在有序的结构中查找某个元素的位置   | 要求有序               |
| `sort()`     | 排序对象中的元素                   | 要求重载`<`和`>`运算符 |

## 向量

在向量中，数据在内存中连续存储，即下标相邻的数据在内存中相邻。C/C++语言中的数组数据结构可以视为简单的向量。但数组不提供插入、删除等具体的操作接口，需要在程序代码中手动实现。将数组封装成类可以提供更多的操作接口，并且保证数据被合法地访问及修改。

向量是数组的抽象泛化、支持所有数组的功能，对于不同类型的元素提供了统一的操作接口。

C++提供了模板类的功能用来针对不同类型的元素提供相同的功能。对于某个ADT（以向量为例），其属性和接口的组织方式可遵循如下规则：

```c++
template <typename T> class Vector { //向量模板类
private: Rank _size; int _capacity; T* _elem; //规模、容量、数据区
protected:
/* ... 内部函数 */
public:
/* ... 构造函数 */
/* ... 析构函数 */
/* ... 只读接口 */
/* ... 可写接口 */
/* ... 遍历接口 */
};
```

通过对`[]`运算符进行重载，向量和列表支持数组风格的访问方式。

具体代码可以参见：

??? 向量模板类声明
    ```c++
    /******************************************************************************************
     * Data Structures in C++
     * ISBN: 7-302-33064-6 & 7-302-33065-3 & 7-302-29652-2 & 7-302-26883-3
     * Junhui DENG, deng@tsinghua.edu.cn
     * Computer Science & Technology, Tsinghua University
     * Copyright (c) 2003-2020. All rights reserved.
     ******************************************************************************************/
    
    typedef int Rank; //秩
    #define DEFAULT_CAPACITY  3 //默认的初始容量（实际应用中可设置为更大）
    
    template <typename T> class Vector { //向量模板类
    protected:
       Rank _size; int _capacity;  T* _elem; //规模、容量、数据区
       void copyFrom ( T const* A, Rank lo, Rank hi ); //复制数组区间A[lo, hi)
       void expand(); //空间不足时扩容
       void shrink(); //装填因子过小时压缩
       bool bubble ( Rank lo, Rank hi ); //扫描交换
       void bubbleSort ( Rank lo, Rank hi ); //起泡排序算法
       Rank max ( Rank lo, Rank hi ); //选取最大元素
       void selectionSort ( Rank lo, Rank hi ); //选择排序算法
       void merge ( Rank lo, Rank mi, Rank hi ); //归并算法
       void mergeSort ( Rank lo, Rank hi ); //归并排序算法
       void heapSort ( Rank lo, Rank hi ); //堆排序（稍后结合完全堆讲解）
       Rank partition ( Rank lo, Rank hi ); //轴点构造算法
       void quickSort ( Rank lo, Rank hi ); //快速排序算法
       void shellSort ( Rank lo, Rank hi ); //希尔排序算法
    public:
    // 构造函数
       Vector ( int c = DEFAULT_CAPACITY, int s = 0, T v = 0 ) //容量为c、规模为s、所有元素初始为v
       { _elem = new T[_capacity = c]; for ( _size = 0; _size < s; _elem[_size++] = v ); } //s<=c
       Vector ( T const* A, Rank n ) { copyFrom ( A, 0, n ); } //数组整体复制
       Vector ( T const* A, Rank lo, Rank hi ) { copyFrom ( A, lo, hi ); } //区间
       Vector ( Vector<T> const& V ) { copyFrom ( V._elem, 0, V._size ); } //向量整体复制
       Vector ( Vector<T> const& V, Rank lo, Rank hi ) { copyFrom ( V._elem, lo, hi ); } //区间
    // 析构函数
       ~Vector() { delete [] _elem; } //释放内部空间
    // 只读访问接口
       Rank size() const { return _size; } //规模
       bool empty() const { return !_size; } //判空
       Rank find ( T const& e ) const { return find ( e, 0, _size ); } //无序向量整体查找
       Rank find ( T const& e, Rank lo, Rank hi ) const; //无序向量区间查找
       Rank search ( T const& e ) const //有序向量整体查找
       { return ( 0 >= _size ) ? -1 : search ( e, 0, _size ); }
       Rank search ( T const& e, Rank lo, Rank hi ) const; //有序向量区间查找
    // 可写访问接口
       T& operator[] ( Rank r ); //重载下标操作符，可以类似于数组形式引用各元素
       const T& operator[] ( Rank r ) const; //仅限于做右值的重载版本
       Vector<T> & operator= ( Vector<T> const& ); //重载赋值操作符，以便直接克隆向量
       T remove ( Rank r ); //删除秩为r的元素
       int remove ( Rank lo, Rank hi ); //删除秩在区间[lo, hi)之内的元素
       Rank insert ( Rank r, T const& e ); //插入元素
       Rank insert ( T const& e ) { return insert ( _size, e ); } //默认作为末元素插入
       void sort ( Rank lo, Rank hi ); //对[lo, hi)排序
       void sort() { sort ( 0, _size ); } //整体排序
       void unsort ( Rank lo, Rank hi ); //对[lo, hi)置乱
       void unsort() { unsort ( 0, _size ); } //整体置乱
       int deduplicate(); //无序去重
       int uniquify(); //有序去重
    // 遍历
       void traverse ( void (* ) ( T& ) ); //遍历（使用函数指针，只读或局部性修改）
       template <typename VST> void traverse ( VST& ); //遍历（使用函数对象，可全局性修改）
    }; //Vector
    ```

### 插入

向量的插入操作分为三步：

1. 检查向量空间与输入下标的合法性，必要时改变向量的长度以容纳该元素
2. 当输入下标不是向量的末尾时，移动向量中的元素，在对应位置腾出空间
3. 将数据写入向量中

在长度为$n$的向量中的随机位置插入一个元素，改变向量长度所需的时间为$\mathcal O(n)$，移动元素以腾出空间的期望时间复杂度为$\mathcal O(n)$，写入数据的时间复杂度为$\mathcal O(1)$，总的时间复杂度为$\mathcal O(n)$

#### 可扩充向量

向量的空间是有限的（即为向量本身的长度），若当向量空间不足时为向量重新分配一块更长的内存，将原数据复制到新的内存空间中以实现容量的扩增，则向量的空间可以近似视为无限。一般存在两种扩充算法：

* 当向量空间不足时，向量空间增加一个常量$I$
* 当向量空间不足时，向量空间乘以一定倍数$k$（通常情况下，$k=2$）

对于初始长度为$0$的向量，考察插入$n\gg 2$个元素下两种扩充算法的调用次数。递增策略下插入第$mI+1, (m\in \mathbb N)$个元素时需要进行扩充，总的调用次数为$\frac{n}{I}$，即$\mathcal O(n)$。倍增策略下插入第$1, 2, 3, 5\dots 2^m+1, (m\in \mathbb N)$个元素时需要进行扩充，总的调用次数为$\mathcal O(\log n)$。

复制数据的时间复杂度为$\mathcal O(n)$，因此递增策略每次扩容所需的时间为$0, I, 2I, \dots$，共需要扩容$\frac nI$次，扩容操作的总时间复杂度为$\mathcal O(n^2)$。每次插入操作分摊$\mathcal O(n)$。倍增策略每次扩容所需的时间为$0, 1, 2, \dots n$，共需要扩容$\log n$次。扩容操作的总时间复杂度为$\mathcal O(n)$，每次插入操作分摊$\mathcal O(1)$。

但倍增策略会导致更多的空间浪费，具体表现为向量的装载因子较低。插入大量元素时，倍增策略的装载因子只能保证$> 50$，而递增策略的装载因子可以保证在$1$左右。

### 删除

向量的删除操作主要为区间删除与单个元素的删除。其中后者可以视为前者的特殊情况。删除操作不需要执行额外的操作，只需要将删除区间后的元素向前移动，覆盖删除区间内的数据并更新操作结束后向量的长度即可。对于可扩充向量，删除后应对向量的装填因子进行检查，在必要时收缩向量。

> 如果多次调用删除单个元素的接口实现区间删除，由于每次删除都会导致一次数据的移动，总的时间复杂度为$\mathcal O(n^2)$

删除操作需要对删除位置的合法性进行检验。

### 查找

无序向量与有序向量的查找方法不同，所需的时间复杂度也不同。具体而言，有序向量的顺序提供了额外的信息，从而使得有序向量中的查找操作能够在$\log n$的时间复杂度内完成。

#### 无序向量

对于无序向量，查找操作假设向量中的元素类型定义了`==`运算符与`!=`运算符。

无序向量查找只需要从向量的开头依次对比向量中的元素与待查元素，当元素相同时返回即可。平均时间复杂度为$\mathcal O(n)$

#### 有序向量

有序向量的查找操作假设向量中的元素类型定义类`==`运算符、`!=`运算符，因此有序向量可以按照无序向量的查找方法线性查找。若有序向量的元素类型定义了比较运算符`<`与`>`，则基于比较的二分查找可以将时间复杂度降至$\mathcal O(\log n)$。

二分查找的核心思想是减而治之。考虑更一般的通用算法，对于长度为$n$的数组，在$\lambda \cdot n (0\leq \lambda\leq 1)$处设为轴点。每次比较当前待查区间的轴点$B$与待查元素$A$。比较有三种可能的结果，假设向量中的元素按照升序排序，则：

* $A<B$，表示待查元素只可能出现在轴点左侧，将待查区间缩小至左半部分，继续查找过程；
* $A=B$，表示轴点处出现待查元素，直接返回中点的下标即可；
* $B<A$，表示待查元素只可能出现在轴点右侧，将待查区间缩小至右半部分，继续查找过程。

对于二分查找，轴点为待查区间的中点，即$\lambda = 0.5$。

<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 943.49 74.26"><rect width="73" height="73" rx="12.5" fill="#80ff75"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(27.97 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">1</text><rect x="87.49" width="73" height="73" rx="12.5" fill="#80ff75"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(115.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">2</text><rect x="174.49" width="73" height="73" rx="12.5" fill="#80ff75"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(202.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="261" width="73" height="73" rx="12.5" fill="#80ff75"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(288.97 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">4</text><rect x="348.49" width="73" height="73" rx="12.5" fill="#80ff75"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(376.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="435.49" width="73" height="73" rx="12.5" fill="#ffbf75"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(463.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">6</text><rect x="522" width="73" height="73" rx="12.5" fill="#759aff"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(549.97 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">7</text><rect x="609.49" width="73" height="73" rx="12.5" fill="#759aff"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(637.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="696.49" width="73" height="73" rx="12.5" fill="#759aff"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(724.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">9</text><rect x="783" width="73" height="73" rx="12.5" fill="#759aff"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(802.92 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">10</text><rect x="870.49" width="73" height="73" rx="12.5" fill="#759aff"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(890.41 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">11</text></svg>

但二分查找有多种意外情形，如：

1. 向量中找不到待查元素，返回特殊值表示找不到元素，也可以返回在该元素在向量中的预期位置；
2. 向量中待查元素存在多个，此时应当返回待查元素首次出现的下标。

二分查找通过尽可能减少递归深度的方式减少时间复杂度，由此，每一次递归的不同分支应有相同的期望时间消耗（即转向成本）。此处的“二分”只是在数组区间的意义上二等分，若对于如下条件语句：

```c
if (A > B)
    // statement
else if (A < B)
    // statement
else
    // statement
```

左右两个跳转位于不同的分支，需要进行比较的次数不同，因此所需的时间在严格意义上是不同的。可以通过改变轴点位置，将同一递归深度下比较的期望次数调整为相同。从而降低平均查找长度。

### 去重

对于有序向量，去重操作可以在线性时间复杂度内完成，无序向量去重的时间复杂度为$\mathcal O(n^2)$

#### 无序向量

使用指针标记无序向量已经完成去重的部分。对于无序向量未去重部分的每个元素，在未去重部分的后半部分中查找是否存在相同的元素，如果找到相同的元素则删除。完成查找后指针后移，将当前元素标记为已经完成去重。

#### 有序向量

使用双指针算法，一个指针$P$标记已去重部分的结尾，另一个指针$Q$标记未去重部分的开头，初始情况下，$P$位于向量第一个元素且$P+1=Q$。当$P$指向的对象与$Q$指向的对象相同时，$Q$递增而$P$不移动，否则将$Q$处的元素复制到$P+1$处，两指针同时递增。

<center>
<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="50%" viewBox="0 0 609.23 1288.83"><rect y="179.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(19.52 209.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="62.23" y="180" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(81.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="124.23" y="180" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(143.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="186.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(205.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="248.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(267.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="310.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(329.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="372.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(391.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="434.23" y="105" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(453.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="496.23" y="105" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(515.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="558.23" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(572.27 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><rect y="432.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(19.52 462.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="62.23" y="433" width="50" height="45" rx="13" fill="#919191"/><text transform="translate(81.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="124.23" y="433" width="50" height="45" rx="13" fill="#919191"/><text transform="translate(143.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="186.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(205.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="248.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(267.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="310.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(329.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="372.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(391.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="434.23" y="358" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(453.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="496.23" y="358" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(515.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="558.23" y="253" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(572.27 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><polygon points="25.48 239.94 10.73 265.49 40.23 265.49 25.48 239.94" fill="#474747"/><polygon points="87.48 239.94 72.73 265.49 102.23 265.49 87.48 239.94" fill="#474747"/><polygon points="19.48 488.94 4.73 514.49 34.23 514.49 19.48 488.94" fill="#474747"/><polygon points="211.48 488.94 196.73 514.49 226.23 514.49 211.48 488.94" fill="#474747"/><rect x="1" y="701.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(20.52 731.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="125.23" y="702" width="50" height="45" rx="13" fill="#919191"/><text transform="translate(144.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="187.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(206.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="63.23" y="672" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(82.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="249.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(268.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="311.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(330.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="373.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(392.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="435.23" y="627" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(454.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="497.23" y="627" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(516.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="559.23" y="522" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(573.27 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><polygon points="88.48 757.94 73.73 783.49 103.23 783.49 88.48 757.94" fill="#474747"/><polygon points="460.48 757.94 445.73 783.49 475.23 783.49 460.48 757.94" fill="#474747"/><rect y="970.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(19.52 1000.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="186.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(205.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="62.23" y="941" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(81.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="248.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(267.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="310.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(329.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="372.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(391.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="434.23" y="896" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(453.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="124.23" y="896" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(143.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="496.23" y="896" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(515.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="558.23" y="791" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(572.27 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><polygon points="149.48 1026.94 134.73 1052.48 164.23 1052.48 149.48 1026.94" fill="#474747"/><polygon points="583.48 1026.94 568.73 1052.48 598.23 1052.48 583.48 1026.94" fill="#474747"/><rect x="1" y="1239.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(20.52 1269.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="63.23" y="1210" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(82.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="249.23" y="1210" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(268.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="311.23" y="1210" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(330.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="373.23" y="1210" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(392.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="435.23" y="1165" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(454.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="125.23" y="1165" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(144.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="497.23" y="1165" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(516.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="559.23" y="1060" width="50" height="225" rx="13" fill="#919191"/><text transform="translate(573.27 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><rect x="187.23" y="1060" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(201.27 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text></svg>
</center>
