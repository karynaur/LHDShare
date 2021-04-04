import requests
import argparse


parser = argparse.ArgumentParser(description="Translator\n")
parser.add_argument('-t','--to',help="to language",required=True)
parser.add_argument('-c','--content',help="text to be translated",required=True)

args=vars(parser.parse_args())
url="https://libretranslate.com/translate"

parser.add_argument('-f','--from',help="from language",required=True)
print(targets)
data={
	'q':args['content'],
   'source':'auto',
   'target':args['to']
   
}
out=requests.post(url,data=data).json()
print(out['translatedText'])

