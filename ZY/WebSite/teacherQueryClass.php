<?php
header('Content-type:text/json;charset=utf-8');

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

// 面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . mysqli_connect_error());
}

$courseName = $_POST['courseName'];
$className = $_POST['className'];
$starTime = $_POST['starTime'];
$endTime = $_POST['endTime'];

$sql1 = "SELECT * FROM courses WHERE courseName = '$courseName' ";
$result1 = mysqli_query($conn, $sql1);

if (mysqli_num_rows($result1) > 0) {
	// 输出数据
	while ($row = mysqli_fetch_assoc($result1)) {
		$courseNum = $row["courseNum"];
	}

	if ($starTime == "" || $endTime == "") {
		//echo "<script>alert('没有选择时间段将查询班级全部签到信息')'</script>";
		$sql_query = "SELECT * FROM sign";
	} else {
		$sql_query = "SELECT * FROM sign WHERE studentClass = '$className' and  courseNum ='$courseNum' and  startTime between '$starTime' and  '$endTime'";
	}

	$result2 = mysqli_query($conn, $sql_query);
	$jsonArray = array(); // 新建数据用于接收数据库每行对应的数据组
	while ($rows = mysqli_fetch_assoc($result2)) {
		// 把数据库的内容添加到新建数组中
		array_push($jsonArray, $rows); // 注意这里是$rows
	}
	echo json_encode($jsonArray); // 转换成json传递给前端
}

/*$data=' { className:" ' . $className .'",starTime:"' . $starTime. '",courseName:"' . $courseName .'" } ';//组合成json格式数据
echo json_encode($data);//输出json数据*/

mysqli_close($conn);

?>