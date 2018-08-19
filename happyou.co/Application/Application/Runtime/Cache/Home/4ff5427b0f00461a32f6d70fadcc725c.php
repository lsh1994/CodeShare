<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>首页</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/Public/pintuer/pintuer.css">
</head>

<body>
    <div id="page1">
        <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title-娜塔莎个人网站</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="/Public/pintuer/pintuer.css">
</head>
<body>
	<div class="container">
		<div class="container-layout padding-big-top padding-big-bottom">
			<div class="line">
				<div class="xl12 xs5 xm6 xb7">
					<button class="button icon-navicon float-right"
						data-target="#header-demo1"></button>
					<a href="#"> <img src="/Public/img/iconall.png" alt="娜塔莎个人网站" />
					</a>
				</div>
				<div class="xl12 xs7 xm6 xb5 padding-small-top">
					<ul class="nav nav-menu nav-inline nav-navicon" id="header-demo1">
						<li><a href="<?php echo U('Index/welcome');?>">首页</a></li>
						<li><a href="<?php echo U('Notes/articles');?>">轻笔记</a></li>
						<li><a href="<?php echo U('Gallery/show_img');?>">图库</a></li>
						<li><a href="<?php echo U('Articles/show_articles');?>">微文悦读</a></li>
						<li class=""><a href="">更多<span class="arrow"></span></a>
							<ul class="drop-menu">
								<li>
									
										<?php if($_SESSION['user']!= null): ?><a href="<?php echo U('User/about');?>"><span class="icon-user margin-right"></span><?php echo ($_SESSION['user']['username']); ?></a>
										<?php else: ?>
											<a href="<?php echo U('User/login');?>"><span class="icon-user margin-right"></span>未登录</a><?php endif; ?>
									
								</li>
								<?php if($_SESSION['user']!= null): ?><li><a href="<?php echo U('User/logout');?>">退出</a></li><?php endif; ?>
								
								
							</ul></li>
					</ul>
				</div>
			</div>
		</div>
	</div>
	<script src="/Public/pintuer/jquery.js"></script>
	<script src="/Public/pintuer/pintuer.js"></script>

</body>
</html>
    </div>

    <div class="container">
        <div class="panel">
            <div class="panel-head">
                <button class="button border-main" onclick="getHtml()">提交</button>
            </div>
            <div class="panel-body" style="padding: 0px">
                <textarea id="md_editor">
###Mditor是一个轻量级的markdown编辑器
![我的相片](/Public/img/me.jpg)
                </textarea>
            </div>
        </div>
        <form method="post" class="hidden" action="<?php echo U('Notes/upload_content');?>"  id="form1">
            <input name="content" id="content" type="text" value="">
        </form>

    </div>

    <div id="page2">
        <!DOCTYPE html>
<html lang="en">
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Title</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="/Public/pintuer/pintuer.css" rel="stylesheet" />
</head>
<body>
<div class="container-layout">
<div class="padding-top">
<div class="text-center">
<ul class="nav nav-inline">
	<li class="active"><a href="#">网站首页</a></li>
	<li><a href="#">新闻资讯</a></li>
	<li><a href="#">产品中心</a></li>
	<li><a href="#">技术反馈</a></li>
	<li><a href="#">留言反馈</a></li>
	<li><a href="#">联系方式</a></li>
</ul>
</div>

<div class="text-center height-big">版权所有 &copy; happyou.co&nbsp;All Rights Reserved，图ICP备：123456789</div>
</div>
</div>
<script src="/Public/pintuer/jquery.js"></script><script src="/Public/pintuer/pintuer.js"></script></body>
</html>
    </div>

    <script src="/Public/pintuer/jquery.js"></script>
    <script src="/Public/pintuer/pintuer.js"></script>
    <script type="text/javascript" src="/Public/mditor/mditor.js"></script>
    <script type="text/javascript">
        //获取textarea dom对象
        var ele_textarea = document.getElementById('md_editor');
        //实例化Mditor
        var editor = new mditor(ele_textarea, {
            //自定义显示效果class
            previewClass: 'article'
        });

        function getHtml(){
            $('#content').val(editor.getHtml());
            $('#form1').submit();
        }
    </script>
</body>

</html>