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
//header('Content-type:text/json;charset=utf-8');

$studentNum = $_POST['studentNum'];
$Pwd = $_POST['Pwd'];

if ($studentNum == "") {
	echo "<script>alert('请输入账户名');location.href='studentLoginManageChange.html'</script>";
} else if ($Pwd == "") {
	echo "<script>alert('请输入密码');location.href='studentLoginManageChange.html'</script>";
} else {

	$sql_query = "UPDATE studentInfo SET PWD = '$Pwd' WHERE Account = '$studentNum' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('密码修改成功')</script>";
	} else {
		echo "<script>alert('密码修改失败')</script>";
	}
}

mysqli_close($conn);

?>