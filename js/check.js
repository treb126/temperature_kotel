function temp(){
        $.ajax({
           type: "POST",
           url: "engine/ds_pyt_read.php",
           data: {}
         }).done(function(req){
              var temp_arr = req.split("/");
          
              document.getElementById('t1').outerHTML="<div id='t1' style='font-size:20px;display: inline-block; background-color: red;'>Time:"+temp_arr[0]+"<br>Temp 1:"+temp_arr[1]+"</div>";
              document.getElementById('t2').outerHTML="<div id='t2' style='font-size:20px;display: inline-block; background-color: blue;'>Time:"+temp_arr[0]+"<br>Temp 2:"+temp_arr[2]+"</div>";
            });
}