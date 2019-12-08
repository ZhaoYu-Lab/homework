<?php
header('Content-type:text/json;charset=utf-8');

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . $conn->connect_error);
}

$conn->query("set names utf8");

$studentName = $_POST['studentName'];
$studentClass = $_POST['studentClass'];
$starTime = $_POST['starTime'];
$endTime = $_POST['endTime'];

$sql1 = "SELECT * FROM students WHERE studentName = '$studentName' ";
$result = $conn->query($sql1);
if (mysqli_num_rows($result) > 0) {
	// 输出数据
	while ($row = $result->fetch_assoc()) {
		$studentNum = $row["studentNum"];
	}
} else {
	echo "2";
}

if ($starTime == "" || $endTime == "" || $studentNum == "") {
	//条件为空则查询所有
	$sql_query = "SELECT * FROM sign";
} else {
	$sql_query = "SELECT * FROM sign WHERE studentClass = '$studentClass' and  studentNum ='$studentNum' and  startTime between '$starTime' and  '$endTime'";
}

$result = mysqli_query($conn, $sql_query);

$jsonArray = array(); //新建数据用于接收数据库每行对应的数据组
while ($rows = $result->fetch_assoc()) {
	//把数据库的内容添加到新建数组中
	array_push($jsonArray, $rows); //注意这里是$rows

}
echo json_encode($jsonArray); //转换成json传递给前端

mysqli_close($conn);

?>