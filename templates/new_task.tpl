%#template for the form for a new task
<p>Add a new task to the ToDo list:</p>
<form action="/new" method="GET">
  <input type="text" maxlength="100" name="task">
  <input type="submit" name="save" value="Save" class="btn btn-success">
</form>
