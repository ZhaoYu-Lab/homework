<?php
header('Content-type:text/html;charset=utf-8');
$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . $conn->connect_error);
}
//header('Content-type:text/json;charset=utf-8');

$addNum = $_POST['addNum'];
$addName = $_POST['addName'];

if ($addNum == "") {
	echo "<script>alert('学号为空');location.href='bindManageAdd.html'</script>";
} else if ($addName == "") {
	echo "<script>alert('一卡通为空');location.href='bindManageAdd.html'</script>";
} else {

	$sql_query = "INSERT INTO studentBind  VALUES('$addName','$addNum') ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据添加成功')</script>";
	} else {
		echo "<script>alert('数据添加失败')</script>";
	}
}
mysqli_close($conn);

?>