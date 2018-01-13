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
						class="button bg-inverse bg-sub">男女买家各个年龄段交易对比</a></li>
						
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
						<span class="icon-database"></span>&nbsp;男女买家各个年龄段交易对比
					</div>
				</div>
				<div class="panel">
					<div class="panel-head">散点图</div>
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
<%Object[] objects=dataRefresh.getAgeSex();%>
$(function () {
    $('#container').highcharts({
        chart: {
            type: 'scatter',
            zoomType: 'xy'
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            title: {
                enabled: true,
                text: '年龄段'
            },
            startOnTick: true,
            endOnTick: true,
            showLastLabel: true
        },
        yAxis: {
            title: {
                text: '交易量'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'left',
            verticalAlign: 'top',
            x: 100,
            y: 20,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
            borderWidth: 1
        },
        credits: {
        	text: '',
        	href: ''
    	},
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{series.name}</b><br>',
                    pointFormat: '年龄段：{point.x} , 交易量：{point.y}'
                }               
            }
        },
        series: [{
            name: '女',
            color: 'rgba(223, 83, 83, .5)',
            data: <%=objects[0]%>
        }, {
            name: '男',
            color: 'rgba(119, 152, 191, .5)',
            data: <%=objects[1]%>
        }]
    });
});

	})
	</script>
</body>
</html>