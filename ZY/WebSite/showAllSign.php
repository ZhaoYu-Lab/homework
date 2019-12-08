<?php

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . $conn->connect_error);
}
header('Content-type:text/json;charset=utf-8');

$nowDay = $_POST['nowDay'];
$YDay = $_POST['YDay'];
$NDay = $_POST['NDay'];

$sql_query = "SELECT * FROM sign where signTime >'$nowDay' and signTime < '$NDay' ";

$result = mysqli_query($conn, $sql_query);

$jsonArray = array(); //新建数据用于接收数据库每行对应的数据组
while ($rows = $result->fetch_assoc()) {
	//把数据库的内容添加到新建数组中
	array_push($jsonArray, $rows); //注意这里是$rows
}
echo json_encode($jsonArray); //转换成json传递给前端
mysqli_close($conn);

?>