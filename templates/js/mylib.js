function addTab(title, url){
		if ($('#menu').tabs('exists', title)){
			$('#menu').tabs('select', title);
		} else {
			var content = '<iframe scrolling="auto" frameborder="0"  src="'+url+'" style="width:100%;height:100%;"></iframe>';
			$('#menu').tabs('add',{
				title:title,
				content:content,
				closable:true
			});
		}
	}