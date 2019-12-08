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

$studentNum = $_POST['studentNum'];
$studentName = $_POST['studentName'];
$studentSex = $_POST['studentSex'];
$studentClass = $_POST['studentClass'];
$studentDepart = $_POST['studentDepart'];
$studentMail = $_POST['studentMail'];

if ($studentNum == "") {
	echo "<script>alert('一卡通号为空');location.href='studentManageAdd.html'</script>";
} else if ($studentName == "") {
	echo "<script>alert('姓名为空');location.href='studentManageAdd.html'</script>";
} else if ($studentSex == "") {
	echo "<script>alert('性别为空');location.href='studentManageAdd.html'</script>";
} else if ($studentClass == "") {
	echo "<script>alert('班级为空');location.href='studentManageAdd.html'</script>";
} else if ($studentDepart == "") {
	echo "<script>alert('学院为空');location.href='studentManageAdd.html'</script>";
} else if ($studentMail == "") {
	echo "<script>alert('邮件为空');location.href='studentManageAdd.html'</script>";
} else {

	$sql_query = "UPDATE students SET studentName = '$studentName',studentSex='$studentSex', studentClass = '$studentClass',studentDepart='$studentDepart', studentMail='$studentMail' WHERE studentNum = '$studentNum' ";

	$result = mysqli_query($conn, $sql_query);
	if (mysqli_affected_rows($conn) > 0) {
		echo "<script>alert('数据修改成功')</script>";
	} else {
		echo "<script>alert('数据修改失败')</script>";
	}
}
mysqli_close($conn);

?>