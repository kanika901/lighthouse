import csv, urllib, MySQLdb

def file_name(precision, name, i):
    return str(precision+name+"_"+i+".txt") 


reader = csv.reader(open("url.csv"))

for idn, precision, routine, url in reader:
    URL = str("http://www.netlib.org/lapack/"+url)
    page = urllib.urlopen(URL)
    
    copy_page= open(file_name(precision, routine, idn), "w")

    
    while True:
        content = page.readline()

        if "===============================================" in content:
            print idn, "--> find match!"
            break


	if "Further Details" in content:
            print idn, "--> find match!"
            break		


        else:
            copy_page.write(content)
            
 
    page.close()
    copy_page.close()




