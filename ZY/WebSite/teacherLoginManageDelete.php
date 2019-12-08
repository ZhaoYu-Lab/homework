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

$teacherNum = $_POST['teacherNum'];

if ($teacherNum == "") {
	echo "<script>alert('教师一卡通号为空');location.href='teacherLoginManageDelete.html'</script>";
} else {

	$sql_query = "DELETE FROM  counsellorInfo  WHERE Account = '$teacherNum' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据删除成功')</script>";
	} else {
		echo "<script>alert('数据删除失败')</script>";
	}
}

mysqli_close($conn);

?>