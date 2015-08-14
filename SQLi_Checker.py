import urllib
import re
ff = open('Crawl_Result.txt', 'r+')
sqli_result = open('SQLi_Result.txt', 'w+')
for links in ff:
        if '=' in links:
                try :
                        print '[Checking] '+links
                        rez = links+"'"
                        tst = urllib.urlretrieve(rez)
                        tstf = open(tst[0])
                        tstdd= tstf.read()
                        tstfind=re.findall('/error in your SQL syntax|mysql_fetch_array()|execute query|mysql_fetch_object()|mysql_num_rows()|mysql_fetch_assoc()|mysql_fetch_row()|SELECT * FROM|supplied argument is not a valid MySQL|Syntax error|Fatal error/i|You have an error in your SQL syntax|Microsoft VBScript runtime error',tstdd)
                        if(tstfind):
                                print "[SQLi Found] : " + rez
                                sqli_result.write(rez + '\r\n')
                        else:
                                print "[+] Not Vulnerable.\r\n"
                except IOError:
                        print "[ERROR] No result found"
        else:
                pass
print 'Vulnerable Result Sved in SQLi_Result.txt'
print './ done'
ff.close()
