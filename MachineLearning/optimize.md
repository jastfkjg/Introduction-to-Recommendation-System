# 优化方法

无约束优化问题的优化算法：
1. 直接法
2. 迭代法

## 直接法

能够直接给出优化问题最优解的方法。
但要求目标函数 1. 是凸函数 2. 函数导数为0有解。

如：岭回归(Ridge Regression):
$$ L(\theta) = ||X\theta - y||^2 + \lambda ||\theta||^2 $$
通过数学推导可得到最优解：
$$ \theta^\star = (X^TX+\lambda I)^{-1}X^Ty $$

## 迭代法

迭代法又分为**一阶法**和**二阶法**。

### 一阶法 

一阶法 也称梯度下降法。
一阶法对目标函数做一阶泰勒展开，得到近似式：
$$L(\theta_t + \epsilon) = L(\theta_t) + \triangledown L(\theta_t)^T \epsilon $$ 
$\epsilon$ 需要足够小才准确，因此求解时通常会加上L2正则项：
$$ \epsilon = argmin_{\epsilon}(L(\theta_t) + \triangledown L(\theta_t)^T \epsilon + \frac{1}{2\alpha}||\epsilon||^2) $$
因此，迭代公式为：
$$ \theta_{t+1} = \theta_t - \alpha \triangledown L(\theta_t) $$


### 二阶法
二阶法对目标函数做二阶泰勒展开，得到近似式：
$$L(\theta_t + \epsilon) = L(\theta_t) + \triangledown L(\theta_t)^T \epsilon + \frac{1}{2}\epsilon^T\triangledown^2L(\theta_t)\epsilon $$

得到二阶法对迭代公式：
$$ \theta_{t+1} = \theta_t - \triangledown^2L(\theta_t)^{-1}\triangledown L(\theta_t) $$

二阶法也称 **牛顿法**，二阶法的收敛速度要远快于一阶法。但在高维情况下，二阶法的Hessian矩阵求逆计算复杂度很高，且当目标函数非凸时，二阶法可能会收敛到鞍点。


# 深度学习中常用优化方法：

## SGD

$$ \theta_{t+1}=\theta_t - \alpha g_t$$

- 山谷：在两山壁间来回反弹。
- 鞍点（一个方向两头翘，另一方向两头垂）：停在鞍点。

## Momentum 

$$ v_t = \gamma v_{t-1} + \alpha g_t$$
$$ \theta_{t+1} = \theta_t - v_t $$

每一步更新由两部分组成，一是学习速率乘以当前梯度，二是带衰减的前一次更新步长。惯性就体现在第二部分。

收敛速度相比SGD更快，收敛曲线更稳定。

## Adagrad 
更新频率低的参数可以拥有较大的更新步幅，而更新频率高的参数步幅可以减小。AdaGrad利用历史梯度平方和来衡量不同参数的梯度和稀疏性。
$$ \theta_{t+1,i} = \theta_{t,i} - \frac{\alpha}{\sqrt{\sum_{k=0}^t g_{k,i}^2 + \epsilon}} g_{t,i}$$

## Adam

$$ m_t = \beta_1 m_{t-1} + (1-\beta_1)g_t $$
$$ v_t = \beta_2 v_{t-1} + (1-\beta_2)g_t^2$$
$$ \theta_{t+1} = \theta_t - \frac{\alpha \hat{m}_t}{\sqrt{\hat{v}_t + \epsilon}}$$

With $\hat{m}_t = \frac{m_t}{1-\beta_1^t}$, $\hat{v}_t=\frac{v_t}{1-\beta_2^t}$

## FTRL

迭代和选取模型的时候我们经常希望得到更加稀疏的模型，这不仅仅起到了特征选择的作用，也降低了预测计算的复杂度。

L1正则化在大规模在线机器学习算法中好像无法起到参数稀疏化的作用：在梯度下降算法下，L1正则化通常能得到更加稀疏的解；可是在SGD算法下模型迭代并不是沿着全局梯度下降，而是沿着某个样本的梯度进行下降，这样即使是L1正则也不一定能得到稀疏解。

一些稀疏解的优化方法：
### 1. Truncated Gradient
https://zr9558.com/2016/01/12/truncated-gradient/

### 2. FOBOS
https://zr9558.com/2016/01/12/forward-backward-splitting-fobos/

### 3. RDA 
https://zr9558.com/2016/01/12/regularized-dual-averaging-algorithm-rda/

### FTRL





