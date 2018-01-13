<%@page import="action.dataRefresh"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>大数据实验结果可视化</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="Res/pintuer/pintuer.css">
</head>
<body>
	<div class="container">
		<h1 class="text-center margin">大数据实验结果可视化</h1>
		<div class="line">
			<div class="xs3 padding">
				<button class="button icon-navicon" data-target="#nav-link1"></button>
				<ul class="nav nav-navicon text-center" id="nav-link1">
					<li class="margin-bottom"><a href="behaviors.jsp"
						class="button border-sub">所有买家消费行为比例</a></li>
						
					<li class="margin-bottom"><a href=""
						class="button border-sub">男女买家交易对比</a></li>
						
					<li class="margin-bottom"><a href="ageSex.jsp"
						class="button border-sub">男女买家各个年龄段交易对比</a></li>
						
					<li class="margin-bottom"><a href="saleTopFive.jsp"
						class="button bg-inverse bg-sub">获取销量前五的商品类别</a></li>
						
					<li class="margin-bottom"><a href="citySales.jsp"
						class="button border-sub">各个省份的总成交量对比</a></li>
						
					<li class="margin-bottom"><a href="repeatPredict.jsp"
						class="button border-sub">回头客预测分数对比</a></li>
				</ul>
			</div>
			<div class="xs9 padding">
				<div class="panel margin-bottom">
					<div class="panel-head bg-main">
						<span class="icon-database"></span>&nbsp;获取销量前五的商品类别
					</div>
				</div>
				<div class="panel">
					<div class="panel-head">柱状图</div>
					<div class="panel-body">
						<div id="container"
							style="width: 100%; max-width: 600px; height: 400px; margin: auto;"></div>
					</div>
				</div>

			</div>

		</div>
	</div>
	<script src="Res/pintuer/jquery.js"></script>
	<script src="Res/pintuer/pintuer.js"></script>

	<script src="https://img.hcharts.cn/highmaps/highmaps.js"></script>
	<script src="https://data.jianshukeji.com/geochina/china.js"></script>
	<script>
	$(function () {
<%Object[] objects=dataRefresh.getSaleTopFive();%>
		Highcharts.chart('container', {
		    chart: {
		        type: 'column',
		    },
		    title: {
	            text: ''
	        },
	        yAxis: {
	            title: {
	                text: '交易量'
	            }
	        },
	        xAxis: {
	            title: {
	            	enabled: true,
	                text: '商品ID'
	            }
	        },
		    xAxis: {
		        categories: <%= objects[0]%>
		    },
		    credits: {
	        	text: '',
	        	href: ''
	    	},
		    plotOptions: {
		        series: {
		            borderRadius: 5
		        }
		    },

		    series: [{
		    	name: 'Top5商品',
		        data: <%= objects[1]%>
		    }]
		});
	})
	</script>
</body>
</html>