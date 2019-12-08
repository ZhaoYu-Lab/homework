<?php
header("Content-Type: text/html; charset=utf8");

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (mysqli_connect_errno($conn)) {
	die("连接失败: " . mysqli_connect_error());
}

$studentNum = $_POST['studentNum'];

if ($studentNum == "") {
	echo "<script>alert('请输入账户名');location.href='studentLoginManageChange.html'</script>";
} else {

	$sql_query = "DELETE FROM studentInfo  WHERE Account = '$studentNum' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('账户删除成功')</script>";
	} else {
		echo "<script>alert('账户删除失败')</script>";
	}
}

mysqli_close($conn);

?>