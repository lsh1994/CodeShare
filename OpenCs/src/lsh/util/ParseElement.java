package lsh.util;

import java.util.HashMap;
import java.util.Map;

import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class ParseElement {
	
	public static Map<String, Object> getTag(Element element){
		String biaoqian=null;
		String xinde = null;
		String chima=null;
		String yanse=null;
		Map<String, Object> res=new HashMap<>();
		Elements sElements=element.select("dt");
		Elements pElements=element.select("dd");
		for (int i = 0; i < sElements.size(); i++) {
			Element element2 = sElements.get(i);
			//System.out.println(element2.text());
			if(element2.text().trim().equals("标　　签：")){
				biaoqian = pElements.get(i).text();
				res.put("biaoqian", biaoqian);
			}else if(element2.text().trim().equals("心　　得：")){
				xinde = pElements.get(i).text();
				res.put("xinde", xinde);
			}else if(element2.text().trim().equals("尺　　码：")){
				chima = pElements.get(i).text();
				res.put("chima", chima);
			}else if(element2.text().trim().equals("颜　　色：")){
				yanse = pElements.get(i).text();
				res.put("yanse", yanse);
			}
		}	
		return res;
	}
	
}
