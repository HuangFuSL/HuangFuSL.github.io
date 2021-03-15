# LaTeX 数学公式

收集$\LaTeX$常用的数学公式命令

## 字母变体

常用命令有：`\mathcal`、`\mathbb`、`\mathfrak`、`\mathsf`、`\mathbf`、`\boldsymbol`、`\mathit`、`\mathrm`等。其中`\mathcal`、`\mathbb`仅适用于大写字母，其余命令大写、小写字母通用

* `\mathcal{A}`：$\mathcal A$
* `\mathbb{A}`：$\mathbb A$
* `\mathfrak{A}`：$\mathfrak A$
* `\mathsf{A}`：$\mathsf A$
* `\mathbf{A}`：$\mathbf A$
* `\boldsymbol{A}`：$\boldsymbol A$
* `\mathit{A}`：$\mathit A$（无效果）
* `\mathrm{A}`：$\mathrm A$
* `\mathscr{A}`：$\mathscr A$（需要引入宏包`mathrsfs`）

## 希腊字母

|小写|命令|大写|命令|变体|命令|
|:-:|:-:|:-:|:-:|:-:|:-:|
|$\alpha$|`\alpha`|$A$|`A`|
|$\beta$|`\beta`|$B$|`B`|
|$\gamma$|`\gamma`|$\Gamma$|`\Gamma`|$\varGamma$|`\varGamma`|
|$\delta$|`\delta`|$\Delta$|`\Delta`|$\varDelta$|`\varDelta`|
|$\epsilon$|`\epsilonn`|$E$|`E`|$\varepsilon$|`\varepsilon`|
|$\zeta$|`\zeta`|$Z$|`Z`|
|$\eta$|`\eta`|$H$|`H`|
|$\theta$|`\theta`|$\Theta$|`\Theta`|$\vartheta,\varTheta$|`\vartheta,\varTheta`|
|$\iota$|`\iota`|$I$|`I`|
|$\kappa$|`\kappa`|$K$|`K`|$\varkappa$|`\varkappa`|
|$\lambda$|`\lambda`|$\Lambda$|`\Lambda`|$\varLambda$|`\varLambda`|
|$\mu$|`\mu`|$M$|`M`|
|$\nu$|`\nu`|$N$|`N`|
|$\xi$|`\xi`|$\Xi$|`\Xi`|$\varXi$|`\varXi`|
|$o$|`o`|$O$|`O`|
|$\pi$|`\pi`|$\Pi$|`\Pi`|$\varpi, \varPi$|`\varpi,\varPi`|
|$\rho$|`\rho`|$P$|`P`|$\varrho$|`\varrho`|
|$\sigma$|`\sigma`|$\Sigma$|`\Sigma`|$\varsigma, \varSigma$|`\varsigma,\varSigma`|
|$\tau$|`\tau`|$T$|`T`|
|$\upsilon$|`\upsilon`|$\Upsilon$|`\Upsilon`|$\varUpsilon$|`\varUpsilon`|
|$\phi$|`\phi`|$\Phi$|`\Phi`|$\varphi, \varPhi$|`\varphi,\varPhi`|
|$\chi$|`\chi`|$X$|`X`|
|$\psi$|`\psi`|$\Psi$|`\Psi`|$\varPsi$|`\varPsi`|
|$\omega$|`\omega`|$\Omega$|`\Omega`|$\varOmega$|`\varOmega`|

## 运算符

常见运算符列于下表：

### 数学运算


|运算符|命令|
|:---:|:-:|
|$\times$|`\times`|
|$\div$|`\div`|
|$\odot$|`\odot`|
|$\oplus$|`\oplus`|
|$\otimes$|`\otimes`|

### 集合运算

|运算符|命令|
|:---:|:-:|
|$\in$|`\in`|
|$\ni$|`\ni`|
|$\subset$|`\subset`|
|$\subseteq$|`\subseteq`|
|$\subseteqq$|`\oplsubseteqqu`|
|$\subsetneq$|`\subsetneq`|
|$\subsetneqq$|`\subsetneqq`|
|$\supset$|`\subset`|
|$\supseteq$|`\subseteq`|
|$\supseteqq$|`\oplsubseteqqu`|
|$\supsetneq$|`\subsetneq`|
|$\supsetneqq$|`\subsetneqq`|
|$\cap$|`\cap`|
|$\cup$|`\cup`|

### 关系运算符

|运算符|命令|
|:---:|:-:|
|$\geq$|`\geq`|
|$\geqq$|`\geqq`|
|$\geqslant$|`\geqslant`|
|$\gg$|`\gg`|
|$\ggg$|`\ggg`|
|$\leq$|`\leq`|
|$\leqq$|`\leqq`|
|$\leqslant$|`\leqslant`|
|$\ll$|`\ll`|
|$\lll$|`\lll`|
|$\sim$|`\sim`|
|$\approx$|`\approx`|

### 逻辑运算符

|运算符|命令|
|:---:|:-:|
|$\lnot$|`\lnot`|
|$\land$|`\land`|
|$\lor$|`\lor`|
|$\forall$|`\forall`|
|$\exists$|`\exists`|

### 函数与复杂运算

|运算符|命令|
|:---:|:-:|
|$\frac ab$|`\frac{a}{b}`|
|$\sum_i^n f$|`\sum_{i}^{n} f`|
|$\prod_i^n f$|`\prod_{i}^{n} f`|
|$\sqrt[x]{y}$|`\sqrt[x]{y}`|
|$\int_a^bf(x)\mathrm dx$|`\int_a^bf(x)\mathrm dx`|
|$\oint_Df(x)\mathrm dx$|`\oint_Df(x)\mathrm dx`|
|$\iint_Df(x)\mathrm dx$|`\iint_Df(x)\mathrm dx`|
|$\iiint_Df(x)\mathrm dx$|`\iiint_Df(x)\mathrm dx`|
|$\partial$|`\partial`|
|$\log$|`\log`|
|$\ln$|`\ln`|
|$\lg$|`\lg`|
|$\exp$|`\exp`|
|$a\mod b$|`a\mod b`|
|$\max$|`\max`|
|$\min$|`\min`|
|$\arg$|`\arg`|
|$\sin$|`\sin`|
|$\cos$|`\cos`|
|$\tan$|`\tan`|
|$\cot$|`\cot`|
|$\sinh$|`\sinh`|
|$\cosh$|`\cosh`|
|$\tanh$|`\tanh`|
|$\coth$|`\coth`|
|$\arcsin$|`\arcsin`|
|$\arccos$|`\arccos`|
|$\arctan$|`\arctan`|
|$\ker$|`\ker`|
|$\dim$|`\dim`|
|$\det$|`\det`|
|$\lim$|`\lim`|
|$\inf$|`\inf`|

## 括号

|运算符|命令|
|:---:|:-:|
|$\{$|`\{`|
|$\}$|`\}`|
|$\langle$|`\langle`|
|$\rangle$|`\rangle`|
|$\lceil$|`\lceil`|
|$\rceil$|`\rceil`|
|$\lfloor$|`\lfloor`|
|$\rfloor$|`\rfloor`|
|$\|$|`\|`|