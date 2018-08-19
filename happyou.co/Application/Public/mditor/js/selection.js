/**
 * @author bh-lay
 * 
 * @github: https://github.com/bh-lay/Selection
 * 
 * @modified 2014-6-9 11:22
 *  
 */
define(function(doc){
	//set
	var setPosition = (function() {
		var textarea = doc.createElement("textarea");
		if (textarea.setSelectionRange) {
			return function(tarea,start, len) {
				var len = len || 0;
				setTimeout(function(){
					tarea.focus();
					tarea.setSelectionRange(start,start+len);
				});
			}
		} else if (textarea.createTextRange) {//IE
			return function(tarea,start, len) {
				var len = len || 0;
				tarea.focus();
				var strLen = tarea.value.length;
				var rng = tarea.createTextRange();
				rng.moveStart('character', start);
				rng.moveEnd('character', start + len - strLen);
				rng.select();
			}
		}
	})();
	//get
	var getPosition = (function(){
		var textarea = doc.createElement("textarea");
		if(typeof(textarea.selectionStart)=='number'){ //not IE
			return function(tarea){
				
				return [tarea.selectionStart,tarea.selectionEnd,tarea.value.slice(tarea.selectionStart,tarea.selectionEnd)];
			}
		}else{ //IE
			return function(tarea){
				var start = 0,
					 end = 0;
				tarea.focus();
				var sTextRange = doc.selection.createRange();
				
				if (tarea.tagName == "TEXTAREA") {
					var oTextRange = doc.body.createTextRange();
					oTextRange.moveToElementText(tarea);
					for (start = 0; oTextRange.compareEndPoints("StartToStart", sTextRange) < 0; start++) {
						oTextRange.moveStart('character', 1);
					}
					for (var i = 0; i <= start; i++) {
						if (tarea.value.charAt(i) == '\n') {
							start++;
						}
					}
					oTextRange.moveToElementText(tarea);
					for (end = 0; oTextRange.compareEndPoints('StartToEnd', sTextRange) < 0; end++) {
						oTextRange.moveStart('character', 1);
					}
					for(var i = 0; i <= end; i++) {
						if(tarea.value.charAt(i) == '\n') {
							end++;
						}
					}
				}
				return [start,end,selectedTxt,tarea.value.slice(start,end)];
			}
		}
	})();
	
	/**	 
	 * @method insertTxt
	 * @param {Object} dom jquery dom
	 * @param {String} text
	 * @param {Number} [start]
	 * @param {Number} [end]
	 * 
	 **/
	function insertTxt(tarea,txt,start,end){
		if(tarea.tagName != 'TEXTAREA' || typeof(txt) == 'undefined'){
			return
		}
		var txt = txt.toString();
		var this_start,this_end;
		if(typeof(start) == 'undefined'){
			var pos = getPosition(tarea);
			
			this_start = pos[0];
			this_end = pos[1];
		}else{
			this_start = parseInt(start);
			this_end = end || this_start;
		}
		
		var allTxt = tarea.value,
			frontTxt = allTxt.slice(0,this_start),
			 endTxt = allTxt.slice(this_end);
		tarea.value = frontTxt + txt + endTxt;
		
		setPosition(tarea ,frontTxt.length + txt.length,0);
	};
	
	//exports
	return {
		insertTxt : insertTxt,
		Selection : Selection,
		setPosition : setPosition,
		getPosition : getPosition
	};
});