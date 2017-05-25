## **Frequentism and Bayesianism: A Python-driven Primer**

​										論文評論報告 104971001 林信甫


​	作者首先介紹Frequentist和Bayesian的分歧點在於”Probability”的定義上的不同，對於Frequentist來說，Probability是藉由重複觀測所得出的結果，在本質上相關於事件出現的頻率；Frequentist認為事件有***single truth***，觀測的結果為存在誤差的single truth，如果我們能搜集更多的觀測樣本即能更為逼近此single truth。而對於Bayesian來說Probability為對statements的degree of certainty，Bayesian不用single truth來表達certainty，而是藉由觀測到的資料，給出一個statement的可能機率P，以投擲錢幣例子來說，Bayesian觀測數字的投擲錢幣情形，然後根據這些data給出一個錢幣是否公平的機率。

​	作者以Photon flux舉例，問題為在不同的環境條件下給定一系列的觀測值，分別以frequentist和bayesian計算的方法嘗試估計true flux範圍，計算結果為兩者皆有相同的值999$\pm$4，此結果說明簡單的問題兩者可以得到相同的結果。

​	若考慮兩者處理nuisance parameters和uncertainty的不同，Frequentist和Bayesian則會產生差異，作者以Bayes' Biiliards Game解說nuisance parameter處理方法差異，Frequentist方法下，給定目前的觀測結果得出maximum likelihood probability後可計算出其中一方贏的比賽的機率約為18分之1；若以Bayesian方法計算， 忽視未知的機率p(unknown probability ball lands on one's side)，經過計算後得出相同一方獲勝的機率約為10分之1，作者提出經過程式模擬，Bayesian約為10分之1的機率為較正確的結果。此結果說明，Bayesian處理nuisance parameters的方法較為自然，不需要非常深入的統計專業也容易得出比Frequentist正確的結果。

​	另一比較的重點為Frequentist和Bayesian處理uncertainty哲學上的差異，frequentist常用"Confidence interval"，而bayesian則用"Credible regions"，以常用95%和parameter $\phi$其代表的意義分別為，frequentist: 重複執行實驗，95% confidence interval將包含true $\phi$, bayesian: 給定觀測資料，有95%機率true value $\phi$落在credible region內。兩種處理uncertainty的方法在某些情況下是重疊的，然而作者舉出Truncated Exponential的例子說明，若以Frequentist的方法計算，得到的結果與常識相違背，而以Bayesian的方法計算則得出的結果符合預期且正確，其原因為data為95%之外導致frequentist的方法產生相當大的誤差。作者提醒當使用**frequentist**時要注意此方法**回答的是不是我們所預期的問題**，且不能嘗試以Bayesian解讀以Frequentist建構的模型。

​	結語及心得：Frequentism和Bayesianism因如何定義"Probability"產生差異，在多數簡單的統計問題上，兩者會得到相似的結果，但若問題變得複雜，兩者常常會產生差異；相對於Frequentism，Bayesianism處理nuisance parameters方法較為自然，且以Bayesian的方式解釋科學結果較為直觀，作者強調只要我們能小心且正確的解讀結果，Frequentist和Bayesian都有其適用地方（但運用Frequentism解釋科學結果要更小心是否錯誤解讀）。









