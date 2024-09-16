# Secure Quiz Label Index
> Halogen has just released all the questions to the next CyberSecurity test. Blahaj wants to score full marks, and believes the answers and bonus questions are listed somewhere on the site. Help Blahaj get the answers and score full marks on this quiz!

## Solution
The SQL query being shown gives a hint as to what we need to do. SQL Injection:
https://portswigger.net/web-security/sql-injection

As we are given the code, we see that the flag is inserted as an answer to a hidden question under ID 25. Though SQL injection, we can retrieve it


Payload: `1' UNION SELECT ID, question, answer FROM quizzes WHERE ID = 25--`<br>
Flag: `blahaj{full_m4rk5_guar4nte3d!!}`