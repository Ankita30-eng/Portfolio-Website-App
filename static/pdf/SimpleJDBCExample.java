import java.sql.*;
public class SimpleJDBCExample 
{
public static void main(String[] args) throws ClassNotFoundException, SQLException
{
Connection conn = null;
Statement stmt = null;
ResultSet rs=null;



Class.forName("com.mysql.cj.jdbc.Driver");


String url = "jdbc:mysql://localhost:3306/studentdb";
String user = "root"; // Your MySQL username
String pass = "anki@123"; //Your MySQL password
conn = DriverManager.getConnection(url,user,pass);


stmt= conn.createStatement();
String sql = "SELECT id,name,age FROM student";
rs =stmt.executeQuery(sql);


while(rs.next())
{
int id =  rs.getInt("id");
String name = rs.getString("name");
int age= rs.getInt("age");

System.out.println("ID: " + id +" ,Name:" + name +" Age:" +age);
}


rs.close();
stmt.close();
conn.close();
}
}
