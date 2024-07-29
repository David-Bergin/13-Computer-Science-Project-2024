<h3>Timetable for this week</h3>
<div class="table-responsive">
  <table class="table table-striped">        
  <tr>
    <th scope="col">Weekday</th>
    <th scope="col">Homeroom</th>
    <th scope="col">Period 1</th>
    <th scope="col">Period 2</th>
    <th scope="col">Period 3</th>        
    <th scope="col">Period 4</th>
    <th scope="col">Period 5</th>          
  </tr>
  %for day, details in timetable_data.items():
    <tr>     
        <td>{{ day }}</td>
        <td>                
            {{ details['homeroom_subject'] }}  
        </td>
        <td>                
            {{ details['period1_subject'] }}  
        </td>
        <td>                
            {{ details['period2_subject'] }}  
        </td>
        <td>                
            {{ details['period3_subject'] }}  
        </td>
        <td>                
            {{ details['period4_subject'] }}  
        </td>
        <td>                
            {{ details['period5_subject'] }}  
        </td>              
    </tr>
  %end      
</table>
