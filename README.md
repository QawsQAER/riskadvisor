# Risk Analysis

Risk Advisor use Public Big Data to retrieve and analyze the "Risk Factors" for US publicly traded companies. Publicly available data sources (such as 10-K) are retrieved to create profiles for the companies and segment them based on their "risk factors" and "needs."

The current url is [riskanalysis.mybluemix.net](http://riskanalysis.mybluemix.net/).

##End-point for backend
http://54.191.103.199:8080/tradeoffParser/webapi/parser/select

##Sample json input
```
see the a.json file in the root directory
```
##Sample json output
```json
{  
    "columns":[  
        {  
            "full_name":"Funding risks",
            "goal":"MIN",
            "is_objective":"TRUE",
            "type":"numeric",
            "key":"Funding risks"
        },
        {  
            "full_name":"Competition risks",
            "goal":"MIN",
            "is_objective":"TRUE",
            "type":"numeric",
            "key":"Competition risks"
        }
    ],
    "subject":"Risk",
    "options":[  
        {  
            "values":{  
                "Funding risks":3,
                "Competition risks":0
            },
            "name":"AMZN2014",
            "description_html":"Risk Advisor feat. TradeOff Analysis",
            "key":"0"
        },
        {  
            "values":{  
                "Funding risks":7,
                "Competition risks":5
            },
            "name":"TWTR2014",
            "description_html":"Risk Advisor feat. TradeOff Analysis",
            "key":"1"
        }
    ]
}
```

##How to test (on Mac only)
```sh
brew install httpie
cd IBM-RiskAdvisor-Tradeoff
http POST http://54.191.103.199:8080/tradeoffParser/webapi/parser/select @a.json
```

## Prequisite

Be sure the followings are installed successfully on your machine.

*   Tomcat 6+
*   Java 1.5
*   Ant
*   MongoDB 2+
*   Git

## Build from Source

There are two places you can clone from.

* From GitHub

This is a public project, so you can clone the repo directly.

```
cd your_workspace_path
git clone git@github.com:Gonghan/WebCrawlerApp.git
cd WebCrawlerApp
ant
```

* From Jazz Hub

```
cd your_workspace_path
git clone https://hub.jazz.net/git/gonghan/WebCrawlerApp
cd WebCrawlerApp
ant
```

* Tomcat configurations
  * Go to the directory of your tomcat.
  * Go to your_tomcat/conf
  * Open server.xml
  * Add this line into the <host> tag.
  
  ```
  <Context docBase="your_workspace/WebCrawlerApp/webStarterApp.war" path="/" reloadable="true"/>
  ```
  Here the **webStarterApp.war** is the compressed file generated by running **ant**. You can modify the **build.xml** to use a more meaningful name. Also the **path="/"**, otherwise you may get a bug.
  
  If you find a bug about missing keywords or categories, please read the DummyServlet.java. You need to manually insert all this into the MongoDB.

## Import into IDE

I recommend [Eclipse EE](http://www.eclipse.org/downloads/packages/eclipse-ide-java-ee-developers/keplersr2) as the IDE for this project.

 * Import the downloaded source code into Eclipse EE.
 * Add all the jars in the WebContent/lib/ into the project build path.
 * Strongly recommend you create a web server(tomcat) inside Eclipse and continue the tomcat configurations.

## Deployment

* On your own machine.
 Follow the instructions above and done.
* BlueMix
 * Create a BlueMix account
 * Log in BlueMix website and go to the dashboard.
 * Create an App and select Library for Java.
 * Enter the domain name and click 'create' button.
 * Then click the app and go to the overview page of the app.
 * Click **VIEW QUICK START** the top right corner.
 * Follow the instructions.

## Database
Currently I use the MongoLab single-instance as the database for this project. If you have the account, just log in. You can see the detailed collections and data.

If you want to use a new account or create a new database. 
* Make sure the new database is accessible from the BlueMix space.
* Create a database.
* Update the constants in the MongoConstants.java.
* Manually insert all the keywords and categories into the new database.
* Read DummyServlet.java which tells you how to do that.

## Components

### UI

#### index.jsp

Show the basic information about this project.

#### crawler.jsp

Provide a form to crawl data or delete data.

#### comparison.jsp

Provide a comparison between the finanical risks of two companies.

#### results.jsp

Show the details financial risks of a given company.

#### APIs.jsp

Give a table of all available APIs.

### Model

#### Category

Define the risk of a company in terms of categories.

Data structure
```
{
    "Funding risks": 1,
    "Concentration on few large customers": 0,
    "Competition risks": 2,
    "Downstream risks": 0,
    "Catastrophes": 1,
    "Macroeconomic risks": 3,
}
```

#### Keywords

Define the keywords and frequencies of a company.
```
{
    "keywords": {
        "new regulation": 1,
        "economic condition": 1,
        "emerging markets": 1,
        "foreign laws": 1,
        "intellectual property": 1,
    }
}
```

#### Record

Contains the raw data(riskFactor) and the year.

```
{
    "records": [
        {
            "companyName": null,
            "year": "2013",
            "riskFactor": "item 1a. risk factors:         downturn  spending budgets could impact the ......",
            "symbol": "IBM",
            "keywords": {
                "new regulation": 1,
                "economic condition": 1,
                "emerging markets": 1
            }
        }
    ]
}
```

### API

I use [Jersey](https://jersey.java.net/) to build the restful APIs.

This is a sample about the API resource. You can find this code snippet in the edu.cmu.sv.webcrawler.apis.ResultsResource.java

```
@Path("/results")
public class ResultsResource {
```
@Path provides a relative URI path.

```
@GET
	@Path("/{param}")
	@Produces(MediaType.APPLICATION_JSON)
	public Records getResult(@PathParam("param") String symbol,
			@QueryParam("year") String year) {
 		Records records = new Records();
 		List<Record> list = null;
 		if (year == null || year.isEmpty()) {
 			list = Record.search(symbol);
 		} else {
 			list = Record.search(symbol, year);
 		}
 		records.setRecords(list);
 		return records;
	}
```
This function gets one param as the symbol and a query string as the year. A sample url which will redirect to this function:

```
api/results/IBM?year=2013
```
The return format is JSON. You don't need to create a JSON object manually. What you need to do is to define the data format in the models package.

### Servlet
All servlets are in the edu.cmu.sv.webcrawler.servlets package. In fact, I use them for very limited functions. It's a good practice to build API layer and UI layer independently. Then use JavaScript to connect them together. In the next steps, I will remove all servlets and build more APIs instead.

### MongoDB and Schema

There are four collections in the MongoDB: **categories**, **companysymbols**, **keywords**, **webcrawler**. To access to the collections, make sure that you have already created the database. **Database creation can be done manually only.**

#### categories

There is only one document in this collection. The document is the same as the json file 'catogories.json' which is located in the root directory of the project.

````
{
    "Funding risks": [
        "capital",
        "raise capital",
    ],
    "Concentration on few large customers": [
        "customer",
        "key customer",
        "large customer"
    ]
}

````

#### companysymbols

This collection contains 3637 records. Each record has one symbol.

````
{
    "_id": {
        "$oid": "53cd61868f6491b7c901a635"
    },
    "symbol": "NWSA"
}
{
    "_id": {
        "$oid": "53cd61868f6491b7c901a636"
    },
    "symbol": "FUBC"
}
````

#### keywords

This collection contains 142 records. Each record has one keyword.

````
{
    "_id": {
        "$oid": "53cd62318f640941ecabdb9f"
    },
    "value": "net loss"
}
{
    "_id": {
        "$oid": "53cd62318f640941ecabdba0"
    },
    "value": "loss of business"
}
````

#### webcrawler

This is the main collection and the place where all raw data is stored.

```
{
    "records": [
        {
            "companyName": null,
            "year": "2013",
            "riskFactor": "item 1a. risk factors:         downturn  spending budgets could impact the ......",
            "symbol": "IBM",
            "keywords": {
                "new regulation": 1,
                "economic condition": 1,
                "emerging markets": 1
            }
        }
    ]
}
