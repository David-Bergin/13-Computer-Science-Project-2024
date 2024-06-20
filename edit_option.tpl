%#template for choosing a task to edit
<p>What ID of the task do you want to edit? </p>
<form action="/edit" method="get">
  <input type="text" name="task" value="" size="25" maxlength="10">
  <br>
  <input type="submit" name="edit" value="edit">
</form>
%rebase layout title='Edit option'
