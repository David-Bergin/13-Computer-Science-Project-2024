
%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p>The open items are as follows:</p>

<table>
  <tr>
    <td class="kanban_column">
      <h3>To do</h3>
      <table class="kanban_table">
        %for row in rows_todo:
          <tr>            
              <td class="kanban">
                <a class="btn btn-outline-primary" href="edit/{{row[0]}}">
                  {{row[1]}}                
                </a>
              </td>
          </tr>
        %end
      </table>
    </td>
    <td class="kanban_column">
      <h3>Doing</h3>
      <table class="kanban_table">

        %for row in rows_doing:
         <tr>            
              <td class="kanban">
                <a class="btn btn-outline-success" href="edit/{{row[0]}}">
                  {{row[1]}}                
                </a>
              </td>
          </tr>
        %end
      </table>
    </td>
    <td class="kanban_column">
      <h3>Done</h3>
      <table class="kanban_table">

        %for row in rows_done:
          <tr>            
              <td class="kanban">
                <a class="btn btn-outline-secondary" href="edit/{{row[0]}}">
                  {{row[1]}}                
                </a>
              </td>
          </tr>
        %end
      </table>
    </td>
  </tr>
</table>
