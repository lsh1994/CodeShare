<?php
/**
 * Created by PhpStorm.
 * User: lsh18
 * Date: 2018/1/22
 * Time: 17:20
 */
namespace Home\Controller;
use Think\Controller;
use Think\Page;
class ArticlesController extends Controller {
    function get_page($count, $pagesize = 10) {
        $p = new Page($count, $pagesize);
        $p->setConfig('header', '<li class="rows">共<b>%TOTAL_ROW%</b>条记录&nbsp;第<b>%NOW_PAGE%</b>页/共<b>%TOTAL_PAGE%</b>页</li>');
        $p->setConfig('prev', '上一页');
        $p->setConfig('next', '下一页');
        $p->setConfig('last', '末页');
        $p->setConfig('first', '首页');
        $p->setConfig('theme', '%FIRST%%UP_PAGE%%LINK_PAGE%%DOWN_PAGE%%END%%HEADER%');
        $p->lastSuffix = false;//最后一页不显示为总页数
        return $p;
    }
    function show_articles()
    {
        $news = M("Articles");
        $count = $news->where(1)->count();
        $p = $this->get_page($count, 6);
        $list = $news->where(1)->order('id desc')->limit($p->firstRow, $p->listRows)->select();
        $this->assign('list', $list); // 赋值数据集
        $this->assign('page', $p->show()); // 赋值分页输出
        $this->display();
    }
}