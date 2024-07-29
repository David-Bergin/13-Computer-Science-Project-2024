<!DOCTYPE html>
<html>
    <head>
        <!-- bring in Bootstrap framework to help with aesthetics of UI -->
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">  
        
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
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
</html>
