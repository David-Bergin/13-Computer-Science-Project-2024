
<table>
  <tr>
    <td>
      <h3>Timetable for this week</h3>
      <table border="1" class="center">        
        <tr>
          <td>Weekday</td>
          <td>Homeroom</td>
          <td>Period 1</td>
          <td>Period 2</td>
          <td>Period 3</td>        
          <td>Period 4</td>
          <td>Period 5</td>
          <td>Period 6</td>          
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
              <td>                
                  {{ details['period6_subject'] }}  
              </td>
          </tr>
        %end      
      </table>
    </td>    
  </tr>
</table>
