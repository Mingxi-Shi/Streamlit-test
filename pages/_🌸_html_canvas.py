
import streamlit as st
import streamlit.components.v1 as components


def main():
    st.set_page_config(page_title="HTML简易画图", page_icon="🌸", layout="wide")

    sysmenu = '''
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility:hidden;}
            '''
    st.markdown(sysmenu, unsafe_allow_html=True)

    components.html("""

<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>无标题文档</title>
<style>
#aaa{
	border:5px #000 double;
	float:left;
	}
#bbb{
	width:350px;
	height:600px;
	border:5px #000 double;
	border-left-width:0px;
	float:left;
	}
</style>
</head>

<body>
<canvas id="aaa" height="600px" width="600px" onMouseDown="down(event);" onMouseMove="move(event);" onMouseUp="up(event);">
</canvas>
<div id ="bbb">
	<p>画笔颜色：<input type="color" id="hbys"/></p>
	<p>画笔大小：<input type="number" id="hbdx" value="1" min="1"/></p>
	选择需要画的图形：
	<div>
		<input type="button" id="zx" value="直线" onClick="setV(1);"/>
		<input type="button" id="yx" value="圆形"  onClick="setV(2);"/>
		<input type="button" id="zjjx" value="直角矩形"  onClick="setV(3);"/>
		<input type="button" id="yjjx" value="圆角矩形"  onClick="setV(4);"/>
		<input type="button" id="zdy" value="自定义"  onClick="setV(5);"/>
		<p></p>
	</div>
	<p><input type="checkbox" id="tc"/>是否需要填充</p>
	<p><label onClick="display();">添加文字(点击)：</label>
    	<input type="text" id="tjwz" style="display:none" onChange="changeT(file);"/></p>
	<p><input type="file" id="bjtp" onChange="getF(this);"/></p>
	<p><input type="button" value="清空" onclick="location.reload()"></p>
</div>
</body>
</html>

<script>
	var can=document.getElementById("aaa");//获取canvas标签
	var ctx=can.getContext("2d");//获取语填
	
	var type=5;
	var startX,startY,tc,a,typeT;

	function down(e)
	{
		startX=e.pageX-document.getElementById("aaa").offsetLeft;
		startY=e.pageY-document.getElementById("aaa").offsetTop;
		ctx.strokeStyle=document.getElementById("hbys").value;
		ctx.fillStyle=document.getElementById("hbys").value;
		ctx.lineWidth=document.getElementById("hbdx").value;

		if(type==1||type==5)
		{
			ctx.moveTo(startX,startY);
			a=1;
		}
		if(typeT==1)
		{
			ctx.strokeText(document.getElementById("tjwz").value,startX,startY);
			ctx.stroke();
		}	
	}
	function move(e)
	{
		var endX=e.pageX-document.getElementById("aaa").offsetLeft;
		var endY=e.pageY-document.getElementById("aaa").offsetTop;
		if(type==5&&a==1)
		{
			ctx.lineTo(endX,endY);
			ctx.stroke();
		}	
	}
	function up(e)
	{
		a=0;
		var endX=e.pageX-document.getElementById("aaa").offsetLeft;
		var endY=e.pageY-document.getElementById("aaa").offsetTop;
		
		if(type==1)
		{
			ctx.lineTo(endX,endY);
			ctx.stroke();
			
		}
		else if(type==2)
		{
			ctx.beginPath();
			ctx.arc(startX,startY,Math.abs((endX-startX))/2,0,2*Math.PI,false);
			ctx.stroke();
			ctx.closePath();
		}
		else if(type==3)
		{
			ctx.rect(startX,startY,(endX-startX),(endY-startY));
			ctx.stroke();
		}
		else if(type==4)
		{
			ctx.lineJoin="round";
			ctx.rect(startX,startY,(endX-startX),(endY-startY));
			ctx.stroke();
		}
		if(document.getElementById("tc").checked)
		{
			ctx.fill();
		}		
	}
	function setV(a)
	{
		type=a;
	}
	function display()
	{
		document.getElementById("tjwz").style.display="inline";
		typeT=1;
	}
	function changeT()
	{
		ctx.strokeText(document.getElementById("tjwz").value,startX,startY);
		ctx.stroke();
		
	}
	function getF(f)
	{
		var reader = new FileReader();
		reader.readAsDataURL(f.files[0]);	
		reader.onload=function()
		{
			var imageObj= new Image();
			imageObj.src=this.result;
			imageObj.onload=function()
			{
			  ctx.drawImage(imageObj,0,0,600,600);
			};
		}
	}
</script>


    """, height=1920, width=1080, scrolling=True)


if __name__ == '__main__':
    main()