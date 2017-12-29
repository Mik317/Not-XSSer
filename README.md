# Not-XSSer
Tool for test XSS vulnerabilities of a site

## What Does It Do???
This tool is a simple XSS payloads injector that can:

- Inject manual payloads
- Inject automatic payloads (Generated in automatic way for all js code inserted)
- Use modules for XSS exploits [like keylogging,reverse shell,credentials harvester ...](/XSSer/Modules/)
- Report all in a Web Panel (Django Powered)
- Connect and send requests under HTTP proxies
- Search for vuln sites (I recommend you under http proxy for not be banned from Google engine)
- Synchronization between terminal script and web panel
- Test for requirements installation
- Read payloads or target urls from text file (txt file accepted)
- List of proxyes
- CSRF and ClickJacking test
- Report in text file (for save the session output)
- Identify a session with title,authors and description (It will be reported in Web Panel)
- It offer a simple 'base-class' for the creation of other modules for XSS exploiting

## To do:

- [ ] Create modules for XSS payloads
- [ ] Add POST support (now only GET)
- [ ] Insert output div in report on web panel
- [ ] Fix code (some things are hard coded :scream:)

## Docs :information_source:
This tool is very simple to use, but I want document all functions for test the final code and for eliminate any doubts;

##### Help Command
The help command show in few lines, what does every function, and what arguments it want;
You can see it just typing: `python Xss.py -h` or `py Xss.py --help`, and it will show you an output like this:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/help.png "Help Command Out")

##### Inject Manual Payload
This option allows to specify a custom payload to inject (specify it using `-i` or `--inject` agrument) in a specified site (you do specify it using the `--url` or `-u` argument);
For avoid problems, insert the script and the url (with the vulnerable resource to test) in single apices (''); 
The output will be similar to this:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/inj.png "Inject Manual Payload")

##### Create a Proxy List
This script provide the `-lp` or `--list_proxies`, that accept a number; The number will identify the number of proxies to return;
Insert a number between 1 and 20, because higher number will list much obsolete proxies;
IMPORTANT: Proxies aren't tested then, some of this will report errors if you use it. 
The output will be suchlike: 
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/lp.png "List Proxies")

##### Use the Proxies
This script allows to use proxed connection for avoid being discovered, and it support HTTP proxies (recommended);
For use proxies, you do specify the `-p` or `--proxy` arguments, and pass the complete url address of the proxy, like this:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/proxy.png "Use Proxy")
IMPORTANT: The headers that you can see in the photo are different from the output without proxy arg; This because when you use the proxy, some of these tunnells the connection, and return their headers, not of the target url.
IMPORTANT2: If you are under proxy, and you want use your default proxy, set `--proxy` as `localhost` or `127.0.0.1`

##### Url Argument
The url argument (`--url` or `-u`), accept url within the resource to test, then, you cannot insert a simple web address of a site, but you do insert the web address and the GET resource of the site:
In other words: 
:exclamation: :-1: `py Xss.py --url 'https://www.google.com/' `    `py Xss.py --url 'https://www.google.com/search?q=' ` :+1: (example)

##### The Automated Attacks
This script allows you to generate payloads from a simple piece of code (javascript);
The `-a` or `--automatic` , generate payloads from the payloads in the 'payloads' list in the python code, and return another list within more payloads; 
Example case (default): in the list 'payloads' you have only this: `alert(123456789)`, but if you insert the `-g` or `--generated_payloads` , you can view more than one payload ...... :
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/gen.png "See Generated Payloads")
For have even more payloads, insert the pieces of js code that you want inject in various shapes in the 'payload' list (you can find it in the primary part of code).
IMPORTANT: Not confuse `-a` with `-g`: 
`-a` inject all the payloads that you can see with `-g-` in a target site, while `-g` show only they ......
Example:
`py Xss.py -g` : ![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/gen.png "See Generated Payloads")
`py Xss.py -a --url 'http://site.com/search_result.php?Code=' -p localhost` : ![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/automated.png "Automated Attack")

##### Report In File
You can save an attack session simply using the `-r` or ` --report_on_file` argument; It will create automatically a file with memorized all that you can view from the terminal; The file is marked and named with the data of the day,hours and minutes;
The argument doesn't accept arguments, and the result will be such this:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/report%20in%20file.png "Use Report in File")
IMPORTANT: With some proxy, you receive an error, or the text will be only the first line of the terminal; 
In this evenience, change proxy or try with a simple `-p localhost` for avoid other problems

##### Inject Payloads From a File
This script can read payloads from a file and inject they in the specified url. 
For do it, insert the `-fp` or `--file_payloads` argument, with the name of the file where the script can read all the payloads. 
Simply: ![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/pay.png "Payload In File payloads.txt")
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/pay2.png "Payload In File Automatic Injection")
In this example you can see how the elementary payload `<script>alert(document.cookie)</script>`, united with the `-a` argument, will be generated in more than one !!!

##### Attack Target Urls From File
Using the `-ft` or `--file_target_url` argument, you can extract from the file, all the site to attack; 
You do simply specify the file with the target's urls; The output will be similar to this:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/ft.png "File Target Urls")

##### Search Option
This script can crawl all the Google engine, and using the dorks (interesting technique that Google use for indicize all the pages), you can view if a site present probability vulnerable resource that accept html/text/other code.
For use it, use the `-s` or `--search`, with argument the site to scan;
Like this:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/search.png "Search")

##### CSRF and ClickJacking Option
This option control the headers and see their values; 
Usig the result, you can try or not with CSRF and ClickJacking attacks (manually)

##### Test 
The `-t` or `--test` argument will test the requirements for bring a term the script installation.
You can also use the `setup.py`

##### Modules Usage and Development
You can use modules specifing the `-M` or `--module` argument; 
You can find more infos typing `py Xss.py -Mh`.
For use a Module, do it:
1. `mv module.py module`, and then, type `py Xss.py -M module`
2. Type `Y` (if you want use it), and wait that it finish.
3. See the result that the console show
IMPORTANT: You cannot use modules with Web Panel
For create other modules, you do bring step-by-step all the steps:
1. Create a new class with name 'Module'
2. Insert the script in a string, and execute it with the eval() function
3. Instantiate all the base method and the variables (name, description,author,date,help(),execute(),ecc....)
4. Load and execute it as a simple module (You can see an example from the 'ExampleModule')

##### Session
This script can organize you attacks as session of attack that you can synch with the web panel;
For identify an attack, use this options:
- `--title` (most important for identify an attack)
- `--completed` (mark as completed attack or uncompleted)
- `--desc` (insert a description of the attack)
- `--auth` (insert the attack's author)

##### Report in Web Panel
Using the `-rW` or `--report_on_web` option, you can report it as a session on the web panel;
For do it, you do specify all as a simple attack and add the argument `-rW`, like this:
`py Xss.py -a -p localhost -u 'http://www.vuln.site/vuln.php?resource=' -c -rW --title 'HackWorld' --desc 'Simple example of desc' --auth 'Mik' --completed`
Before: ![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/w1.png "Web Panel 1")
Command: ![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/cw.png "Coomand for Report in Web Panel")
After: ![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/cw2.png "Our Session in Web Panel")
And then, you can view the report (insert always the tile, or the session will not appear):
1. click on the title, you will redirected in another page, reclick the title and then .... :
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/rep.png "Report in Web Panel")
(I have added the output panel on the report)
For create Session from the web panel:
1. Go on `localhost:8000/admin` 
2. Login with credentials that you have used for create the `superuser` 
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/login.png "Web Panel Login")
3. Click on `Add` or on `Edit`, and do what you want :smiling_imp: :alien:
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/xla.png "Web Panel Actions")
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/add.png "Web Panel Add Attack")
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/added.png "Added From Web Panel")
![alt text](https://github.com/Mik317/Not-XSSer/blob/master/images/added2.png "Home Now")

##### The Help Options
This script is provided of:
- `-rWh` (for help you in Web Panel Report), 
- `-h` (simple help message),
- `-Mh` (for help you in module creation and usage)

##### Web Panel Setup
With the script, there are the configuration file for the Web Panel (powered by Django);
1. Open the terminal, go to the path of the 'manage.py' file
2. Insert the command: `py manage.py makemigrations`, and after `py manage.py migrate` (for make the db)
3. Now, insert: `py manage.py runserver`, and `py manage.py createsuperuser`; Insert your credentials for a new account
4. And then, go on `localhost:8000/home/`, or on `localhost:8000/admin` : Now you can manage your XSSer !!!
IMPORTANT: If you have some problem with db, or index, go on the 'manage.py path', and execute it: `rm -rf db.sqlite3`, now do the first point for recreate the db. If the problem persist, contact me !!!

> Bug isn't only an error 
