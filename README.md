# IB-Index
Scrapes www.ibindex.se for current weights and returns the number of stocks to buy in order to follow the index.

IB-index follow Swedish investment companies on the Stockholm Stock Exchange. IB-index gives the companies an equal base weight which is often preferable compared to a market weighted index. The weighting is adjusted according to the Net Asset Value discount or premium,
a discount gives a company an increased weight in the index whereas a premium gives a reduced weight. 

What is the rationale behind that? 

As an example, if investment company A has a market cap of 100 million SEK and own stocks of the publicly traded company B for a value of 120 million SEK you would pay a lower price for the stock of company B by buying stocks of company A. The theory is that investment companies traded at a discount will outperform investment companies valued at a premium and that investment companies will outperform the market as a whole.

<img src="https://github.com/hataloo/IB-Index/blob/master/IBIndexShowcase/startpage.png" width="450">
<img src="https://github.com/hataloo/IB-Index/blob/master/IBIndexShowcase/valuation.png" width="500">

The above tables are downloaded with BeautifulSoup. By filling out how many stocks you currently own of each investment company and the amount you want to invest (perhaps a monthly investment), the following table is produced.

<img src="https://github.com/hataloo/IB-Index/blob/master/IBIndexShowcase/recommendation.png" width="700">

The table includes the number of stocks to buy (or sell) in order to best follow the index, how much each stock deviates from the index and how much of your invested money will remain.
