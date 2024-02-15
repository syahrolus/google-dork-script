import sys
import argparse
from googlesearch import search

def load_checkpoint():
    try:
        with open('googling_checkpoint.txt', 'r') as checkpoint_file:
            return int(checkpoint_file.read().strip())
    except FileNotFoundError:
        return 0
    except Exception as e:
        print(f"Error loading checkpoint: {e}", file=sys.stderr)
        return 0

def search_and_log(query_list, domain):
    start_query_number = load_checkpoint()
    try:
        with open('googling_log.txt', 'a') as log_file:
            for query_number, query in enumerate(query_list[start_query_number:], start=start_query_number + 1):
                try:
                    print(f"\033[96m Searching for query {query_number}: '{query}' on '{domain}'\033[00m")
                    if query[5:] == "site:":
                        for url in search(query + domain, num=10, stop=10, pause=10):
                            print(url)
                            log_file.write(f"{query_number}: {url}\n")
                    else:
                        for url in search('site:' + domain + query, num=10, stop=10, pause=10):
                            print(url)
                            log_file.write(f"{query_number}: {url}\n")
                except Exception as e:
                    print(f"\033[97m Error occurred while processing query {query_number}: {e}\033[00m", file=sys.stderr)
                    # If timeout error, store the current query number in a checkpoint file
                    if "timed out" in str(e):
                        with open('googling_checkpoint.txt', 'w') as checkpoint_file:
                            checkpoint_file.write(str(query_number))
                    continue
    except Exception as e:
        print(f"\033[91m Error occurred: {e}\033[00m", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="Search queries on Google and save the results to googling_log.txt")
    parser.add_argument("domain", help="Domain to search for")
    args = parser.parse_args()

    # query_list = ["query1", "query2", "query3", "query4", "query5"]  # Your list of queries
    query_list = [
    ' intitle:index.of',
    ' ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini',
    ' ext:sql | ext:dbf | ext:mdb',
    ' ext:log',
    ' ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup',
    ' inurl:login',
    ' intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"',
    ' ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv',
    ' ext:php intitle:phpinfo "published by the PHP Group"',
    ' inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download',
    ' inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor',
    ' inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config',
    ' inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http',
    ' ext:action | ext:struts | ext:do',
    'site:pastebin.com ',
    'site:linkedin.com employees ',
    ' inurl:"/phpinfo.php" | inurl:".htaccess" | inurl:"/.git" ' + ' -github',
    'site:*.',
    'site:*.*.',
    ' inurl:wp-content | inurl:wp-includes',
    # 'https://github.com/search?q="*.'   site  '"&type=host',
    # 'http://'   site   '/crossdomain.xml', 
    # 'http://threatcrowd.org/domain.php?domain='   site, 
    # 'https://www.google.com/search?q= inurl:'   site   ' ext:swf',
    # 'https://yandex.com/search/?text=site:'   site   '%20mime:swf',
    # 'https://web.archive.org/cdx/search?url='   site   '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000&_=1507209148310',
    # 'https://web.archive.org/cdx/search?url='   site   '/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000&_=1507209148310',
    # 'https://web.archive.org/web/*/(.'   site   ')',
    # 'https://web.archive.org/web/*/'   site   '/*', 
    # 'https://crt.sh/?q=%25.'   site, 
    # 'https://www.openbugbounty.org/search/?search='   site  '&type=host',
    # 'https://www.reddit.com/search/?q='   site  '&source=recent', 
    # 'http://wwwb-dedup.us.archive.org:8083/cdx/search?url='   site   '/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx=',
    # 'https://censys.io/ipv4?q='   site,
    # 'https://censys.io/domain?q='   site, 
    # 'https://censys.io/certificates?q='   site,
    # 'https://www.shodan.io/search?query='   site,
    ]
    search_and_log(query_list, args.domain)

if __name__ == "__main__":
    main()
