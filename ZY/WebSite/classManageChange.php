<?php
header('Content-type:text/html;charset=utf-8');

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . $conn->connect_error);
}
//header('Content-type:text/json;charset=utf-8');

$classNum = $_POST['classNum'];
$classLon = $_POST['classLon'];
$classLat = $_POST['classLat'];

if ($classNum == "") {
	echo "<script>alert('教室编号为空');location.href='classManageChange.html'</script>";
} else if ($classLon == "") {
	echo "<script>alert('教室纬度为空');location.href='classManageChange.html'</script>";
} else if ($classLat == "") {
	echo "<script>alert('教师经度为空');location.href='classManageChange.html'</script>";
} else {
	$sql_query = "UPDATE classes SET classLon = '$classLon',classLat='$classLat'WHERE classNum = '$classNum' ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据添加成功')</script>";
	} else {
		echo "<script>alert('数据添加失败')</script>";
	}
}
mysqli_close($conn);

?>