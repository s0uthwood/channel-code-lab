# channel-code-lab

作业备份项目，需配合作业中提供的测试程序使用

## (15,11)汉明码

### 推导过程

仿照实验指导的步骤进行推导

矩阵$H$为

$$
H=\left(\begin{matrix}
    1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1\\
    0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1\\
    0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1\\
\end{matrix}\right)
$$

将其变换为$H_s$

$$
H_s=\left(\begin{matrix}
    1 & 1 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 0\\
    1 & 0 & 1 & 1 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 1 & 0 & 0\\
    0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 & 0 & 1 & 0\\
    0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 1\\
\end{matrix}\right)
$$

由$G_2=(I_{15-4}|-A^T)$给出$G_s$

$$
G_s=\left(\begin{matrix}
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0\\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0\\
    0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 0\\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 1 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 1 & 1\\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1
\end{matrix}\right)
$$

进行列交换，得到$G$

$$
G_s=\left(\begin{matrix}
    1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    1 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    1 & 1 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0\\
    1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0\\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0\\
    1 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0\\
    1 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\
    0 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\
    1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{matrix}\right)
$$

`hamming_15_11_mat.py` 为用矩阵乘法实现的 (15, 11) 汉明码

> 程序的执行思路为：
>
> > 同时读入测试的输入数据和正确结果，将输入数据传入函数中，利用python的assert与结果进行解密，没有出现错误提示，说明其结果正确
>
> > 修改编码结果中的一位时，利用随机数生成器将某一位置的数字取反，然后再对其进行解码，最后同样使用assert进行比较

### 奇偶校验观点的构造

仿照实验指导，进行奇偶校验位的构造

1. 将 $1$ 到 $15$ 写成二进制的形式：$0001,0010,\ldots,1111$
2. 取 $1, 2, 4, 8$ 为奇偶校验位，其余为数据位
3. 得到传输比特串 $p_0p_1d_0p_2d_1d_2d_3p_3d_4d_5d_6d_7d_8d_9d_10$，将数据填入数据位，奇偶校验位填入0
4. 记录下所有1的位置，进行异或运算，得到的结果为 $p_3p_2p_1p_0$

`hamming_15_11_xor.py` 为优化后的 (15, 11) 汉明码编码与译码

## 比特错误检测

### OP4.2: (16,11)扩展汉明码实现

`hamming_16_11.py` 为扩展后的汉明码，该实现方式基于对指导书的理解

相较于(15,11)汉明码，进行如下修改：

1. 错误产生函数：可以随机产生两个不同的错误
2. 添加奇偶校验函数，偶数个1时返回`True`，奇数个时返回`False`
3. `encode` 时在末尾增加一个总奇偶校验位
4. `decode` 时按照指导书中的检错方式进行检错，同时可以指定错误个数为0,1,2，默认为0
5. 在未发生错误与发生一个错误时，对编码结果进行译码，并于正确的译码结果进行比较；在发生两个错误时，要求返回结果为`False`

>  其检错和纠错方法为：
>  
>  当前15位未检出错误时，直接返回正常译码后的结果
>  
>  当前15位检出错误时，对16位数据进行奇偶校验，若奇偶校验正确，说明出现了两个错误，只能检错，无法纠错，返回 `False`；若奇偶校验错误，说明出现了一个错误，可以进行纠错，返回纠错后结果

程序的校验同样采用了 `assert`，不发生错误和发生一次错误时，编码再解码后的结果需要与编码前相同，在发生两次错误时，编码再解码后需要返回False。

`hamming_16_11_method2.py` 是在查阅资料后，得知的一种实现方法

>  该方法为：
>
> 当前15位未检出错误时，直接返回正常译码后的结果
>
> 当前15位检出错误时，先对其进行纠错，对纠错结果进行正确编码，选取其总奇偶校验位，与原先的总奇偶校验位进行对比，若相同，则认为出现了一个错误，可以纠错，返回纠错结果；否则，认为出现了两个错误，只能检错，返回 `False`

## 突发错误信道

### 实现三个分组的比特交织的(15,11)汉明码

#### 源代码

- `hamming_std_encode_tri.py`
- `hamming_std_decode_tri.py`

> 在encode中，将原始01串进行编码后，进行比特交织，发送给模拟信道程序
> 在decode中，将接收到的01串进行比特交织的还原，然后进行解码，发送给验证程序生成图片

encode程序相较于基础版本，进行如下修改：

1. 接收到3组后再进行编码
2. 使用 `buf` 存储3组分别进行编码后的结果
3. 对3组进行比特交织，并输出

decode程序相较于基础版本，进行如下修改：

1. 接收到3组后再进行译码
2. 对3组读入数据进行比特交织的逆过程，并存储到 `buf` 中
3. 对3组数据分别进行译码，并输出

#### 测试结果

输入图片为：

![](./img/data.png)

输出图片为：

![](./img/result.png)