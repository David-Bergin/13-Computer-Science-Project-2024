%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the task with ID = {{no}}</p>
<form action="/edit/{{no}}" method="get">
  <input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100">
  <select name="status">
    <option value="1">Todo</option> 
    <option value="2">Doing</option>
    <option value="0">Done</option> 
  </select>
  <br>
  <input type="submit" name="save" value="save">
</form>


