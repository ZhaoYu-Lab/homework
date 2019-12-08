<?php
require_once 'PHPMailer/src/PHPMailer.php';
require_once 'PHPMailer/src/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;

$servername = "localhost";
$username = "zhaoyu_test_com";
$password = "2an7MKAcJc8ERHTe";
$dbname = "zhaoyu_test_com";

//面向过程语法
$conn = mysqli_connect($servername, $username, $password, $dbname);
if (!$conn) {
	die("连接失败: " . $conn->connect_error);
}
header('Content-type:text/json;charset=utf-8');

$studentNum = $_POST['choosen'];

$sql = "SELECT * FROM students WHERE studentNum = '$studentNum' ";
$result = $conn->query($sql);
if (mysqli_num_rows($result) > 0) {
	// 输出数据
	while ($row = $result->fetch_assoc()) {
		$mail = $row["studentMail"];
	}
}

class QQMailer {
	public static $HOST = 'smtp.qq.com'; // QQ 邮箱的服务器地址
	public static $PORT = 465; // smtp 服务器的远程服务器端口号
	public static $SMTP = 'ssl'; // 使用 ssl 加密方式登录
	public static $CHARSET = 'UTF-8'; // 设置发送的邮件的编码

	private static $USERNAME = '1054812428@qq.com'; // 授权登录的账号
	private static $PASSWORD = 'qvzpepxdlxdxbdih'; // 授权码
	private static $NICKNAME = 'Tom'; // 发件人的昵称

	/**
	 * @param bool $debug [调试模式]
	 */
	public function __construct($debug = false) {
		$this->mailer = new PHPMailer();
		$this->mailer->SMTPDebug = $debug ? 1 : 0;
		$this->mailer->isSMTP(); // 使用 SMTP 方式发送邮件
	}

	/**
	 * @return PHPMailer
	 */
	public function getMailer() {
		return $this->mailer;
	}

	/**
	 * 加载配置
	 * [loadConfig description]
	 */
	private function loadConfig() {
		/* Server Settings  */
		$this->mailer->SMTPAuth = true; // 开启 SMTP 认证
		$this->mailer->Host = self::$HOST; // SMTP 服务器地址
		$this->mailer->Port = self::$PORT; // 远程服务器端口号
		$this->mailer->SMTPSecure = self::$SMTP; // 登录认证方式
		/* Account Settings */
		$this->mailer->Username = self::$USERNAME; // SMTP 登录账号
		$this->mailer->Password = self::$PASSWORD; // SMTP 登录密码
		$this->mailer->From = self::$USERNAME; // 发件人邮箱地址
		$this->mailer->FromName = self::$NICKNAME; // 发件人昵称（任意内容）
		/* Content Setting  */
		$this->mailer->isHTML(true); // 邮件正文是否为 HTML
		$this->mailer->CharSet = self::$CHARSET; // 发送的邮件的编码
	}

	/**
	 * 发送邮件
	 * @param $email [收件人]
	 * @param $title [主题]
	 * @param $content [正文]
	 * @return bool [发送状态]
	 */
	public function send($email, $title, $content) {
		$this->loadConfig();
		$this->mailer->addAddress($email); // 收件人邮箱
		$this->mailer->Subject = $title; // 邮件主题
		$this->mailer->Body = $content; // 邮件信息
		return (bool) $this->mailer->send(); // 发送邮件
	}
}
// 测试
// 实例化 QQMailer 类
$mailer = new QQMailer(true);
// 邮件标题
$title = '测试邮件';
// 邮件内容
$content = <<< EOF
<p align="center">
预警预警预警
</p>
EOF;

// 发送QQ邮件
$mailer->send($mail, $title, $content);

mysqli_close($conn);

?>