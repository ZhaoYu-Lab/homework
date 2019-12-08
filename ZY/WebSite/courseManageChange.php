<?php
//header('Content-type:text/json;charset=utf-8');
header('Content-type:text/html;charset=utf-8');

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

// 面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (mysqli_connect_errno($conn)) {
	die("连接失败: " . mysqli_connect_error());
}

$courseNum = $_POST['courseNum'];

if ($courseNum == "") {
	echo "<script>alert('课程编号为空');location.href='courseManageChange.html'</script>";
} else if ($courseName == "") {
	echo "<script>alert('课程名称为空');location.href='courseManageChange.html'</script>";
} else {

	$sql_query = "UPDATE courses SET courseName = '$courseName' WHERE courseNum = '$courseNum' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据添加成功')</script>";
	} else {
		echo "<script>alert('数据添加失败')</script>";
	}
}
mysqli_close($conn);

?>