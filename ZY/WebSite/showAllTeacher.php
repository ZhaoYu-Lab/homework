<?php
header("Content-Type: text/html; charset=utf8");

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
	die("连接失败: " . $conn->connect_error);
}
$conn->query("set names utf8");

$query = "SELECT * FROM teachers";
//Use a variable to save result
$result = $conn->query($query);

$jsonArray = array(); //新建数据用于接收数据库每行对应的数据组
while ($rows = $result->fetch_assoc()) {
	//把数据库的内容添加到新建数组中
	array_push($jsonArray, $rows); //注意这里是$rows

}
echo json_encode($jsonArray); //转换成json传递给前端
$conn->close();
?>