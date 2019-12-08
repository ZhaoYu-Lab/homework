<?php
header("Content-Type: text/html; charset=utf8");
//面向过程语法
$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

// 面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (mysqli_connect_errno($conn)) {
	die("连接失败: " . mysqli_connect_error());
}

$studentNum = $_POST['addNum'];
$studentPass = $_POST['addPass'];
if ($studentNum == "") {
	echo "<script>alert('一卡通号为空');location.href='studentLoginManageAdd.html'</script>";
} else if ($studentPass == "") {
	echo "<script>alert('密码为空');location.href='studentLoginManageAdd.html'</script>";
} else {

	$sql_query = "INSERT INTO studentInfo(Account,Pwd) VALUES('$studentNum','$studentPass') ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据添加成功')</script>";
	} else {
		echo "<script>alert('数据添加失败')</script>";
	}
}
mysqli_close($conn);

?>