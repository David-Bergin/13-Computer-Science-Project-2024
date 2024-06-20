
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>

<table border="1" class="center">

  %for row in rows:
    <tr>
      %for col in row:
        <td>{{col}}</td>
      %end
    <td><a href="edit/{{row[0]}}">
          <button class="myButton">Edit</button>
    </a></td>
  %end
</table>

%rebase layout title='Make Table'

