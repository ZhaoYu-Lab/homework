<?php
//header('Content-type:text/html;charset=utf-8');
header("Content-Type: text/html; charset=utf8");

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

$addNum = $_POST['addNum'];
$addName = $_POST['addName'];
$addSex = $_POST['addSex'];
$addClass = $_POST['addClass'];
$addDepart = $_POST['addDepart'];
$addMail = $_POST['addMail'];

if ($addNum == "") {
	echo "<script>alert('一卡通号为空');location.href='studentManageAdd.html'</script>";
} else if ($addName == "") {
	echo "<script>alert('姓名为空');location.href='studentManageAdd.html'</script>";
} else if ($addSex == "") {
	echo "<script>alert('性别为空');location.href='studentManageAdd.html'</script>";
} else if ($addClass == "") {
	echo "<script>alert('班级为空');location.href='studentManageAdd.html'</script>";
} else if ($addDepart == "") {
	echo "<script>alert('学院为空');location.href='studentManageAdd.html'</script>";
} else if ($addMail == "") {
	echo "<script>alert('邮件为空');location.href='studentManageAdd.html'</script>";
} else {
	$sql_query = "INSERT INTO students VALUES('$addNum','$addName','$addSex','$addClass','$addDepart','$addMail') ";
	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据添加成功')</script>";
	} else {
		echo "<script>alert('数据添加失败')</script>";
	}
}

mysqli_close($conn);

?>