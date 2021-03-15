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
      [Reference](https://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/vector/vector.h.htm)

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

#### 顺序查找

顺序查找操作假设向量中的元素类型定义了`==`运算符与`!=`运算符。

无序向量查找只需要从向量的开头依次对比向量中的元素与待查元素，当元素相同时返回即可。平均时间复杂度为$\mathcal O(n)$

#### 二分查找

有序向量的查找操作假设向量中的元素类型定义类`==`运算符、`!=`运算符，因此有序向量可以按照无序向量的查找方法线性查找。若有序向量的元素类型定义了比较运算符`<`与`>`，则基于比较的二分查找可以将时间复杂度降至$\mathcal O(\log n)$。

减而治之是二分查找的核心思想。考虑更一般的通用算法，对于长度为$n$的数组，在$\lambda \cdot n (0\leq \lambda\leq 1)$处设为轴点。每次比较当前待查区间的轴点$B$与待查元素$A$。每一次对轴点的比较有三种可能的结果，假设向量中的元素按照升序排序，则：

* $A<B$，表示待查元素只可能出现在轴点左侧，将待查区间缩小至左半部分，继续查找过程；
* $A=B$，表示轴点处出现待查元素，直接返回中点的下标即可；
* $B<A$，表示待查元素只可能出现在轴点右侧，将待查区间缩小至右半部分，继续查找过程。

对于二分查找，轴点为待查区间的中点，即$\lambda = 0.5$。

<center><svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="50%" viewBox="0 0 943.49 74.26"><rect width="73" height="73" rx="12.5" fill="#8cc63f"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(27.97 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">1</text><rect x="87.49" width="73" height="73" rx="12.5" fill="#8cc63f"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(115.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">2</text><rect x="174.49" width="73" height="73" rx="12.5" fill="#8cc63f"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(202.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="261" width="73" height="73" rx="12.5" fill="#8cc63f"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(288.97 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">4</text><rect x="348.49" width="73" height="73" rx="12.5" fill="#8cc63f"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(376.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="435.49" width="73" height="73" rx="12.5" fill="#f15a24"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(463.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">6</text><rect x="522" width="73" height="73" rx="12.5" fill="#0071bc"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(549.97 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">7</text><rect x="609.49" width="73" height="73" rx="12.5" fill="#0071bc"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(637.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="696.49" width="73" height="73" rx="12.5" fill="#0071bc"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(724.46 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">9</text><rect x="783" width="73" height="73" rx="12.5" fill="#0071bc"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(802.92 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">10</text><rect x="870.49" width="73" height="73" rx="12.5" fill="#0071bc"><animate attributeName="opacity" restart="whenNotActive" values="1;0;1" calcMode="spline" keySplines="0 0.5 1 1; 0 0 0.5 1" begin="click" dur="0.75s"/></rect><text transform="translate(890.41 45)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">11</text></svg></center>

但该版本的二分查找有多种意外情形，如：

1. 向量中找不到待查元素；
2. 向量中待查元素存在多个。

此时函数返回的结果不一定唯一。约定二分查找算法返回不大于待查元素的最后一个元素的位置。

二分查找通过尽可能减少递归深度的方式减少时间复杂度，由此，每一次递归的不同分支应有相同的期望时间消耗（即转向成本）。此处的“二分”只是在数组区间的意义上二等分，若对于如下条件语句：

```c
if (A > B)
    // statement
else if (A < B)
    // statement
else
    // statement
```

左右两个跳转位于不同的分支，需要进行比较的次数不同，因此所需的时间在严格意义上是不同的。可以通过改变轴点位置，将同一递归深度下比较的期望次数调整为相同，从而降低平均查找长度，在常系数程度上对算法进行优化。

<center><svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="65%" viewBox="0 0 709 205.32"><rect x="0.5" y="0.5" width="708" height="44" rx="11.71" fill="#8cc63f"/><path d="M696.79,1A11.22,11.22,0,0,1,708,12.21V32.79A11.22,11.22,0,0,1,696.79,44H12.21A11.22,11.22,0,0,1,1,32.79V12.21A11.22,11.22,0,0,1,12.21,1H696.79m0-1H12.21A12.21,12.21,0,0,0,0,12.21V32.79A12.21,12.21,0,0,0,12.21,45H696.79A12.21,12.21,0,0,0,709,32.79V12.21A12.21,12.21,0,0,0,696.79,0Z" fill="#8cc63f"/><rect y="146" width="380" height="45" rx="12.21" fill="#f15a24"/><rect x="399" y="146" width="310" height="45" rx="12.21" fill="#0071bc"/><path d="M369.52,45c.44,47.93-116.79,36.39-133.95,87.16" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="6"/><path d="M233.5,146.5c-1.4-7.13-4.29-16.17-8-22.08l10.6,5.91,11.93-2.24C242.71,132.53,237.09,140.18,233.5,146.5Z"/><path d="M370,45c0,53.15,164.61,42.48,192.12,88" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="6"/><path d="M566,147c-4.41-5.78-11-12.6-16.92-16.28l12.13.61,9.7-7.28C568.07,130.39,566.42,139.74,566,147Z"/><path d="M580,293" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="6"/><text transform="translate(224.38 95.92)" font-size="28" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">+1</text><text transform="translate(521.38 95.92)" font-size="28" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">+2</text><text transform="translate(345.83 31.16)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">n</text><text transform="translate(173.2 176)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">λn</text><text transform="translate(516.13 176)" font-size="28" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">(1 -λ<tspan x="58.32" y="0" letter-spacing="-0.25em">)·</tspan><tspan x="82.26" y="0">n</tspan></text></svg></center>

设算法的时间复杂度为$\alpha(\lambda) \log n$，则：

* 左侧子问题消耗的时间等于判断消耗的时间及解决子问题消耗的时间，即：$\lambda (1 + \alpha(\lambda)  \log (\lambda n))$
* 同理，右侧子问题的时间复杂度：$(1 - \lambda)(2+\alpha(\lambda)\log((1-\lambda)n))$

得$\alpha(\lambda) = \frac{\ln 2(\lambda - 2)}{\lambda \cdot\ln\lambda+(1-\lambda)\cdot\ln(1-\lambda)}$

当$\lambda=\frac{\sqrt 5-1}{2}\approx 0.618$时，$\alpha(\lambda)$取最小值。

消除不对称的另一种方式是将三种比较结果变为两种，从而一次比较即可进行划分。记待查元素为$A$，轴点为$B$，则：

* $A<B$：在轴点左侧的区间中查找
* $A\geq B$：在轴点右侧 **（包含轴点）** 的区间中查找
* 当区间长度缩减为1时，表示查找过程结束。

二分查找的最终实现代码如下所示：

??? 二分查找
      ```c++
      /******************************************************************************************
      * Data Structures in C++
      * ISBN: 7-302-33064-6 & 7-302-33065-3 & 7-302-29652-2 & 7-302-26883-3
      * Junhui DENG, deng@tsinghua.edu.cn
      * Computer Science & Technology, Tsinghua University
      * Copyright (c) 2003-2020. All rights reserved.
      ******************************************************************************************/

      // 二分查找算法（版本C）：在有序向量的区间[lo, hi)内查找元素e，0 <= lo <= hi <= _size
      template <typename T> static Rank binSearch ( T* S, T const& e, Rank lo, Rank hi ) {
         while ( lo < hi ) { //每步迭代仅需做一次比较判断，有两个分支
            Rank mi = ( lo + hi ) >> 1; //以中点为轴点（区间宽度的折半，等效于宽度之数值表示的右移）
            ( e < S[mi] ) ? hi = mi : lo = mi + 1; //经比较后确定深入[lo, mi)或(mi, hi)
         } //成功查找不能提前终止
         return lo - 1; //循环结束时，lo为大于e的元素的最小秩，故lo - 1即不大于e的元素的最大秩
      } //有多个命中元素时，总能保证返回秩最大者；查找失败时，能够返回失败的位置
      ```
      [Reference](https://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/vector/vector_search_binary_c.h.htm)

#### 插值查找

假设区间内元素分布的规律已知，根据待查元素在该分布中的位置推断待查元素在区间的位置，以此确定划分的轴点位置。

假设区间内元素服从独立的平均分布，则每次查找平均使得区间缩减至原来的$\sqrt n$，平均时间复杂度为$\mathcal O(\log\log n)$。

### 去重

对于有序向量，去重操作可以在线性时间复杂度内完成，无序向量去重的时间复杂度为$\mathcal O(n^2)$

#### 无序向量

使用指针标记无序向量已经完成去重的部分。对于无序向量未去重部分的每个元素，在未去重部分的后半部分中查找是否存在相同的元素，如果找到相同的元素则删除。完成查找后指针后移，将当前元素标记为已经完成去重。

#### 有序向量

使用双指针算法，一个指针$P$标记已去重部分的结尾，另一个指针$Q$标记未去重部分的开头，初始情况下，$P$位于向量第一个元素且$P+1=Q$。当$P$指向的对象与$Q$指向的对象相同时，$Q$递增而$P$不移动，否则将$Q$处的元素复制到$P+1$处，两指针同时递增。

<center>
<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="50%" viewBox="0 0 609.23 1288.83"><rect y="179.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(19.52 209.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="62.23" y="180" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(81.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="124.23" y="180" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(143.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="186.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(205.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="248.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(267.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="310.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(329.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="372.23" y="150" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(391.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="434.23" y="105" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(453.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="496.23" y="105" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(515.75 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="558.23" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(572.27 210.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><rect y="432.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(19.52 462.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="62.23" y="433" width="50" height="45" rx="13" fill="#919191"/><text transform="translate(81.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="124.23" y="433" width="50" height="45" rx="13" fill="#919191"/><text transform="translate(143.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="186.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(205.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="248.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(267.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="310.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(329.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="372.23" y="403" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(391.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="434.23" y="358" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(453.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="496.23" y="358" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(515.75 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="558.23" y="253" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(572.27 463.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><polygon points="25.48 239.94 10.73 265.49 40.23 265.49 25.48 239.94" fill="#474747"/><polygon points="87.48 239.94 72.73 265.49 102.23 265.49 87.48 239.94" fill="#474747"/><polygon points="19.48 488.94 4.73 514.49 34.23 514.49 19.48 488.94" fill="#474747"/><polygon points="211.48 488.94 196.73 514.49 226.23 514.49 211.48 488.94" fill="#474747"/><rect x="1" y="701.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(20.52 731.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="125.23" y="702" width="50" height="45" rx="13" fill="#919191"/><text transform="translate(144.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="187.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(206.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="63.23" y="672" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(82.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="249.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(268.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="311.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(330.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="373.23" y="672" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(392.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="435.23" y="627" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(454.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="497.23" y="627" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(516.75 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="559.23" y="522" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(573.27 732.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><polygon points="88.48 757.94 73.73 783.49 103.23 783.49 88.48 757.94" fill="#474747"/><polygon points="460.48 757.94 445.73 783.49 475.23 783.49 460.48 757.94" fill="#474747"/><rect y="970.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(19.52 1000.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="186.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(205.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="62.23" y="941" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(81.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="248.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(267.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="310.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(329.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="372.23" y="941" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(391.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="434.23" y="896" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(453.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="124.23" y="896" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(143.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="496.23" y="896" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(515.75 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="558.23" y="791" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(572.27 1001.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><polygon points="149.48 1026.94 134.73 1052.48 164.23 1052.48 149.48 1026.94" fill="#474747"/><polygon points="583.48 1026.94 568.73 1052.48 598.23 1052.48 583.48 1026.94" fill="#474747"/><rect x="1" y="1239.84" width="50" height="45" rx="13" fill="#56ff40"/><text transform="translate(20.52 1269.86)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><rect x="63.23" y="1210" width="50" height="75" rx="13" fill="#ffa640"/><text transform="translate(82.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="249.23" y="1210" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(268.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="311.23" y="1210" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(330.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="373.23" y="1210" width="50" height="75" rx="13" fill="#919191"/><text transform="translate(392.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><rect x="435.23" y="1165" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(454.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="125.23" y="1165" width="50" height="120" rx="13" fill="#ff40d2"/><text transform="translate(144.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="497.23" y="1165" width="50" height="120" rx="13" fill="#919191"/><text transform="translate(516.75 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">8</text><rect x="559.23" y="1060" width="50" height="225" rx="13" fill="#919191"/><text transform="translate(573.27 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text><rect x="187.23" y="1060" width="50" height="225" rx="13" fill="#5d40ff"/><text transform="translate(201.27 1270.02)" font-size="18" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">15</text></svg>
</center>

### 排序

此处介绍对向量的冒泡排序与归并排序，其他排序方式将在以后进行介绍。

#### 冒泡排序

对于数列$\{a_1, \cdots, a_n\}$，若$a_i>a_{i+1}$，称$(a_i, a_{i+1})$为一对逆序对。否则称为顺序对。则有序数列中不存在逆序对，无序数列中至少有一个逆序对。如果能够通过逆序对的交换使得数列中所有的逆序对转为顺序，即可完成对数组的排序。这是冒泡排序算法的核心思想。

> 0. 设向量（数组）长度为$n$，待排序区段下标为$[0,n)$
> 1. 每一次扫描待排序区段中的相邻数据，若为逆序对则交换之
>    * 扫描结束后，数组中的最大元素移动到待排序区段末尾，即为已排序
> 2. 一趟扫描后将待排序区段末尾元素划入已排序区段。
> 3. 重复扫描，直到待排序区段长度缩小为0，即完成排序。
> 
> 提前终止：若某次扫描过程中没有发生交换，说明待排序区段已经有序，可以提前结束算法

由于提前终止的存在，冒泡排序在最好情况下的时间复杂度为$\mathcal O(n)$，对应输入数据已经有序的情况。平均情况下冒泡排序的时间复杂度为$\mathcal O(n^2)$。

在冒泡排序中，相等的元素不被视为逆序对。如果将相等的元素视为逆序对，冒泡排序将失去稳定性。

#### 归并排序

归并排序采用分而治之的方法对数组进行排序，其核心思想是递归。归并排序的算法过程主要分为三步：

* “分”：将向量划分为两个（近似）等长的部分，时间复杂度为$\mathcal O(1)$
* “治”：对两部分分别进行归并排序（已知长度为$1$的向量是有序向量），时间复杂度为$2\times T(n/2)$
* “合”：将排序后的两部分合并为一个有序的整体，时间复杂度为$\mathcal O(n)$
* 算法整体的时间复杂度为$\mathcal O(n\log n)$，即使是在输入数组有序或接近有序的情况下。归并过程的空间复杂度为$\mathcal O(n)$

??? 归并排序
      ```c++
      template <typename T> void Vector<T>::mergeSort( Rank lo, Rank hi ) {
         if ( hi - lo < 2 ) return; //单元素区间自然有序，否则...
         int mi = (lo + hi) >> 1; //以中点为界
         mergeSort( lo, mi ); //对前半段排序
         mergeSort( mi, hi ); //对后半段排序
         merge( lo, mi, hi ); //归并
      }
      ```
      [Reference](https://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/vector/vector_mergesort.h.htm)

归并过程的核心思想即按顺序遍历两部分，将最小的写入目标数组中。

<center>
<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="60%" viewBox="0 0 708 256.5"><rect y="15" width="708" height="52" rx="11.79" fill="#8cc63f"/><rect y="187" width="455" height="52" rx="11.79" fill="#f15a24"/><rect x="456" y="187" width="252" height="52" rx="11.79" fill="#8cc63f"/><line x1="455.5" y1="256.5" x2="455.5" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="6"/><path d="M295.23,27.33h4.83l8.78,26.53h-4.43l-2.23-7.56H293l-2.27,7.56h-4.25ZM293.94,43h7.23l-1-3.57c-.9-2.87-1.69-5.83-2.48-8.81h-.18c-.76,3-1.59,5.94-2.45,8.81Z" fill="#fff"/><path d="M225.5,212.69c0-8.64,5.26-13.82,11.95-13.82a10.22,10.22,0,0,1,7.53,3.34l-2.27,2.67a7,7,0,0,0-5.18-2.38c-4.57,0-7.74,3.82-7.74,10s3,10.16,7.63,10.16a7.67,7.67,0,0,0,5.87-2.81l2.23,2.63a10.5,10.5,0,0,1-8.25,3.81C230.62,226.33,225.5,221.36,225.5,212.69Z" fill="#fff"/><path d="M585.94,199.33h8.21c5.44,0,9.36,1.77,9.36,6.56a5.88,5.88,0,0,1-3.78,5.72v.18a6.09,6.09,0,0,1,5.22,6.3c0,5.25-4.28,7.77-10.15,7.77h-8.86Zm7.74,11.09c4,0,5.73-1.51,5.73-4,0-2.78-1.88-3.82-5.62-3.82h-3.67v7.81Zm.65,12.17c4.14,0,6.52-1.48,6.52-4.72,0-3-2.31-4.32-6.52-4.32h-4.21v9Z" fill="#fff"/><rect x="286" y="192" width="41" height="41" rx="7.48" fill="#c1272d" stroke="#fff" stroke-miterlimit="10" stroke-width="2"/><rect x="499" y="192" width="41" height="41" rx="7.48" fill="#006837" stroke="#fff" stroke-miterlimit="10" stroke-width="2"/><rect x="333" y="20" width="41" height="41" rx="7.48" fill="#006837" stroke="#fff" stroke-miterlimit="10" stroke-width="2"/><path d="M305.08,204.55a1.72,1.72,0,1,1,1.71,1.65A1.59,1.59,0,0,1,305.08,204.55Zm.34,4.12h2.76v13.21h-2.76Z" fill="#fff"/><path d="M516.18,225.2l.5-2.06a4.49,4.49,0,0,0,1.2.22c1.23,0,1.56-.89,1.56-2.45V206.67h2.76v14.19c0,2.76-1.05,4.7-4,4.7A5.29,5.29,0,0,1,516.18,225.2Zm2.9-22.65a1.72,1.72,0,1,1,1.71,1.65A1.59,1.59,0,0,1,519.08,202.55Z" fill="#fff"/><path d="M348.42,30.75h2.71V43.06h.1l5.11-6.39h3.07L355,42.05l5,7.83h-3l-3.57-6-2.21,2.54v3.44h-2.71Z" fill="#fff"/><path d="M354,106.18c0,19.36-47.84,25.34-48.92,66.22" fill="#fff"/><path d="M354,106.18c0,16.86-36.27,23.57-46.36,52" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="3"/><path d="M308.71,155.17l7-2.48.09.24-6.18,9.33-4.58,10.14c0-3.71-.07-7.41-.1-11.12l-1.9-11,.15-.19Z"/><path d="M513.45,159.4c-29.75-29.45-159-36.33-159-53.4" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="3"/><path d="M511.13,157l-7.45-.38,0,.26,8.57,7.18,7.27,8.43-3.06-10.7-1.31-11.11-.2-.14Z"/><path d="M310.46,83.9h1.89l.18,1.55h.06A4.82,4.82,0,0,1,316,83.62a3,3,0,0,1,3.06,2,5.1,5.1,0,0,1,3.59-2c2.32,0,3.4,1.57,3.4,4.38v7h-2.31V88.29c0-1.91-.6-2.68-1.85-2.68a3.71,3.71,0,0,0-2.49,1.51V95h-2.31V88.29c0-1.91-.58-2.68-1.85-2.68a3.68,3.68,0,0,0-2.47,1.51V95h-2.31Z" fill="#ed1e79"/><path d="M329.11,80.45a1.32,1.32,0,0,1,1.42-1.37,1.38,1.38,0,1,1,0,2.75A1.32,1.32,0,0,1,329.11,80.45Zm.28,3.45h2.31V95h-2.31Z" fill="#ed1e79"/><path d="M335.16,83.9H337l.19,1.53h.06a5.27,5.27,0,0,1,3.65-1.81c2.35,0,3.4,1.57,3.4,4.38v7H342V88.29c0-1.91-.56-2.68-1.87-2.68-1,0-1.73.53-2.69,1.51V95h-2.31Z" fill="#ed1e79"/><path d="M347.74,88.67a18.91,18.91,0,0,1,3-10.27l1.45.62a19.65,19.65,0,0,0,0,19.29l-1.45.65A19,19,0,0,1,347.74,88.67Z" fill="#ed1e79"/><path d="M357,89.19l-3.31-5.29h2.49l1.32,2.22c.33.62.69,1.24,1.05,1.86h.08c.3-.62.62-1.24.92-1.86l1.17-2.22h2.41l-3.32,5.55L363.33,95h-2.51l-1.45-2.35c-.36-.65-.74-1.33-1.14-2h-.1c-.34.62-.69,1.28-1,2L355.82,95h-2.44Z" fill="#ed1e79"/><path d="M364.94,97.67a3.08,3.08,0,0,0,2.19-2.75.82.82,0,0,1-.22,0,1.45,1.45,0,0,1-1.55-1.49A1.51,1.51,0,0,1,367,92c1.13,0,1.79,1,1.79,2.5a4.72,4.72,0,0,1-3.3,4.52Z" fill="#ed1e79"/><path d="M375.25,99.36l.44-1.81a3,3,0,0,0,.81.16c1.2,0,1.9-.88,2.31-2.07l.22-.76-4.38-11H377l2.05,5.69c.32,1,.66,2.09,1,3.12h.1l.87-3.12,1.77-5.69h2.25L381,95.62c-.87,2.37-2,4-4.36,4A3.93,3.93,0,0,1,375.25,99.36Z" fill="#ed1e79"/><path d="M386.24,98.31a19.58,19.58,0,0,0,0-19.29l1.45-.62a19.17,19.17,0,0,1,0,20.56Z" fill="#ed1e79"/></svg></center>

实际执行过程中，只需将数组的前半部分复制一份，然后进行合并即可。

* 若前半部分提前结束，由于目标数组的后半部分与原数组的后半部分重合，目标数组自动成为有序
* 若后半部分提前结束，将前半部分剩余的数据复制到目标数组后半部分对应位置即可
  
如下图：

<center>
<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="80%" viewBox="0 0 913 579.5"><rect y="15" width="913" height="52" rx="11.79" fill="#8cc63f"/><rect y="187" width="455" height="52" rx="11.79" fill="#f15a24"/><rect x="456" y="187" width="457" height="52" rx="11.79" fill="#8cc63f"/><rect x="727" y="187" width="186" height="52" rx="11.79" fill="#009245"/><rect x="727" y="15" width="186" height="52" rx="11.79" fill="#009245"/><line x1="455.5" y1="256.5" x2="455.5" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="6"/><path d="M295.23,27.33h4.83l8.78,26.53h-4.43l-2.23-7.56H293l-2.27,7.56h-4.25ZM293.94,43h7.23l-1-3.57c-.9-2.87-1.69-5.83-2.48-8.81h-.18c-.76,3-1.59,5.94-2.45,8.81Z" fill="#fff"/><path d="M225.5,212.69c0-8.64,5.26-13.82,11.95-13.82a10.22,10.22,0,0,1,7.53,3.34l-2.27,2.67a7,7,0,0,0-5.18-2.38c-4.57,0-7.74,3.82-7.74,10s3,10.16,7.63,10.16a7.67,7.67,0,0,0,5.87-2.81l2.23,2.63a10.5,10.5,0,0,1-8.25,3.81C230.62,226.33,225.5,221.36,225.5,212.69Z" fill="#fff"/><path d="M585.94,199.33h8.21c5.44,0,9.36,1.77,9.36,6.56a5.88,5.88,0,0,1-3.78,5.72v.18a6.09,6.09,0,0,1,5.22,6.3c0,5.25-4.28,7.77-10.15,7.77h-8.86Zm7.74,11.09c4,0,5.73-1.51,5.73-4,0-2.78-1.88-3.82-5.62-3.82h-3.67v7.81Zm.65,12.17c4.14,0,6.52-1.48,6.52-4.72,0-3-2.31-4.32-6.52-4.32h-4.21v9Z" fill="#fff"/><line x1="820" y1="102.67" x2="820" y2="108.67" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="3"/><line x1="820" y1="118.54" x2="820" y2="153.07" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="3" stroke-dasharray="9.87 9.87"/><line x1="820" y1="158" x2="820" y2="164" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="3"/><path d="M820,105.91l6.49,3.94.14-.22-4.2-10.58L820,88l-2.43,11-4.2,10.58.11.22Z"/><rect y="338" width="913" height="52" rx="11.79" fill="#8cc63f"/><rect y="510" width="455" height="52" rx="11.79" fill="#f15a24"/><rect x="456" y="510" width="457" height="52" rx="11.79" fill="#8cc63f"/><rect x="269" y="510" width="186" height="52" rx="11.79" fill="#c1272d"/><rect x="727" y="338" width="186" height="52" rx="11.79" fill="#009245"/><line x1="455.5" y1="579.5" x2="455.5" y2="323" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="6"/><path d="M295.23,350.33h4.83l8.78,26.53h-4.43l-2.23-7.56H293l-2.27,7.56h-4.25ZM293.94,366h7.23l-1-3.57c-.9-2.87-1.69-5.83-2.48-8.81h-.18c-.76,3-1.59,5.94-2.45,8.81Z" fill="#fff"/><path d="M225.5,535.69c0-8.64,5.26-13.82,11.95-13.82a10.22,10.22,0,0,1,7.53,3.34l-2.27,2.67a7,7,0,0,0-5.18-2.38c-4.57,0-7.74,3.82-7.74,10s3,10.16,7.63,10.16a7.67,7.67,0,0,0,5.87-2.81l2.23,2.63a10.5,10.5,0,0,1-8.25,3.81C230.62,549.33,225.5,544.36,225.5,535.69Z" fill="#fff"/><path d="M585.94,522.33h8.21c5.44,0,9.36,1.77,9.36,6.56a5.88,5.88,0,0,1-3.78,5.72v.18a6.09,6.09,0,0,1,5.22,6.3c0,5.25-4.28,7.77-10.15,7.77h-8.86Zm7.74,11.09c4,0,5.73-1.51,5.73-4,0-2.78-1.88-3.82-5.62-3.82h-3.67v7.81Zm.65,12.17c4.14,0,6.52-1.48,6.52-4.72,0-3-2.31-4.32-6.52-4.32h-4.21v9Z" fill="#fff"/><path d="M362,499.27c36.22-51.14,352.84-48.66,417.91-80.66" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="3"/><path d="M777,420.14l-7.12-2.62.08-.25,10.89-3.3L791,409l-7.14,8.78-5.66,9.87-.25.05Z"/></svg></center>

若在归并过程中出现相同元素，左侧的元素优先归入目标数组，则可以保证归并排序的稳定性。

## 位图

位图是其中元素只能取0/1的向量。对于一个有限的整数集合$U$，位图构建了$U$的子集$S$，其中$k\in S$等价于位图中下标为$k$的元素的取值为$1$。位图提供了`set()`、`get()`、`clear()`三个接口，分别对应于位图的写入、查询、清除操作。

<center><svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="40%" viewBox="0 0 671 180.42"><rect width="671" height="76" rx="11.55" fill="#fbb03b"/><text transform="translate(297.9 49.85)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC"><tspan letter-spacing="-0.01em">b</tspan><tspan x="22.43" y="0">y</tspan><tspan x="42.01" y="0" letter-spacing="-0.02em">t</tspan><tspan x="55.66" y="0">e</tspan></text><rect y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(28.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">1</text><rect x="85" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(113.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">1</text><rect x="170" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(198.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">0</text><rect x="255" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(283.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">1</text><rect x="340" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(368.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">0</text><rect x="425" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(453.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">0</text><rect x="510" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(538.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">1</text><rect x="595" y="93" width="76" height="76" rx="11.55" fill="#8cc63f"/><text transform="translate(623.14 142.73)" font-size="36" fill="#fff" font-family="SourceHanSansSC-Medium-GBpc-EUC-H, Source Han Sans SC">1</text></svg></center>

基于位运算的实现如下：

??? 位图方法实现
      ```c++
      bool test( int k ) { return M[ k >> 3 ] & ( 0x80 >> (k & 0x07) ); }
      void set( int k ) { expand( k ); M[ k >> 3 ] |= ( 0x80 >> (k & 0x07) ); }
      void clear( int k ) { expand( k ); M[ k >> 3 ] &= ~( 0x80 >> (k & 0x07) ); }
      ```
      [Reference](https://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/bitmap/bitmap.h.htm)

读取字节中的某个位可以使用`&`运算符实现，向字节中设置某个位为$1$可以使用`|=`运算符实现。

位图的应用场景：

1. 整数数组去重操作，借助位图可以在$O(n)$时间复杂度内完成，同时也可以完成相应的排序操作。
2. 质数计算：Eratosthenes筛

### 快速初始化

在严格意义上讲，即使调用`memset()`函数，位图的初始化（清空）也需要$\mathcal O(n)$的时间。借助校验环结构可以将位图的初始化复杂度由$\mathcal O(n)$提高到$\mathcal O(1)$（但相应地，位图中的一个位需要两个`int`类型即64字节进行存储，造成空间的大量浪费）。

将位图的数组拆分为`A[]`、`B[]`两个数组，对于第`k`位，满足：

* `A[B[k]] = k`
* `B[A[k]] = k`

两个数组构成了相互校验的关系，按照下标查询，符合校验条件的下标存储的位为`1`，否则为`0`。

<center>
<svg id="图层_1" data-name="图层 1" xmlns="http://www.w3.org/2000/svg" width="40%" viewBox="0 0 606.87 435.2"><rect x="51.37" y="62.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M98.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H61.92a10.06,10.06,0,0,1-10.05-10.05V72.55a10.05,10.05,0,0,1,10.05-10H98.83m0-1H61.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05H98.83a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="122.37" y="62.01" width="58" height="58" rx="10.55" fill="#8cc63f"/><path d="M169.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H132.92a10.06,10.06,0,0,1-10-10.05V72.55a10.05,10.05,0,0,1,10-10h36.91m0-1H132.92a11,11,0,0,0-11,11v36.91a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="193.37" y="62.01" width="58" height="58" rx="10.55" fill="#8cc63f"/><path d="M240.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H203.92a10.06,10.06,0,0,1-10-10.05V72.55a10.05,10.05,0,0,1,10-10h36.91m0-1H203.92a11,11,0,0,0-11,11v36.91a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="264.37" y="62.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M311.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H274.92a10.06,10.06,0,0,1-10.05-10.05V72.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H274.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="335.37" y="62.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M382.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H345.92a10.06,10.06,0,0,1-10.05-10.05V72.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H345.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="406.37" y="62.01" width="58" height="58" rx="10.55" fill="#8cc63f"/><path d="M453.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H416.92a10.06,10.06,0,0,1-10.05-10.05V72.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H416.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="477.37" y="62.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M524.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H487.92a10.06,10.06,0,0,1-10.05-10.05V72.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H487.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="548.37" y="62.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M595.83,62.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H558.92a10.06,10.06,0,0,1-10-10.05V72.55a10.05,10.05,0,0,1,10-10h36.91m0-1H558.92a11,11,0,0,0-11,11v36.91a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V72.55a11,11,0,0,0-11-11Z"/><rect x="51.37" y="217.51" width="58" height="58" rx="10.55" fill="#fff"/><path d="M98.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H61.92A10.06,10.06,0,0,1,51.87,265V228.05a10.05,10.05,0,0,1,10.05-10H98.83m0-1H61.92a11,11,0,0,0-11.05,11V265A11.05,11.05,0,0,0,61.92,276H98.83a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="122.37" y="217.51" width="58" height="58" rx="10.55" fill="#8cc63f"/><path d="M169.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H132.92a10.06,10.06,0,0,1-10-10.05V228.05a10.05,10.05,0,0,1,10-10h36.91m0-1H132.92a11,11,0,0,0-11,11V265a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="193.37" y="217.51" width="58" height="58" rx="10.55" fill="#8cc63f"/><path d="M240.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H203.92a10.06,10.06,0,0,1-10-10.05V228.05a10.05,10.05,0,0,1,10-10h36.91m0-1H203.92a11,11,0,0,0-11,11V265a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="264.37" y="217.51" width="58" height="58" rx="10.55" fill="#fff"/><path d="M311.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H274.92A10.06,10.06,0,0,1,264.87,265V228.05a10.05,10.05,0,0,1,10.05-10h36.91m0-1H274.92a11,11,0,0,0-11.05,11V265A11.05,11.05,0,0,0,274.92,276h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="335.37" y="217.51" width="58" height="58" rx="10.55" fill="#fff"/><path d="M382.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H345.92A10.06,10.06,0,0,1,335.87,265V228.05a10.05,10.05,0,0,1,10.05-10h36.91m0-1H345.92a11,11,0,0,0-11.05,11V265A11.05,11.05,0,0,0,345.92,276h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="406.37" y="217.51" width="58" height="58" rx="10.55" fill="#8cc63f"/><path d="M453.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H416.92A10.06,10.06,0,0,1,406.87,265V228.05a10.05,10.05,0,0,1,10.05-10h36.91m0-1H416.92a11,11,0,0,0-11.05,11V265A11.05,11.05,0,0,0,416.92,276h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="477.37" y="217.51" width="58" height="58" rx="10.55" fill="#fff"/><path d="M524.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H487.92A10.06,10.06,0,0,1,477.87,265V228.05a10.05,10.05,0,0,1,10.05-10h36.91m0-1H487.92a11,11,0,0,0-11.05,11V265A11.05,11.05,0,0,0,487.92,276h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="548.37" y="217.51" width="58" height="58" rx="10.55" fill="#fff"/><path d="M595.83,218a10,10,0,0,1,10,10V265a10.05,10.05,0,0,1-10,10.05H558.92a10.06,10.06,0,0,1-10-10.05V228.05a10.05,10.05,0,0,1,10-10h36.91m0-1H558.92a11,11,0,0,0-11,11V265a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V228.05a11,11,0,0,0-11-11Z"/><rect x="51.37" y="373.01" width="58" height="58" rx="10.55" fill="#009245"/><path d="M98.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H61.92a10.06,10.06,0,0,1-10.05-10.05V383.55a10.05,10.05,0,0,1,10.05-10H98.83m0-1H61.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05H98.83a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="122.37" y="373.01" width="58" height="58" rx="10.55" fill="#009245"/><path d="M169.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H132.92a10.06,10.06,0,0,1-10-10.05V383.55a10.05,10.05,0,0,1,10-10h36.91m0-1H132.92a11,11,0,0,0-11,11v36.91a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="193.37" y="373.01" width="58" height="58" rx="10.55" fill="#009245"/><path d="M240.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H203.92a10.06,10.06,0,0,1-10-10.05V383.55a10.05,10.05,0,0,1,10-10h36.91m0-1H203.92a11,11,0,0,0-11,11v36.91a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="264.37" y="373.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M311.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H274.92a10.06,10.06,0,0,1-10.05-10.05V383.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H274.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="335.37" y="373.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M382.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H345.92a10.06,10.06,0,0,1-10.05-10.05V383.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H345.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="406.37" y="373.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M453.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H416.92a10.06,10.06,0,0,1-10.05-10.05V383.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H416.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="477.37" y="373.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M524.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H487.92a10.06,10.06,0,0,1-10.05-10.05V383.55a10.05,10.05,0,0,1,10.05-10h36.91m0-1H487.92a11,11,0,0,0-11.05,11v36.91a11.05,11.05,0,0,0,11.05,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><rect x="548.37" y="373.01" width="58" height="58" rx="10.55" fill="#fff"/><path d="M595.83,373.51a10,10,0,0,1,10,10v36.91a10.05,10.05,0,0,1-10,10.05H558.92a10.06,10.06,0,0,1-10-10.05V383.55a10.05,10.05,0,0,1,10-10h36.91m0-1H558.92a11,11,0,0,0-11,11v36.91a11.05,11.05,0,0,0,11,11.05h36.91a11,11,0,0,0,11-11.05V383.55a11,11,0,0,0-11-11Z"/><text transform="translate(73.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">0</text><text transform="translate(0.42 255.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">A</text><text transform="translate(0 410.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">B</text><text transform="translate(144.03 255.12)" font-size="24" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">0</text><text transform="translate(144.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">1</text><text transform="translate(73.03 410.12)" font-size="24" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">1</text><text transform="translate(215.03 410.12)" font-size="24" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">2</text><text transform="translate(144.03 410.12)" font-size="24" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><text transform="translate(428.03 255.12)" font-size="24" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">1</text><text transform="translate(215.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">2</text><text transform="translate(215.03 255.12)" font-size="24" fill="#fff" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">2</text><text transform="translate(286.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">3</text><text transform="translate(357.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">4</text><text transform="translate(428.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">5</text><text transform="translate(499.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">6</text><text transform="translate(570.03 21.12)" font-size="24" font-family="SourceHanSansSC-Heavy-GBpc-EUC-H, Source Han Sans SC">7</text><line x1="80.87" y1="372.51" x2="151.87" y2="276.51" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="2"/><line x1="151.87" y1="372.51" x2="435.87" y2="276.51" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="2"/><line x1="222.87" y1="372.51" x2="222.87" y2="276.51" fill="none" stroke="#000" stroke-miterlimit="10" stroke-width="2"/></svg></center>

双数组模式下，数组`B`为类似于栈的结构，从开头逐渐向后延伸，维护一个变量`top`记录`B`中元素的数量。数组`A`随机访问。

* `set(k)`：在数组`B`中追加一个值为`k`的元素，在`A[k]`中存储`B`中对应元素的下标；
* `get(k)`：若`B[A[k]] == k`且`A[k]`小于栈顶位置则为真，否则为假；
* `clear()`：清空数组`B`，即将`top`置`0`。
* `remove(k)`：先将`A-B`校验环中的最后一对（对应`B[top - 1]`）复制到`B[A[k]]`的位置，再`top--`删除最后一个元素。

“校验环”位图的实现：

??? 位图
      ```c++
      void set(int k)
      {
         A[k] = top;
         B[top++] = A[k];
      }
      int get(int k)
      {
         return B[A[k]] == k && A[k] < top;
      }
      void remove(int k)
      {
         A[B[--top]] = k;
         B[k] = B[top];
      }
      void clear(int k)
      {
         top = 0;
      }
      ```

## 列表

向量是静态的数据结构，一次只能分配固定长度的空间，向量的扩增需要分配一块新的空间，然后将向量中的元素复制到新的向量中。而列表与之不同，列表的元素可以动态分配，列表的扩增只需要分配扩增所需的空间即可。

列表中元素的排列与列表元素在内存中的排列顺序没有必然的关系，这些元素在逻辑上形成一个序列。列表的元素又称节点，相邻的节点互称前驱与后继。没有前驱的节点称为首节点，没有后继的节点称为尾节点。节点需要额外的空间记录相邻节点的地址以构建逻辑上的顺序关系。

这种方法的缺点在于列表中的元素不能直接按照下标进行访问，只能从列表的第一个节点开始，依序访问节点直到访问到对应下标的节点，时间复杂度为$\mathcal O(n)$

### 节点类型

为实现列表的各项操作，节点类型需要实现以下接口：

* 获取与设置当前节点的前驱
* 获取与设置当前节点的后继
* 获取与设置当前节点的取值
* 插入前驱节点
* 插入后继节点

**注意：** 双向链表在实现时有潜在的数据不一致的风险。（前驱节点的后继不等于后继节点的前驱）

如下提供了一个节点类的示例接口，没有包含接口的具体实现。

??? 列表节点类
      ```c++
      /******************************************************************************************
       * Data Structures in C++
       * ISBN: 7-302-33064-6 & 7-302-33065-3 & 7-302-29652-2 & 7-302-26883-3
       * Junhui DENG, deng@tsinghua.edu.cn
       * Computer Science & Technology, Tsinghua University
       * Copyright (c) 2003-2020. All rights reserved.
       ******************************************************************************************/
      
      typedef int Rank; //秩
      #define ListNodePosi(T) ListNode<T>* //列表节点位置
      
      template <typename T> struct ListNode { //列表节点模板类（以双向链表形式实现）
      // 成员
         T data; ListNodePosi(T) pred; ListNodePosi(T) succ; //数值、前驱、后继
      // 构造函数
         ListNode() {} //针对header和trailer的构造
         ListNode ( T e, ListNodePosi(T) p = NULL, ListNodePosi(T) s = NULL )
            : data ( e ), pred ( p ), succ ( s ) {} //默认构造器
      // 操作接口
         ListNodePosi(T) insertAsPred ( T const& e ); //紧靠当前节点之前插入新节点
         ListNodePosi(T) insertAsSucc ( T const& e ); //紧随当前节点之后插入新节点
      };
      ```
      [Reference](https://dsa.cs.tsinghua.edu.cn/~deng/ds/src_link/list/listnode.h.htm)

### 插入与删除

向列表中插入数据需要如下过程：

* 定位到节点
* 分配一个新的节点
* 更新节点之间的指针，将新节点与其他节点相连接

删除过程是插入过程的反向过程，更新节点之间指针，将删除节点排除在外即可。

### 查找与去重

无序列表的查找与去重操作与无序向量的查找与去重操作的基本思路相同，此处不再赘述。

有序列表的查找不能使用二分查找而只能顺序查找。

有序列表的去重：反复考察相邻的节点，若节点相同，则删除后边的节点，继续考察，否则当前节点向后移动，重复考察过程。直到列表到达结尾，算法结束。