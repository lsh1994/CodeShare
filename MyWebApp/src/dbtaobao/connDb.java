package dbtaobao;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;

import com.sun.javafx.collections.MappingChange.Map;

public class connDb {
	private static Connection con = null;
	private static Statement stmt = null;
	private static ResultSet rs = null;

	// 连接数据库方法
	public static void startConn() {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			// 连接数据库中间件
			try {
				con = DriverManager.getConnection("jdbc:MySQL://192.168.221.128:3306/dbtaobao?useSSL=false", "root", "root");
			} catch (SQLException e) {
				e.printStackTrace();
			}
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	// 关闭连接数据库方法
	public static void endConn() throws SQLException {
		if (con != null) {
			con.close();
			con = null;
		}
		if (rs != null) {
			rs.close();
			rs = null;
		}
		if (stmt != null) {
			stmt.close();
			stmt = null;
		}
	}

	// 数据库双11 所有买家消费行为比例
	public static HashMap<String, Integer> index() throws SQLException {
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		startConn();
		stmt = con.createStatement();
		rs = stmt.executeQuery("select action,count(*) num from user_log group by action desc");
		while (rs.next()) {		
			map.put(rs.getString("action"), rs.getInt("num") );
		}
		endConn();	
		return map;
	}

	// 男女买家交易对比
	public static ArrayList<String[]> index_1() throws SQLException {
		ArrayList<String[]> list = new ArrayList<>();
		startConn();
		stmt = con.createStatement();
		rs = stmt.executeQuery("select gender,count(*) num from user_log group by gender desc");
		while (rs.next()) {
			String[] temp = { rs.getString("gender"), rs.getString("num") };
			list.add(temp);
		}
		endConn();
		return list;
	}

	// 男女买家各个年龄段交易对比
	public static ArrayList<String[]> index_2() throws SQLException {
		ArrayList<String[]> list = new ArrayList<>();
		startConn();
		stmt = con.createStatement();
		rs = stmt.executeQuery("select gender,age_range,count(*) num from user_log group by gender,age_range desc");
		while (rs.next()) {
			String[] temp = { rs.getString("gender"), rs.getString("age_range"), rs.getString("num") };
			list.add(temp);
		}
		endConn();
		return list;
	}

	// 获取销量前五的商品类别
	public static HashMap<String, Integer> index_3() throws SQLException {
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		startConn();
		stmt = con.createStatement();
		rs = stmt.executeQuery(
				"select cat_id,count(*) num from user_log group by cat_id order by count(*) desc limit 5");
		while (rs.next()) {			
			map.put(rs.getString("cat_id"), rs.getInt("num"));
		}
		endConn();
		return map;
	}

	// 各个省份的总成交量对比
	public static HashMap<String, Integer> index_4() throws SQLException {
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		startConn();
		stmt = con.createStatement();
		rs = stmt.executeQuery("select province,count(*) num from user_log group by province order by count(*) desc");
		while (rs.next()) {
			map.put(rs.getString("province"), rs.getInt("num"));
		}
		endConn();
		return map;
	}
	//回头客预测
	public static ArrayList<Double> rPredict() throws SQLException {
		ArrayList<Double> list=new ArrayList<>();
		startConn();
		stmt = con.createStatement();
		rs = stmt.executeQuery("select score from rebuy limit 100");
		while (rs.next()) {
			list.add(rs.getDouble("score"));
		}
		endConn();
		return list;
	}
}
