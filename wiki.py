import wikipedia 
import pdfkit

wikipedia.set_lang("en")
random_page = wikipedia.random()
page = wikipedia.page(random_page)
pdfkit.from_url(page.url, random_page + ".pdf")

# ok, so this didn't quite work first time as it did miss a depenedency: sudo apt-get install wkhtmltopdf
# however, i'm still really impressed with this