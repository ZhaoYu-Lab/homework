<?php
header("Content-Type: text/html; charset=utf8");

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . mysqli_connect_error());
}
//header('Content-type:text/json;charset=utf-8');

$studentName = $_POST['studentName'];

if ($studentName == "") {
	echo "<script>alert('学生姓名为空');location.href='studentManageDelete.html'</script>";
} else {

	$sql_query = "DELETE FROM  students  WHERE studentName = '$studentName' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据删除成功')</script>";
	} else {
		echo "<script>alert('数据删除失败')</script>";
	}
}

mysqli_close($conn);

?>