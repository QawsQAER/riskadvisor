<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Web Crawler</title>
<%@  include file="./templates/includes.jsp"%></head>
<body>
	<%@  include file="./templates/header.jsp"%>
	<%
		String url = request.getRequestURL().toString();
		String host = url.substring(0, url.length() - 9);
	%>

	<!-- Main part -->
	<h1>APIs</h1>
	<div class="apis">
		<table
			class="table table-striped table-hover table-bordered table-striped">
			<tbody>
				<tr>
					<td>Method</td>
					<td>URL</td>
					<td>Description</td>
				</tr>

				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/symbols"%></td>
					<td>Get symbols of all companies and return JSON file.</td>
				</tr>

				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/crawl"%></td>
					<td>Begin to crawl the 10-K documents from all companies' symbols.</td>
				</tr>

				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/crawl/:symbol?docType=:docType"%></td>
					<td>Begin to crawl the record from a given company symbol for a specific document type</td>
				</tr>

				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/results/:symbol"%></td>
					<td>Show the results of a given company.</td>
				</tr>

				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/results/:symbol?year=:year"%></td>
					<td>Show the results of a given company in a year.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/results/:symbol?docType=:docType"%></td>
					<td>Show the results of a given company in a specific document type.</td>
				</tr>

				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/results/:symbol?year=:year&docType=:docType"%></td>
					<td>Show the results of a given company in a year with a specific document type.</td>
				</tr>
				
				<tr class="success">
					<td>DELETE</td>
					<td><%=host + "/api/results/"%></td>
					<td>DELETE all results.</td>
				</tr>
				
				<tr class="success">
					<td>DELETE</td>
					<td><%=host + "/api/results/:symbol?year=:year"%></td>
					<td>DELETE the results of a given company in a given year.</td>
				</tr>
				
				<tr class="success">
					<td>DELETE</td>
					<td><%=host + "/api/results/:symbol?docType=:docType"%></td>
					<td>DELETE the results of a given company in a specific document type.</td>
				</tr>
				
				<tr class="success">
					<td>DELETE</td>
					<td><%=host + "/api/results/:symbol?year=:year&docType=:docType"%></td>
					<td>DELETE the results of a given company in a year with a specific document type.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/keywords"%></td>
					<td>Show all keywords.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/keywords/:symbol?year=:year"%></td>
					<td>Show keywords of a given company in a given year.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category"%></td>
					<td>Show the categories of all keywords.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category/:symbol?year=:year"%></td>
					<td>Show the categories of one company in a given year.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category/:symbol?docType=:docType"%></td>
					<td>Show the categories of one company in a specific document type.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category/:symbol?year=:year&docType=:docType"%></td>
					<td>Show the categories of one company in a given year with a specific document type.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category/frequency/:symbol?year=:year&docType=:docType"%></td>
					<td>Show the normalized categories of one company in a given year with a specific document type.</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category/addKeyword?category=:categoryName&keyword=:keywordString"%></td>
					<td>Add keyword according to category</td>
				</tr>
				
				<tr class="success">
					<td>GET</td>
					<td><%=host + "/api/category/deleteKeyword?category=:categoryName&keyword=:keywordString"%></td>
					<td>delete keyword according to category</td>
				</tr>
				
			</tbody>
		</table>
	</div>

<!-- 	<div id="instructions" class="bg-info">
		<label>Instructions</label>
		<ul>
			<li>Replace symbol with a REAL company symbol(e.g., NWSA, FUBC).</li>
			<li>Replace the yyyy with a REAL year(e.g., 2013, 2012)</li>
		</ul>
	</div> -->

	<%@  include file="./templates/footer.jsp"%>
</body>
</html>