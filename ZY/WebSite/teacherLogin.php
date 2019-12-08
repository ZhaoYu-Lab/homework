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
	die("连接失败: " . mysqli_connect_error());
}
$conn->query("set names utf8");

$uname = $_POST['uname']; //post获得用户名表单值
$pass = $_POST['pass']; //post获得用户密码单值
$role = $_POST["role"];

//没有判断逻辑
if ($role == "教师") {

	$sql = "SELECT * from counsellorInfo where Account = '$uname'"; //检测数据库是否有对应的username和password的sql
	$re = mysqli_query($conn, $sql);
	$n = mysqli_num_rows($re);
	if ($n > 0) {
		while ($date = mysqli_fetch_assoc($re)) {
			if ($date['Account'] == $uname && $date['Pwd'] == $pass) {
				echo "<script>alert('登陆成功');location.href='main.html'</script>";
			} else {
				echo "<script>alert('密码输入错误');location.href='teacherLogin.html'</script>";
			}

		}

	} else {
		echo "<script>alert('用户名不存在');location.href='teacherLogin.html'</script>";
	}

} else if ($role == "辅导员") {
	$sql = "SELECT * from supervisorInfo where Account = '$uname'"; //检测数据库是否有对应的username和password的sql
	$re = mysqli_query($conn, $sql);
	$n = mysqli_num_rows($re);
	if ($n > 0) {
		while ($date = mysqli_fetch_assoc($re)) {
			if ($date['Account'] == $uname && $date['Pwd'] == $pass) {
				echo "<script>alert('登陆成功');location.href='mainS.html'</script>";
			} else {
				echo "<script>alert('密码输入错误');location.href='teacherLogin.html'</script>";
			}

		}

	} else {
		echo "<script>alert('用户名不存在');location.href='teacherLogin.html'</script>";
	}

}

?>