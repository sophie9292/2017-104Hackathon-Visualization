# D3.js Example
使用bl.ocks.org的D3.js Bubble Chart[範例](https://bl.ocks.org/mbostock/4063269)，參賽者下載資料集後，將資料整理成相對應的格式，
```
python jobcat.py job_structured_info.csv job_category.csv
```
並將index.html中的flare.csv換成jobcat.csv，即可簡單地畫出Bubble Chart。
更多的範例可以參考D3 github上的gallery https://github.com/d3/d3/wiki/Gallery

* 使用說明:
	1. 在Mac或Linux中使用簡易的Python Simple Server
		```
		# python 2.x
		python -m SimpleHTTPServer 8888 &
		
		# python 3.x
		python -m http.server 8888 &
		```
	
	2. 在瀏覽器輸入localhost:8888 即可以看到範例的bubble chart	

![alt text](https://github.com/104corp/2017-104Hackathon-Visualization/blob/master/d3js-example/bubble-chart.png)
