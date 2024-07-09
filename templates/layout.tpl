<!DOCTYPE html>
<html>
    <head>
        <title>{{title or 'No title'}}</title>
        <!--brings the stylesheet into the html -->
        <link href="/static/homepage.css" rel="stylesheet" />         
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    </head>
    <body>       
        <div class="wrapper"> 
            <div class="logo_container"> <!-- Container with the class 'container' that holds the image -->
                <!-- image called and its deimensions specified -->
                <a href="http://localhost:8080/"> <!-- anchors the button/image to the homepage -->
                    <button> <!-- Allows for the image to have the properties of a button when clicked -->
                    <img src="/static/images/CramBerryFinalLogoDesignWithText.png" alt="CramBerry" width="90" height="140" />
                    </button>
                </a>
            </div>
            <div class="table_container">
                <div class="table">
                    <table id="TableMenu" border="1">
                        <tr>
                            <td class="bordered-cell"><a href="/todo">View Open Items</a></td>
                            <td class="bordered-cell"><a href="/new">New Task</a></td>
                        </tr>
                    </table>
                    
                    {{!content}}
                </div>
            </div>
        </div>

    </body>
</html>
