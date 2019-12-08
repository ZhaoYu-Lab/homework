<?php
header("Content-Type: text/html; charset=utf8");

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

// 面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (mysqli_connect_errno($conn)) {
	die("连接失败: " . mysqli_connect_error());
}
//header('Content-type:text/json;charset=utf-8');

$addNum = $_POST['addNum'];
$addName = $_POST['addName'];

if ($addNum == "") {
	echo "<script>alert('一卡通号为空');location.href='teacherLoginManageAdd.html'</script>";
} else if ($addName == "") {
	echo "<script>alert('密码为空');location.href='teacherLoginManageAdd.html'</script>";
} else {

	$sql_query = "INSERT INTO counsellorInfo  VALUES('$addNum','$addName') ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据添加成功')</script>";
	} else {
		echo "<script>alert('数据添加失败')</script>";
	}
}
mysqli_close($conn);

?>