<?php
/**
 * Created by PhpStorm.
 * User: lsh18
 * Date: 2018/1/15
 * Time: 20:03
 */

namespace Home\Controller;
use Think\Controller;
use Think\Page;
class NotesController extends Controller {

    function isLogin(){
        if (session('user'))
            return true;
        else
            $this->display("./Public/page/user_anthorize.html");
            return false;
    }

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

    function articles(){
        if(!$this->isLogin())
            return false;
        $Notes = M("Notes");
        $condition['user_id']=session('user')['id'];
        $condition['is_delete']=0;
        // 读取数据
        $count = $Notes->where($condition)->count();
        $p = $this->get_page($count, 3);
        $list = $Notes->where($condition)->order('create_time desc')->limit($p->firstRow, $p->listRows)->select();
        $this->assign('list', $list); // 赋值数据集
        $this->assign('page', $p->show()); // 赋值分页输出
        $this->display();
    }

    function upload_content($content=''){
        $Notes = M("Notes");
        $condition['user_id'] = session('user')['id'];
        $condition['content'] = $content;
        $res=$Notes->data($condition)->add();
        if($res){
            $this->redirect('Notes/articles');
        }else{
            $this->display('./Public/page/opt_wrong.html');
        }
    }
    function delete($id=''){
        $Notes = M("Notes"); // 实例化User对象
        $condition['id'] = $id;
        $condition['user_id'] = session('user')['id'];
//        $res=$Notes->where($condition)->delete();
        $condition['is_delete']=1;
        $res=$Notes->save($condition);
        if($res){
            $this->redirect('Notes/articles');
        }else{
            $this->display('./Public/page/opt_wrong.html');
        }
    }
}