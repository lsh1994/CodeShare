<?php
/**
 * Created by PhpStorm.
 * User: HelloSH
 * Date: 2018/1/2
 * Time: 11:14
 */
namespace Home\Controller;
use Think\Controller;
class UserController extends Controller {
    function loginVerify($username='',$password=''){
        $User=M("User");
        $condition['username']=$username;
        $condition['password']=$password;
        $condition['status']=1;
        // 读取数据
        $data = $User->where($condition)->find();
        if($data) {
            session('user',$data);
            $this->redirect('Index/index');
        }else{
            session('login_info',"用户名或密码错误或账号暂不能使用！");
            $this->redirect('User/login');
        }

    }
    function logout(){
        session(null);
        $this->redirect('Index/index');
    }

    function registerVerify($username='',$password='',$email=''){
        if(!$username or count($username)==0 or !$password or count($password)==0){
            session('register_info',"用户名或密码不能为空！");
            $this->redirect('User/register');
            return false;
        }
        $User=M("User");
        $condition['username']=$username;

        if(count($User->where($condition)->find())!=0){
            session('register_info',"用户名已经存在！");
            $this->redirect('User/register');
            return false;
        }
        $condition['password']=$password;
        $condition['email']=$email;
        $res=$User->add($condition);
        if($res) {
            $this->redirect('User/loginVerify',$condition);
        }else{
            $this->display('./Public/page/opt_wrong.html');
        }
    }
}