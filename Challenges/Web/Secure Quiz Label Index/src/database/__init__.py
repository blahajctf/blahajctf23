# Initialise the database
import sqlite3 
import sys
flag = "blahaj{full_m4rk5_guar4nte3d!!}"

from pathlib import Path
CWD = Path(__file__).parent.resolve()
class SQL:
    def __init__(self):
        self.con = sqlite3.connect('/data/scratch/Database.db')

    def execute(self, query):
        cur = self.con.execute(query)
        return cur.fetchall()


# Intialize the database
cur = SQL()

#Create data for the user table
cur.execute("DROP TABLE IF EXISTS quizzes;")
cur.execute("CREATE TABLE quizzes (ID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT, Setter TEXT, Answer TEXT, Visible BOOLEAN)")
cur.execute(f"""INSERT INTO quizzes(question, setter, answer, visible) VALUES
    ('What is the name of the CTF competition held annually at the Chaos Communication Congress (CCC)?', 'Halogen', 'CTF', 1),
    ('What is the best plush toy?', 'Halogen', 'BLÅHAJ', 1),
    ('What type of CTF challenge involves reverse engineering binary files to find vulnerabilities?', 'Halogen', 'Binary Exploitation', 1),
    ('What is the name of the popular CTF platform that hosts online competitions and provides a wide range of challenges?', 'Halogen', 'CTFd', 1),
    ('What is a math equation of all time?', 'Halogen', '1 = 2', 1),
    ('Which famous CTF competition is hosted annually by DEF CON?', 'Halogen', 'Capture The Flag (CTF)', 1),
    ('In CTF, what is the term for a challenge that requires participants to reverse engineer and analyze malware?', 'Halogen', 'Malware Analysis', 1),
    ('In CTF, what term is used to describe a challenge where participants need to find and exploit a web application vulnerability?', 'Halogen', 'Web Exploitation', 1),
    ('In CTF, what term describes a challenge that requires participants to find and exploit vulnerabilities in a mobile app?', 'Halogen', 'Mobile Exploitation', 1),
    ('What type of CTF challenge focuses on identifying and exploiting vulnerabilities in network services?', 'Halogen', 'Pwn (Exploit)', 1),
    ('In a CTF challenge, what is the term for a vulnerability that allows an attacker to read sensitive information from a system?', 'Halogen', 'Information Disclosure', 1),
    ('What does the term "XSS" stand for in the context of web security and CTF challenges?', 'Halogen', 'Cross-Site Scripting', 1),
    ('In CTF, what is the term for a challenge where participants need to decrypt a message or data?', 'Halogen', 'Crypto', 1),
    ('What does the acronym "CTF" stand for in the context of cybersecurity?', 'Halogen', 'Capture The Flag', 1),
    ('Which programming language is commonly used for web exploitation challenges in CTF competitions?', 'Halogen', 'Python', 1),
    ('Can you hack this website?', 'Halogen', 'Yes, on the listing page 🤔', 1),
    ('Which popular Linux distribution is commonly used for CTF challenges due to its lightweight nature and tools availability?', 'Halogen', 'Kali Linux', 1),
    ('In a CTF challenge, what is the term for a small piece of code or data that grants access to a system?', 'Halogen', 'Flag', 1),
    ('Which CTF category involves solving puzzles, riddles, and ciphers to find hidden information or flags?', 'Halogen', 'Forensics', 1),
    ('What is the name of the largest annual international CTF competition held in Las Vegas, USA?', 'Halogen', 'DEF CON Capture The Flag', 1),
    ('Is there even a flag?',  'Halogen', 'Yes there is, I think', 1),
    ('In CTF, what term describes a vulnerability that allows an attacker to execute arbitrary code on a target system?', 'Halogen', 'Remote Code Execution (RCE)', 1),
    ('What protocol is often used for secure communication in CTF challenges, providing encryption and authentication?', 'Halogen', 'TLS/SSL', 1),
    ('What is SQL Injection (SQLi)?', 'Halogen', 'Improperly sanitised SQL Query', 1),
    ('What is the flag?',  'Halogen', '{flag}', 0);
""")

cur.con.commit()