
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>

<table>
  <tr>
    <td>
      <h3>To do</h3>
      <table border="1" class="center">

        %for row in rows_todo:
          <tr>
            %for col in row:
              <td>{{col}}</td>
            %end
          <td><a href="edit/{{row[0]}}">
                <button class="myButton">Edit</button>
          </a></td>
        %end
      </table>
    </td>
    <td>
      <h3>Doing</h3>
      <table border="1" class="center">

        %for row in rows_doing:
          <tr>
            %for col in row:
              <td>{{col}}</td>
            %end
          <td><a href="edit/{{row[0]}}">
                <button class="myButton">Edit</button>
          </a></td>
        %end
      </table>
    </td>
    <td>
      <h3>Done</h3>
      <table border="1" class="center">

        %for row in rows_done:
          <tr>
            %for col in row:
              <td>{{col}}</td>
            %end
          <td><a href="edit/{{row[0]}}">
                <button class="myButton">Edit</button>
          </a></td>
        %end
      </table>
    </td>
  </tr>
</table>
