<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<%@ page import="java.util.List" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="java.util.Map" %>
<%@ page import="java.util.HashMap" %>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
</head>
<body>

<%
	List<Map<String, Object>> articles = new ArrayList<>();
	try {
		Class.forName("com.mysql.cj.jdbc.Driver");
		out.print("JDBC 연동 완료");
	} catch ( ClassNotFoundException e ) {
    	out.print("JDBC를 찾을 수 없음");
		e.printStackTrace();
		return ;
    }
	Connection conn = null;
	Statement stmt = null;
	ResultSet rs = null;
	
	try {
		String url = "jdbc:mysql://localhost:3306/a?characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false";
		conn = DriverManager.getConnection(url,"root","");
		
		out.print("DB 연동 완료");
		
		stmt = conn.createStatement();
		String sql = "SELECT * FROM article ORDER BY id DESC;";
		rs = stmt.executeQuery(sql);
		
		out.print("쿼리 실행 완료");
		
		while ( rs.next() ) {
			Map<String, Object> article = new HashMap<>();
			article.put("id",rs.getInt("id"));
			article.put("regDate",rs.getString("regDate"));
			article.put("title",rs.getString("title"));
			article.put("writer",rs.getString("writer"));
			
			articles.add(article);
		}
		
	} catch (SQLException se1) {
	    se1.printStackTrace();
	} catch (Exception ex) {
	    ex.printStackTrace();
	} finally {
	    try {
	        if (stmt != null)
	            stmt.close();
	    } catch (SQLException se2) {
	    }
	    try {
	        if (conn != null)
	            conn.close();
	    } catch (SQLException se) {
	        se.printStackTrace();
	    }
	}   
%>


<h1>게시글</h1>
<% for ( int i = 0; i < articles.size(); i++ ) { %>
	<div>번호 : <%= articles.get(i).get("id") %></div>
	<div>날짜 : <%= articles.get(i).get("regDate") %></div>
	<div>제목 : <%= articles.get(i).get("title") %></div>
	<div>작성자 : <%= articles.get(i).get("writer") %></div>
	<hr/>
<% } %>


</body>
</html>