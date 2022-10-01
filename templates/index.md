<!DOCTYPE html>
<html>
 <body>
   <table>
     <tr>
       <th>Date Result</th>
     </tr>
     {% for item in data %}
       <tr>
          <a href="./{{ item }}.md">{{ item }}</a>
       </tr>  
    {% endfor %}
   </table>
 </body>
</html>
