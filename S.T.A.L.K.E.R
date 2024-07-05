<!DOCTYPE html>
<html lang="en">
<head>
    <title>S.T.A.L.K.E.R</title>
    <style>
         .black-text {
            color: black;
        }
        /* General Styles */
        body {
            font-family: 'Times New Roman', serif;
            background-color: #fdf1dc;
            color: #3a3b3c;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
            background-color: #fff8f0;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        }

        /* Header Styles */
        header {
            background: url('castle-background.jpg') no-repeat center center/cover;
            color: white;
            padding-top: 30px;
            min-height: 300px;
            border-bottom: 5px 
                solid #d3a625;
            text-align: center; /* Center the title */
        }
        header h1 {
            font-family: 'Papyrus', fantasy;
            font-size: 3em;
            margin: 0;
        }
        /* Navigation Styles */
        nav ul {
            padding: 0;
            margin: 0;
            list-style: none;
            overflow: hidden;
            text-align: center;
        }
        nav ul li {
            display: inline;
        }
        nav ul li a {
            display: inline-block;
            padding: 10px 20px;
            color: #fdf1dc;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.2em;
            transition: color 0.3s;
        }
        nav ul li a:hover {
            color: #d3a625;
        }

        /* Section Styles */
        section {
            padding: 20px;
            text-align: center;
        }
        footer {
            text-align: center;
            padding: 10px;
            color: #fff;
            background-color: #333;
        }

        /* Custom Fonts and Text Styles */
        @import url('https://fonts.googleapis.com/css2?family=Papyrus&display=swap');
    </style>
</head>
<body>
    <header>
    <div class="container black-text">
        <h1><a href="index.html" style="color: black; text-decoration: none;">TheHoboKingdom</a></h1>
    </div>
    </header>
    <nav>
        <ul>
            <li><a href="index.html" class="black-text">Home</a></li>
            <li><a href="S.T.A.L.K.E.R.html" class="black-text">S.T.A.L.K.E.R</a></li>
            <li><a href="dominions.html" class="black-text">Dominions</a></li>
            <li><a href="minecraft.html" class="black-text">Minecraft</a></li>
            <li><a href="baldurs.html" class="black-text">Baldurs Gate 3</a></li>
            <li><a href="dungeons.html" class="black-text">Dungeons & Dragons</a></li>
        </ul>
    </nav>
    <div class="container">
        <section>
            <h2>Welcome To The Baldurs Gate 3 Page.</h2>
            <p>This page is essentially the Minecraft page. Just a collection of mods or modpacks that we may play with. </p>
    </div>
    <footer>
        <p>&copy; TheHoboKingdom</p>
    </footer>
</body>
</html>
