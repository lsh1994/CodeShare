package lsh.util;

import java.util.Map;

import org.json.JSONArray;
import org.json.JSONObject;
import org.jsoup.Connection.Response;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

public class CrawlData {
	
	public Document getUrl(String id,int page) throws Exception{
		//http://club.jd.com/review/11728532333-3-1-0.html
		String url="http://club.jd.com/review/"+id+"-3-"+page+"-0.html";//id,?,页码,情感信息
		Document doc=Jsoup.connect(url).get();
		return doc;
		
	}
	public void papa(String id,int howpage) throws Exception{
		int allCount=0;
		Document doc=null;
		if(true){			
			Document document=getUrl(id,1);
			String title=document.title();
			Elements per=document.select(".percent");
			String arate=null;
			if (per.size()>0) {
				arate=per.get(0).text();
			}
			Elements abq=document.select(".actor-new");
			String sabq=null;
			if (abq.size()>0) {
				sabq=abq.get(0).text().trim().split("：")[1];
			}
			double price=getPrice(id);
			
			//System.out.println(arate+","+sabq+","+price);
			String string="INSERT INTO good(gid, title, price, biaoqian, haopingdu) VALUES (%s, '%s', %f, '%s', '%s')";
			string=String.format(string, id,title,price,sabq,arate);	
			//System.out.println(string);
			int errcode=DBHelper.update(string);
			if(errcode==-1){
				System.out.println("操作错误："+string);
				return;
			}
		}
		int p=1;
		for(;p<=howpage;p++){
			doc=getUrl(id,p);
			Elements names=doc.select(".user").select(".u-name");	
			Elements comment=doc.select(".comment-content");
			Elements date=doc.select(".date-comment").select("a");
			if (names.size()==0) {
				break;
			}
			allCount+=names.size();
			for (int i = 0; i < names.size(); i++) {
				Map<String, Object> res=ParseElement.getTag(comment.get(i));
				//System.out.println(names.get(i).text()+": "+res.get("xinde")+":"+date.get(i).text());
				String string="INSERT INTO pinglun(uname, gid, date, xinde,yanse, chima, biaoqian) VALUES ('%s', %s,'%s', '%s',' %s','%s', '%s')";
				string=String.format(string, names.get(i).text(),id,date.get(i).text(),res.get("xinde").toString().replaceAll("'", "''"),res.get("yanse"),res.get("chima"),res.get("biaoqian"));
				
				//System.out.println(string);
				DBHelper.update(string);				
			}
		}
		System.out.println("数据已经抓完或达到页数！总条数："+allCount+",实际抓取页数："+(p-1));
		
	}
	
	private double getPrice(String id) {
		// TODO Auto-generated method stub
		//http://p.3.cn/prices/mgets?skuIds=J_11728532333
		String url="http://p.3.cn/prices/mgets?skuIds=J_"+id;
		double price=0;
		try {
			Response rsp=Jsoup.connect(url).ignoreContentType(true).execute();
			JSONArray jArray=new JSONArray(rsp.body());
			if(jArray.length()>0){
				JSONObject jo=new JSONObject(jArray.get(0).toString());
				price=Double.parseDouble(jo.get("p").toString());
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 
		return price;
	}
	public static void main(String[] args) throws Exception {
		new CrawlData().papa("11728532333",100);
		new CrawlData().papa("1150556",100);
		new CrawlData().papa("4891234",100);
	}
}
