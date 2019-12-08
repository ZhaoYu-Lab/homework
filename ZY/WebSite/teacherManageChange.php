<?php
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
//header('Content-type:text/json;charset=utf-8');

$teacherNum = $_POST['teacherNum'];
$teacherName = $_POST['teacherName'];
$teacherSex = $_POST['teacherSex'];

$teacherDepart = $_POST['teacherDepart'];

if ($teacherNum == "") {
	echo "<script>alert('一卡通号为空');location.href='teacherManageChange.html'</script>";
} else if ($teacherName == "") {
	echo "<script>alert('姓名为空');location.href='teacherManageChange.html'</script>";
} else if ($teacherSex == "") {
	echo "<script>alert('性别为空');location.href='teacherManageChange.html'</script>";
} else if ($teacherDepart == "") {
	echo "<script>alert('学院为空');location.href='teacherManageChange.html'</script>";
} else {

	$sql_query = "UPDATE teachers SET teacherName = '$teacherName',teacherSex='$teacherSex',teacherDepart='$teacherDepart',  WHERE teacherNum = '$teacherNum' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据修改成功')</script>";
	} else {
		echo "<script>alert('数据修改失败')</script>";
	}
}
mysqli_close($conn);
?>