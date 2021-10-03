from PIL import Image,ImageColor
im = Image.new('1',(500,500))
def drawCircle(xc,yc,x,y): 
	im.putpixel((xc+x, yc+y),ImageColor.getcolor('WHITE', '1')) 
	im.putpixel((xc-x, yc+y),ImageColor.getcolor('WHITE', '1')) 
	im.putpixel((xc+x, yc-y),ImageColor.getcolor('WHITE', '1'))
	im.putpixel((xc-x, yc-y),ImageColor.getcolor('WHITE', '1'))
	im.putpixel((xc+y, yc+x),ImageColor.getcolor('WHITE', '1')) 
	im.putpixel((xc-y, yc+x),ImageColor.getcolor('WHITE', '1')) 
	im.putpixel((xc+y, yc-x),ImageColor.getcolor('WHITE', '1')) 
	im.putpixel((xc-y, yc-x),ImageColor.getcolor('WHITE', '1'))

def circleBres(xc,yc,r): 
	x=0
	y = r 
	d = 3 - 2 * r 
	drawCircle(xc, yc, x, y) 
	while (y >= x):
		x=x+1
		if (d > 0): 
			y=y-1 
			d = d + 4 * (x - y) + 10 
		else:
			d = d + 4 * x + 6 
		drawCircle(xc, yc, x, y) 

circleBres(100,200,50)
im.show()
