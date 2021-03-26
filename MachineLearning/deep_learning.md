# Deep learning


## Batch Normalization
批量归一化是针对每一批数据，在网络的每一层输入之前增加归一化处理：
$$ \hat{x}^k = \frac{x^k - E[x^k]}{\sqrt{Var[x^k]}}$$

$x^k$ 为该层第k个神经元的原始输入数据。

归一化虽可对数据分布进行额外约束，增加模型泛化能力，但同时也降低了模型的拟合能力，归一化之后的输入分布被强制为0均值和1标准差，破坏了之前学习到的特征分布。为了恢复原始数据分布，实现中引入了变换重构以及可学习的参数$\gamma , \beta$:

$$ y^k = \gamma^k \hat{x}^k + \beta^k$$

若不采用批量归一化，则分布变换依赖于前面网络学习到的连接权重。而在批量归一化操作中，只需用两个参数就可以恢复最优输入数据分布，与之前的网络层参数解耦，更加利于优化过程。

完整的批量归一化 前向传导公式为：
$$ \mu = \frac{1}{n}\sum_i^n x_i$$
$$ \sigma^2  = \frac{1}{n}\sum_i^n(x_i-\mu)^2$$
$$ \hat{x}_i = \frac{x_i-\mu}{\sqrt{\sigma^2+\epsilon}}$$
$$ y_i = BN_{\gamma,\beta}(x_i) = \gamma \hat{x}_i + \beta $$

## Attention 


## Activation function


## Optimizer