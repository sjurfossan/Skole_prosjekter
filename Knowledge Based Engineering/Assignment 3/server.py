#paramServer.py
#HTTP Server template / One parameter
from http.server import BaseHTTPRequestHandler, HTTPServer
from read_data_sparql import read_dataset
import time

HOST_NAME = '127.0.0.1' 
PORT_NUMBER = 1234 # Maybe set this to 1234
#file path of this python file
filePath = 'C:\\Users\\sfoss\\OneDrive - NTNU\\Skole\\Knowledge-based Engineering\\Assignments\\Assignment 3\\tmm4270_assignment3'  #A folder where you store your DFAs
filePath_py = filePath + "\\test_html_server.py"

# Handler of HTTP requests / responses
class MyHandler(BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	
	def do_GET(s):

		# Check what is the path
		path = s.path
		if path.find("/") != -1 and len(path) == 1:
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))

		elif path.find("/info") != -1:
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>Current path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes("<body><p>Let's change some values</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))
			
		elif path.find("/enterTeapot") != -1:
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()
			s.wfile.write(bytes('<html><body><h2>Enter the boxes below</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/enterTeapot" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="lname">Last name:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="lname" name="lname" value="Smith"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="volume">Volume:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="volume" name="volume" value="10"><label for="volume_sufix"> L</label><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="flow_rate">Flow rate:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="flow_rate" name="flow_rate" value="3"><label for="flow_sufix"> L/s</label><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit"></form>', 'utf-8'))
			s.wfile.write(bytes('<img src="theProduct.png" alt="Product" width="700" height="500">', 'utf-8'))
			s.wfile.write(bytes('</body></html>', 'utf-8'))
			
		elif path.find("/theProduct.png") != -1: 
			#Make right headers
			s.send_response(200)
			s.send_header("Content-type", "image/png") #NB! File type dependant 
			s.end_headers()
			#Read and write the file
			
			bReader = open("C:\\Users\\sfoss\\OneDrive - NTNU\\Skole\\Knowledge-based Engineering\\Assignments\\Assignment 3\\tmm4270_assignment3\\images\\example_image.png", "rb")
			theImg = bReader.read() # Reading the file
			print(theImg) #Just for fun, printing/showing the content of the file.
			s.wfile.write(theImg) #Writing the read file to the client.

		elif path.find("/test_html_server.py") != -1: 
			#Make right headers
			s.send_response(200)
			s.send_header("Content-type", "application/octet-stream")
			s.send_header("Content-Disposition", "attachment; filename=test_html_server.py")
			s.end_headers()
			#Read and write the file
			
			bReader = open("C:\\Users\\sfoss\\OneDrive - NTNU\\Skole\\Knowledge-based Engineering\\Assignments\\Assignment 3\\tmm4270_assignment3", "rb")
			thePythonScript = bReader.read() # Reading the file
			print(thePythonScript) #Just for fun, printing/showing the content of the file.
			s.wfile.write(thePythonScript) #Writing the read file to the client.
			
		else:
			s.send_response(200)
			s.send_header("Content-type", "text/html")
			s.end_headers()	
			s.wfile.write(bytes('<html><head><title>Cool interface.</title></head>', 'utf-8'))
			s.wfile.write(bytes("<body><p>The path: " + path + "</p>", "utf-8"))
			s.wfile.write(bytes('</body></html>', "utf-8"))


			
	def do_POST(s):

		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		
		# Check what is the path
		path = s.path
		print("Path: ", path)
		if path.find("/enterTeapot") != -1:
			content_len = int(s.headers.get('Content-Length'))
			post_body = s.rfile.read(content_len)
			param_line = post_body.decode()
			print("Body: ", param_line)
			
			#Get the pairs
			pairs = param_line.split("&")
			
			#Get the param values for Last name, volume and volume rate
			pair_lastname = pairs[0].split("=")
			pair_volume = pairs[1].split("=")
			pair_volumerate = pairs[2].split("=")

			flow, vol = read_dataset(pair_lastname[1], pair_volumerate[1], pair_volume[1])

			
			s.wfile.write(bytes('<html><body><h2>Enter the boxes below</h2>', 'utf-8'))
			s.wfile.write(bytes('<form action="/enterTeapot" method="post">', 'utf-8'))
			s.wfile.write(bytes('<label for="lname">Last name:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="lname" name="lname" value="' + pair_lastname[1] + '"><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="volume">Volume:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="volume" name="volume" value="' + pair_volume[1] +'"><label for="volume_sufix"> L</label><br><br>', 'utf-8'))
			s.wfile.write(bytes('<label for="flow_rate">Flow rate:</label><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="text" id="flow_rate" name="flow_rate" value="' + pair_volumerate[1] + '"><label for="flow_sufix"> L/s</label><br><br>', 'utf-8'))
			s.wfile.write(bytes('<input type="submit" value="Submit">', 'utf-8'))
			
			s.wfile.write(bytes('<p>Last name entered: ' + pair_lastname[1] + 
					   '<br>Volume entered: ' + pair_volume[1] + '<br>Flow rate entered: ' + pair_volumerate[1] + '</p>', 'utf-8'))
			s.wfile.write(bytes('<p><img src="theProduct_generated.png" alt="Product" width="700" height="500"></p>', 'utf-8'))
			
			s.wfile.write(bytes('</form></body></html>', 'utf-8'))
			
			
			
	
			
 
if __name__ == '__main__':
	server_class = HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
	
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))