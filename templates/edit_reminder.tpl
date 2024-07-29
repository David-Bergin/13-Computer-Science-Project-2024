%#template for editing the reminders
<p>Make your changes and click save</p>
<form action="/reminders" method="get">
  <textarea name="reminder" maxlength="200" rows="5">{{reminder[0]}}</textarea>  
  <br><br>
  <input type="submit" name="save" value="Save" class="btn btn-success">
</form>


