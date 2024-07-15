

header = """
        <div class="nav-bar">
                <div class="flex-Container">
                        <div><span class="fname">Restituto</span>Rodeo Jr.</div>
                </div>
        </div>
        
        <style>
        :root {
                --max-width: 1900px; /* Default maximum width */
        }
        .st-emotion-cache-z5fcl4{padding: 0;}
        .st-emotion-cache-v09qz{gap:0;}

        .nav-bar {
                position: fixed;
                top:0;
                left:0;
                right:0;
                background-color: rgba(0, 0, 0, 0.5);
                max-width: var(--max-width);
                margin: 0 auto;
                z-index: 3;
        }
        .nav-bar > .flex-Container{      
                display: flex;
                align-items: center;}
        .flex-Container{
                width: 70%;
                padding: 25px 0;
                margin:0 auto;
        }
        .flex-Container > div > .fname {color:#ff5d56;}
        .flex-Container > div {
                font-family: 'Berkshire Swash', cursive;
                color: White;
                margin: 0px;
                padding: 2.5px;
                font-size: 30px;}
        h2{Color:black}
        </style>
        """

# banner = """
#         <div class="banner">
#         </div>
#         <style>
#         .banner{
#                 position: relative;
#                 top: 0px;
#                 left: 0px;
#                 width: 100%;
#                 background:url('./images/banner.png') no-repeat top;
#                 background-size:cover;
#                 background-position: center;
#                 padding: 550px 0 120px;
#                 }
#         </style>
# """

animated_word = """
        <div>
                <span class="want-to-be">
                        Data Analyst
                </span>
        </div>
        <style>
        .want-to-be{
                font-size:5rem;
                padding: 1rem:
                margin: 0;
                color: #ff5d56;
                }
        </style>

"""

about_me = """
        <div class="center1">
                <h1 class="about">About Me</h1>
                <span>Professional Profile - There Is All About Me</span>
        </div>
        
        <style>
        
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-weigth: 20px;
                font-size: 35px;
                }
        </style>
"""

details_aboutme = """
        <div class="flex-container">
                <div class="flex-columns">
                        <ul>
                                <li><b>Date of birth:</b> 10 March 2000</li>
                                <li><b>Nationality:</b> Filipino</li>
                                <li><b>Freelance:</b> N/A</li>
                                <li><b>Phone:</b> +639602498779</li>
                        </ul>
                </div>
                <div class="flex-columns">
                        <ul>
                                <li><b>Address:</b> Manila, Philippines</li>
                                <li><b>Email:</b> restitutorodeo@gmail.com</li>
                                <li></i><b>Spoken Languages:</b> Tagalog, English</li>
                                <li><b>Telegram:</b> <i><a href="https://t.me/Restituto_Rodeo" class="link">@Restituto_Rodeo</a></i></li>
                        </ul>
                </div>

        </div>
        <style>
        .link{
                text-decoration: none;
        }
        .link:hover{
                text-decoration: none;
        }
        
        .flex-container{
                display: flex;
                width: 100%;
                margin: 15px 0;
        }
        .flex-columns{
                width: 100%;
                margin: 0 20px;
        }
        </style>
"""

#--------------------------------------------------------------------------------
new_banner_html = """
        <div class="container">
                <div class="column2">
                    <div class="column1">
                        <div class="col-1">
                                <h3 class="h3">Hello There! I\'m </b>Aspiring</b></h3>
                                <span class="want-to-be">Data Analyst</span>
                                <span>I organize data for analysis and I\'m eager to learn more. I want to help teams make better decisions using various tools like Excel for data manipulation, SQL for database querying, and visualization tools like Tableau, Power BI, and Python for analysis.</span>
                        </div>
                    </div>
                </div>
        </div>
                """

new_banner_css = """
        <style>
                .container {
                        top: 0px;
                        left: 0px;
                        height: 70%; /* Take full height of parent container */
                        background: url("../images/banner.png") no-repeat top;
                        background-size:cover;
                        background-position: center;
                        z-index: 0; /* Ensure column2 appears below column1 */
                }
                .column1 {
                        display: flex;
                        width: 70%;
                        height: 70vh; /* Take full height of parent container */
                        margin: 0 auto;
                        align-items: center;
                        /* background-color: red;*/
                        z-index: 1; /* Ensure column1 appears above column2 */
                }
                .column2 {
                        position: relative;
                        width: 100%;
                }
                .col-1 {
                        display: grid;
                        margin: 0 50% 0 0;
                }
                .h3 {
                        margin:0;
                        padding: 0;
                }
                .want-to-be{
                        font-size:5rem;
                        padding: 0;
                        margin: 0;
                        color: #ff5d56;
                }
        </style>
    """

Name = """
        <div>
                <span class="h3">I'm Restituto Rodeo Jr.</span>
        </div>    
        <style>.h3{font-size: 30px;}</style>            
"""
Nameko = """
        <div class="nmae-con">
                <span class="nmae">Restituto Rodeo Jr.</span>
        </div>    
        <style>.nmae{font-size: 30px;} 
                .nmae-con{text-align: center;}</style>            
"""

projects = """
        <div class="center1">
                <h1 class="about">Personal Projects</h1>
                <span></span>
        </div>
        
        <style>
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-size: 35px;
                }
        </style>
"""
skills = """
        <div class="center1">
                <h1 class="about">Skills</h1>
                <span></span>
        </div>
        
        <style>
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-size: 35px;
                }
        </style>
"""

certificates = """
        <div class="center1">
                <h1 class="about">Certificates</h1>
                <span></span>
        </div>
        
        <style>
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-size: 35px;
                }
        </style>
"""
other_certificates = """
        <div class="center1">
                <h1 class="about">Other Certificates</h1>
                <span></span>
        </div>
        
        <style>
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-size: 35px;
                }
        </style>
"""

education = """
        <div class="center1">
                <h1 class="about">Education</h1>
                <span></span>
        </div>
        
        <style>
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-size: 35px;
                }
        </style>
"""

contact = """
        <div class="center1">
                <h1 class="about">Contact</h1>
                <span></span>
        </div>
        
        <style>
        .about {
                font-family: 'Berkshire Swash', cursive;
                font-style: normal;
                font-size: 35px;
                }
        </style>
"""


hr = """
        <hr class="hr"></hr>
        <style>
        .hr {
                max-width: var(--max-width);
                width: 70%;
                margin: 2em auto;
                border-bottom: 2px solid #ff5d56;
}
        </style>
"""

contact_form = """
    <form action="https://formsubmit.co/restitutorodeo@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message here" required></textarea>
     <button type="submit">Send</button>
</form>

"""

bible_verse = """
        <div class="center_text">
                <h5><b>Philippians 4:6</b></h5>
                <p><em>Don't worry about anything: instead pray about everything. Tell God what you need, and thank Him for all He has done.</em></p>
        </div>
        <style>
                .center_text{
                        text-align: center;
                        margin: 0 10%;
                }
        </style>
"""

font_awesome_link ="""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
"""

social_links = """
        <div class="link-con">
                <div class="link-child">
                        <a href="https://t.me/Restituto_Rodeo"><i class="fa fa-telegram icon"></i></a>
                        <a href="https://github.com/magan10"><i class="fa fa-github icon"></i></a>
                        <a href="https://www.linkedin.com/in/restituto-rodeo-jr/"><i class="fa fa-linkedin-square icon"></i></a>
                </div>
        </div>

        <style>
                .link-con{
                        position: relative;
                        width: 70%;
                        margin: 0 auto;
                }
                .link-child {
                        text-align: center;
                }
                .icon{
                        font-size:36px;
                        color: #ff5d56;
                        padding: 0 20px;
                }
        </style>
"""

