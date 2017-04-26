//show hide Abstract part
var list = ["Introduction", "Setup","Syntax","Variables","Functions","Algorithms","Requirements","Systems","Hardware","DeviceUsage","Controls","Capabilities","Bugs","FutureDevelopment"];

function sh(s) {
     var i = 0;
     while(i<= list.length)
     {
        var x = document.getElementById(list[i]);
        if(list[i]==s)
        {
            x.style.display = 'block';
        }
        else
        {
             x.style.display = 'none';
        }
        i++;
     }

}



