		function changeElement()
		{
			x=document.getElementById('demo1');
			x.innerHTML='hello bi bibiibbiibi';
			x.style.color="#ff0000"; 
		}

		function changeColor(){
			x = document.getElementById('myeg');
			if(x.src.match('bulboff')){
				x.src='./img/eg_bulbon.gif';
			}
			else{
				x.src='./img/eg_bulboff.gif';
			}
		}
		function check(){
			var x = document.getElementById('inputint').value;
			if(x==''||isNaN(x)){
				alert('骚');
			}
			else{
				alert('屌');
			}
		}