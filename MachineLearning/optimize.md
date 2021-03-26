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


## 随机梯度下降

### Momentum 

s
### Adam


