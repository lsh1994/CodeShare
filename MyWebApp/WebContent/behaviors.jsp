<%@page import="java.util.List"%>
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
						class="button bg-sub bg-inverse">所有买家消费行为比例</a></li>
					<li class="margin-bottom"><a href=""
						class="button border-sub">男女买家交易对比</a></li>
					<li class="margin-bottom"><a href="ageSex.jsp"
						class="button border-sub">男女买家各个年龄段交易对比</a></li>
					<li class="margin-bottom"><a href="saleTopFive.jsp"
						class="button border-sub">获取销量前五的商品类别</a></li>
					<li class="margin-bottom"><a href="citySales.jsp"
						class="button border-sub">各个省份的总成交量对比</a></li>
					<li class="margin-bottom"><a href="repeatPredict.jsp"
						class="button border-sub">回头客预测分数对比</a></li>
				</ul>
			</div>
			<div class="xs9 padding">
				<div class="panel margin-bottom">
					<div class="panel-head bg-main">
						<span class="icon-database"></span>&nbsp;所有买家消费行为比例
					</div>
				</div>
				<div class="panel">
					<div class="panel-head">饼图</div>
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
	<script src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>
	<script type="text/javascript">
		
	<%String list = dataRefresh.getBehaviors();%>
		$(function() {
			$('#container')
					.highcharts(
							{
								chart : {
									plotBackgroundColor : null,
									plotBorderWidth : null,
									plotShadow : false
								},
								title : {
									text : ''
								},
								tooltip : {
									headerFormat : '{series.name}<br>',
									pointFormat : '{point.name}: <b>{point.percentage:.1f}%</b>'
								},
								credits: {
					            	text: '',
					            	href: ''
					        	},
								plotOptions : {
									pie : {
										allowPointSelect : true,
										cursor : 'pointer',
										dataLabels : {
											enabled : true,
											format : '<b>{point.name}</b>: {point.percentage:.1f} %',
											style : {
												color : (Highcharts.theme && Highcharts.theme.contrastTextColor)
														|| 'black'
											}
										},
										states : {
											hover : {
												enabled : false
											}
										},
										slicedOffset : 20, // 突出间距
										point : { // 每个扇区是数据点对象，所以事件应该写在 point 下面
											events : {
												// 鼠标滑过是，突出当前扇区
												mouseOver : function() {
													this.slice();
												},
												// 鼠标移出时，收回突出显示
												mouseOut : function() {
													this.slice();
												},
												// 默认是点击突出，这里屏蔽掉
												click : function() {
													return false;
												}
											}
										}
									}
								},
								series : [ {
									type : 'pie',
									name : '买家消费行为占比',
									data :<%=dataRefresh.getBehaviors()%>
								} ]
							})
		});
	</script>
</body>
</html>