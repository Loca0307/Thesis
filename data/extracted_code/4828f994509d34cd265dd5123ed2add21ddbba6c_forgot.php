// deepcode ignore PhpSameEvalBinaryExpressionfalse: <please specify a reason of ignoring this>
if (isset($nickname) && !empty($nickname) && isset($key) && !empty($key) && $pwdchanged != true) {
	try {
		$pdo = new PDO($dsn, DB_USERNAME, DB_PASSWORD, $db_options);
		switch (DB_DRIVER) {
			case "mysql":
				$stmt = $pdo->prepare("SELECT forgottoken FROM users WHERE nickname = :nickname");
				break;
			case "pgsql":
				$stmt = $pdo->prepare("SELECT forgottoken FROM users WHERE lower(nickname) = :nickname");
				break;
		}
		$stmt->bindValue(":nickname", $nickname);
		$stmt->execute();
		$pdo = null;
	} catch (PDOException $e) {
		error_log($langArray['invalid_query'] . ' ' . $e->getMessage() . '\n' . $langArray['whole_query'] . ' ' . $stmt->queryString, 0);
	}
	$sqlresults = $stmt->fetch(PDO::FETCH_ASSOC);
	$forgottoken = $sqlresults["forgottoken"];

	if (mb_strtolower($key) === mb_strtolower($forgottoken)) {
		require 'includes/header.php';
		print '<form class="srs-container" method="POST" action="' . $_SERVER["PHP_SELF"] . '?nickname=' . $nickname . '&key=' . $forgottoken . '">
<span class="srs-header">' . $langArray['new_password'] . '</span>

<div class="srs-content">
	<a href="#" id="passwordRequirements">' . $langArray['password_requirements'] . '</a><br>
	<div class="bubble-container">
			<div class="bubble" id="bubblePopup">
			' . $langArray['password_requirements_text'] . '
			<button id="closePopup">' . $langArray['close_btn'] . '</button>
			</div>
    <label for="password" class="srs-lb">' . $langArray['password'] . '</label><input name="password" id="password" type="password" class="srs-tb"><br>
    <span id="pwstatus"></span><br>
	</div>
    <label for="password2" class="srs-lb">' . $langArray['repeat_password'] . '</label><input name="password2" id="password2" type="password" class="srs-tb"><br>
</div>
<div class="srs-footer">
	<div class="srs-button-container">
<input type="submit" value="' . $langArray['change_password_button'] . '" class="srs-btn">
</div>
<div class="srs-slope"></div>
</div>
</form>
<br><br>
<script src="./js/pwdreq.js"></script>
<script src="./js/pwdcheck.js"></script>';
		require 'includes/footer.php';
	} else {
		require 'includes/header.php';
		print '<span class="srs-header">' . $langArray['forgot_password_heading'] . ' - ' . $langArray['error'] . '</span>
<div class="srs-content">
' . $langArray['wrong_nickname_or_verification_key'] . '
</div><br><br><br>';
		require 'includes/footer.php';
		exit();
	}
	;
} elseif (!empty($email)) {
	require 'includes/header.php';
	print '<span class="srs-header">' . $langArray['new_password'] . ' - ' . $langArray['email'] . '</span>
<div class="srs-content">
' . $langArray['email_sent_instruction_page_text'] . '
</div><br><br><br>';
	require 'includes/footer.php';
	try {
		$pdo = new PDO($dsn, DB_USERNAME, DB_PASSWORD, $db_options);
		$stmt = $pdo->prepare("SELECT nickname FROM users WHERE email=:email");
		$stmt->bindValue(":email", $email);
		$stmt->execute();
		$sqlresults = $stmt->fetch(PDO::FETCH_ASSOC);
		if ($stmt->rowCount() === 1) {
			$nickname = mb_strtolower($sqlresults['nickname']);
			$randomkey = genRandomKey();
			$pdo = null;

			$pdo = new PDO($dsn, DB_USERNAME, DB_PASSWORD, $db_options);
			switch (DB_DRIVER) {
				case "mysql":
					$stmt = $pdo->prepare("UPDATE users SET forgottoken=:randomkey WHERE nickname=:nickname");
					break;
				case "pgsql":
					$stmt = $pdo->prepare("UPDATE users SET forgottoken=:randomkey WHERE lower(nickname) = :nickname");
					break;
				default:
					throw new Exception("unsupported_database_driver");
			}
			$stmt->bindValue(":randomkey", $randomkey);
			$stmt->bindValue(":nickname", $nickname);
			$stmt->execute();
			$pdo = null;
			$from_name = htmlspecialchars(trim($from_name), ENT_QUOTES, 'UTF-8');
			$from_mail = filter_var($from_mail, FILTER_VALIDATE_EMAIL);
			if (!$from_mail) {
				error_log('Invalid sender email address: ' . $from_mail);
				exit('Invalid sender email address');
			}
			
			// Verify the email exists in the database
			$stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE email = :email");
			$stmt->bindValue(':email', $email);
			$stmt->execute();
			if ($stmt->fetchColumn() === 0) {
				exit('Email address not found');
			}
			
			// Rate limiting to prevent abuse
			if (!isset($_SESSION['email_attempts'])) {
				$_SESSION['email_attempts'] = 0;
			}
			if ($_SESSION['email_attempts'] >= 5) {
				exit('Too many email attempts. Please try again later.');
			}
			$_SESSION['email_attempts']++;
			
			// Ensure HTTPS is used
			if (empty($_SERVER['HTTPS']) || $_SERVER['HTTPS'] !== 'on') {
				exit('Secure connection required');
			}
			
			$mailheaders = "From: {$from_name} <{$from_mail}>\r\n";
			$mailheaders .= "X-Mailer: Seat Reservation/2.0";
			$linkPath = '/forgot.php';
			$baseUrl = 'https://' . $_SERVER['SERVER_NAME'] . $linkPath;
			$resetLink = $baseUrl . '?nickname=' . urlencode($nickname) . '&key=' . urlencode($randomkey);
			$mailmsg = $langArray['email_change_password_body_hi'] . " " . htmlspecialchars($nickname) . "\n\n" .
				$langArray['email_change_password_body_link'] . "\n\n" .
				$resetLink;
			
			// Log email-sending activity for debugging
			// error_log("Password reset email sent to: {$email}");
			
			mail($email, $mail_subject, $mailmsg, $mailheaders);
		}
	} catch (PDOException $e) {
		error_log($langArray['invalid_query'] . ' ' . $e->getMessage() . '\n' . $langArray['whole_query'] . ' ' . $stmt->queryString, 0);
	}
} else {
	if ($pwdchanged != true) {
		require 'includes/header.php';
		print '<form class="srs-container" method="POST" action="' . htmlspecialchars($_SERVER["PHP_SELF"]); . '">
<span class="srs-header">' . $langArray['forgot_password_heading'] . '</span>
<div class="srs-content">
	<label for="email" class="srs-lb">' . $langArray['email'] . '</label><input name="email" value="" id="email" class="srs-tb"><br>
</div>
<div class="srs-footer">
	<div class="srs-button-container">
		<input type="submit" class="submit" name="regsubmit" value="' . $langArray['continue'] . '">
	</div>
	<div class="srs-slope"></div>
</div>
</form><br>';
		require 'includes/footer.php';
	}
	;