<!DOCTYPE html>
<html>
 <body>
   <table>
     <tr>
       <th>Date Result</th>
     </tr>
     {% for item in data %}
       <tr>
          <td> <a href="./results/{{ item }}.md">{{ item }}</a></td>
       </tr>  
    {% endfor %}
   </table>
 </body>
</html>
