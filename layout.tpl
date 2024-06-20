<!DOCTYPE html>
<html>
    <head>
        <title>{{title or 'No title'}}</title>
        <!--brings the stylesheet into the html -->
        <link href="/static/style.css" rel="stylesheet" /> 
    </head>
    <body>
        <table id="TableMenu" border="1">
            <tr>
                <td class="bordered-cell"><a href="/todo">View Open Items</a></td>
                <td class="bordered-cell"><a href="/new">New Task</a></td>
            </tr>
        </table>
        
        %include
    
    </body>
</html>
