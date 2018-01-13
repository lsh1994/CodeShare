package dbtaobao;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;

import com.sun.javafx.collections.MappingChange.Map;

public class connDb {
	private static Connection con = null;
	private static Statement stmt = null;
	private static ResultSet rs = null;

	// �������ݿⷽ��
	public static void startConn() {
		try {
			Class.forName("com.mysql.jdbc.Driver");
			// �������ݿ��м��
			try {
				con = DriverManager.getConnection("jdbc:MySQL://192.168.221.128:3306/dbtaobao?useSSL=false", "root", "root");
			} catch (SQLException e) {
				e.printStackTrace();
			}
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	// �ر��������ݿⷽ��
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

	// ���ݿ�˫11 �������������Ϊ����
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

	// ��Ů��ҽ��׶Ա�
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

	// ��Ů��Ҹ�������ν��׶Ա�
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

	// ��ȡ����ǰ�����Ʒ���
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

	// ����ʡ�ݵ��ܳɽ����Ա�
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
	//��ͷ��Ԥ��
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
