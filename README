Wolfram parser:
	This tool get words and articles from https://mathworld.wolfram.com
	in addition it can collect the definition of the words from https://wolframalpha.com using its API
	to be able to use this script you need :
		1. register at https://www.wolframalpha.com/ 
		2. create API key via My Apps(API) 
		3. replace the existing API Key in the config.json 'app_id'
	Dependencies:
		To run this script you need to use python 3.8 
		install couple of packages via pip install
		You can use " pip3 install -r requirements.txt ":
			beautifulsoup4		4.9.1	4.9.1
			inflect				4.1.0	4.1.0
			jaraco.itertools	5.0.0	5.0.0
			more-itertools		8.4.0	8.4.0
			pip					19.0.3	20.2.2
			setuptools			40.8.0	49.6.0
			six					1.15.0	1.15.0
			soupsieve			2.0.1	2.0.1
			wolframalpha		4.0.0	4.0.0
			xmltodict			0.12.0	0.12.0

			this what i had when i run this script
	Execution:
		execution is very simple , in the config file you need to:
			1. 	insert wolfram API in 'app_id',
			2.	insert "https://mathworld.wolfram.com" (exist by default in the config file)
			3. 	insert all post fix urls with the world list
			4. 	python WolframGetter.py
	Output:
		The script will create 3 json files:
			1. articles.json - json math articles dictionary (3000 articles)
				Format: {'<word from math world>':'<Full article of this word>',....}
			2. definitions.json - json definitions dictionary  (1700 defs)
				Format: {'<word from math world>':'<Definition from wolframalpha API>',....}
			3. failed_definitions.json - json words list that failed to collect definition via wolframalpha API (1200 failed defs)
				Format: ["failed_word_1","failed_word_2",...,"failed_word_N"]
	Example:
		This is my config example :
			{
			  "app_id": "FFFFFF-FFFFFFFFFF",
			  "urls_to_read": {
			    "web_url": "https://mathworld.wolfram.com",
			    "post_fix_urls": [
			      "/topics/AnimatedGIFs.html",
			      "/topics/InteractiveDemonstrations.html",
			      "/topics/webMathematicaExamples.html"
			    ]
			  }
			}


