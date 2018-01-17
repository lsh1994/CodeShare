package lsh.util;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.sql.DataSource;

import com.mchange.v2.c3p0.ComboPooledDataSource;

public class DBHelper {
	private static DataSource dataSource = new ComboPooledDataSource();
	
	private static Connection conn = null;
	private static PreparedStatement ps = null;
	private static ResultSet rs = null;

	/**
	 * 数据查询
	 */
	public static List<Map<String, Object>> query(String sql) {
		Map<String, Object> hm = null;
		List<Map<String, Object>> list = null;
		try {
			list = new ArrayList<>();
			conn = dataSource.getConnection();
			ps = conn.prepareStatement(sql);
			rs = ps.executeQuery();
			ResultSetMetaData rsmd = rs.getMetaData();
			// 可以得到有多少列
			int columnNum = rsmd.getColumnCount();
			// 将数据封装到list中
			while (rs.next()) {
				hm = new HashMap<>(); 
				for (int i = 1; i <= columnNum; i++) {
					hm.put(rsmd.getColumnLabel(i), rs.getObject(i));
				}
				list.add(hm);
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
		return list;
	}

	/**
	 * 插入、修改数据操作
	 */
	public static int update(String sql) {
		int res=0;		
		try {
			conn = dataSource.getConnection();
			ps = conn.prepareStatement(sql);
			res = ps.executeUpdate();
			conn.close();
		} catch (Exception e) {
			// TODO: handle exception
			//e.printStackTrace();			
			res=-1;//0:操作失败，-1：数据库等异常，1,2,3...：操作成功
		}	
		
		return res;
	}
}
