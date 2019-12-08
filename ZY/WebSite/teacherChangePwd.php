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

$uname = $_POST['uname']; //post获得用户名表单值
$oldPass = $_POST['oldPass']; //post获得用户密码单值
$newPass = $_POST['newPass'];
$confirmPass = $_POST['confirmPass'];

if ($newPass != $confirmPass) {
	echo "<script>alert('两次密码输入不一致');location.href='teacherChangePwd.html'</script>";
} else {

	$sql = "SELECT Account,Pwd from counsellorInfo where Account = '$uname' and Pwd ='$oldPass' "; // 检测数据库是否有对应的username和password的sql
	$result = mysqli_query($conn, $sql);

	if (mysqli_num_rows($result)) {
		$sql1 = "UPDATE  counsellorInfo SET Pwd = '$newPass' where Account = '$uname'";
		$result1 = mysqli_query($conn, $sql1);

		if (mysqli_affected_rows($conn) > 0) {
			echo "<script>alert('教师密码修改成功');location.href='index.html'</script>";
		} else {
			echo "<script>alert('教师密码修改失败');location.href='teacherChangePwd.html'</script>";
		}

	} else {
		echo "<script>alert('原用户名密码不匹配');location.href='teacherChangePwd.html'</script>";
	}
}

?>