import argparse

parser = argparse.ArgumentParser(description='Postcard')
parser.add_argument('-t','--title', help='Title of postcard', required=True)
parser.add_argument('-n','--name', help='Your name', required=True)
parser.add_argument('-d','--description', help='content', required=True)

args = vars(parser.parse_args())

f=open('index.html','w')
text="<!DOCTYPE html><html lang=\"en\"><head><link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\"><title>Document</title></head><body><div class=\"card\"><div class=\"header\"><h1>"+str(args['title'])+" </h1></div><div class=\"body1\"><div class=\"texto1\" style=\"text-align:justify\"><p>   "+str(args['description'])+" </p></div></div><div class=\"body2\">By: "+str(args['name'])+"<br><br><br></div><div class=\"footer\"><p> Send My Postcard </p></div></div></body></html>"
f.write(text)
f.close()


