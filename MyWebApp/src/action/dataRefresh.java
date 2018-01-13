package action;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import dbtaobao.connDb;

public class dataRefresh {
	public static String getBehaviors() throws JSONException, SQLException {
		HashMap<String, Integer> map = null;
		map = connDb.index();	
		map.put("点击",map.remove("0"));
		map.put("加入购物车",map.remove("1"));
		map.put("购买",map.remove("2"));
		map.put("关注商品",map.remove("3"));
		List<Object[]> list=new ArrayList<>();
		for (Entry<String, Integer> entry : map.entrySet()) {
			Object[] strings= {entry.getKey(),entry.getValue()};
			list.add(strings);
		}
		
		JSONArray jsonArray=new JSONArray(list);
//		System.out.println(jsonArray.toString());
		return jsonArray.toString();
//		return list;
	}
	public static String getCitySales() throws SQLException, JSONException {
		HashMap<String, Integer> map=connDb.index_4();	
		map.put("重庆",map.remove("重庆市"));
		map.put("上海",map.remove("上海市"));
		map.put("北京",map.remove("北京市"));
		map.put("天津",map.remove("天津市"));
		JSONObject object=null;
		JSONArray array=new JSONArray();
		for (Entry<String, Integer> entry : map.entrySet()) {
			object=new JSONObject();
			object.put("name", entry.getKey());
			object.put("value", entry.getValue());
			array.put(object);
		}
		return array.toString();
//		System.out.println(array.toString());
//		
//		return null;
	}
	
	public static Object[] getSaleTopFive() throws JSONException, SQLException {
		HashMap<String, Integer> map = null;
		map = connDb.index_3();	
			
		ArrayList<String> keys= new ArrayList<>();
		ArrayList<Integer> values=new ArrayList<>();
		for (Entry<String, Integer> entry : map.entrySet()) {			
			keys.add(entry.getKey());
			values.add(entry.getValue());
		}
		Object[] objects= {keys,values};
		
		return objects;
	}
	
	public static Object[] getAgeSex() throws SQLException {
		ArrayList<String[]> list=connDb.index_2();
		
		JSONArray man= new JSONArray();
		JSONArray woman= new JSONArray();
		for (String[] strings : list) {
			JSONArray temp=new JSONArray();
			temp.put(Integer.valueOf(strings[1]));
			temp.put(Integer.valueOf(strings[2]));
			if(strings[0].equals("0")) {
				woman.put(temp);
			}else if(strings[0].equals("1")) {
				man.put(temp);
			}
		}
//		System.out.println(woman);
		
		Object[] objects= {woman,man};
//		System.out.println(objects[0]);
		return objects;
//		return null;
	}
	
	public static ArrayList<Double> getRepeatPredict() throws SQLException {
		ArrayList<Double> list=connDb.rPredict();
		//System.out.println(list);
		return list;
	}
	public static void main(String[] args) throws SQLException, JSONException {
		getRepeatPredict();
	}
}
