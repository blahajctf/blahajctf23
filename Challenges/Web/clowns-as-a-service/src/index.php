<?php

$secret = 'honestly put anything here can nobody cares, it doesnt even matter lol lmao';
$flag = 'blahaj{php_is_the_biggest_clown_of_all_the_clowns}';

$inputsecret = $_POST['secret'];
$meaningoflife = $_POST['meaningoflife'];

# Check if the secret is correct
if (strcmp($inputsecret, $secret) != 0) {
    echo 'come back with correct secret';
}
else{
    # Check if the meaning of life is correct
    if (hash('sha1',$meaningoflife) != 42) {
        echo 'come back with correct meaning of life';
    }
    else{
        echo 'flag: ' . $flag;
    }
}

?>