

function klikk(){
var dag = document.getElementById("dag").value;
var month = document.getElementById("month").value;
var year = document.getElementById("year").value;
var tusen = document.getElementById("tusen").value;
var sjekk = Number.isInteger(tusen/400);



if(tusen==2200){
    var x=5;
    }
    

else if(tusen==2100){
    var x=0;
    }
    


else if(tusen==2000){
var x=2;
}

else if(tusen==1900){
 var x=3;
    }
    
    else if(tusen==1800){
        var x=5;
           }

           else if(tusen==1700){
            var x=0;
               }
    



    if(month==1 && sjekk==true){
        var y=4;
        var sum = dag-y; 
        
        if(sum < 0){
        sum=sum+7;
        
        }
            } 







if(month==1 && sjekk==false){
    var y=3;
    var sum = dag-y; 
    
    if(sum < 0){
    sum=sum+7;
    
    }
} 

if(month==2 && sjekk==true){
var y=29;
var sum = dag-y; 

if(sum < 0){
sum=sum+35;

}
    } 

if(month==2 && sjekk==false){
        var y=28;
        var sum = dag-y; 
        
        if(sum < 0){
        sum=sum+35;
        
        }
            } 


if(month==3){
var y=14;
var sum = dag-y; 

if(sum < 0){
sum=sum+14;
                
                }
} 

if(month==4){
var y=4;
var sum = dag-y; 

if(sum < 0){
sum=sum+7;
                                        
 }
} 

if(month==5){
    var y=9;
    var sum = dag-y; 
    
    if(sum < 0){
    sum=sum+14;
                                            
     }
    } 
              
if(month==6){
    var y=6;
    var sum = dag-y; 
        
    if(sum < 0){
    sum=sum+7;
                                                
         }
        } 

if(month==7){
            var y=11;
            var sum = dag-y; 
                
            if(sum < 0){
            sum=sum+14;
                                                        
                 }
                } 

if(month==8){
                    var y=8;
                    var sum = dag-y; 
                        
                    if(sum < 0){
                    sum=sum+14;
                                                                
                         }
                        } 
                                
        
if(month==9){
    var y=5;
    var sum = dag-y; 
        
    if(sum < 0){
    sum=sum+14;
                                                
         }
        } 

        if(month==10){
            var y=10;
            var sum = dag-y; 
                
            if(sum < 0){
            sum=sum+14;
                                                        
                 }
                } 
                                    
if(month==11){
    var y=7;
    var sum = dag-y; 
        
    if(sum < 0){
    sum=sum+14;
                                                
         }
        } 

        if(month==12){
            var y=12;
            var sum = dag-y; 
                
            if(sum < 0){
            sum=sum+14;
                                                        
                 }
                } 


var ar = year-tusen;

var skuddar = Math.floor((year-tusen)/4);

var ukedag = ar+skuddar+x+sum;
if(ukedag > 6){
ukedag= ukedag % 7;

}




if(ukedag==0){
document.getElementById("ukedag").innerHTML="Søndag"
}

if(ukedag==1){
    document.getElementById("ukedag").innerHTML="Mandag"
    }

if(ukedag==2){
    document.getElementById("ukedag").innerHTML="Tirsdag"
        }

if(ukedag==3){
            document.getElementById("ukedag").innerHTML="Onsdag"
                }

if(ukedag==4){
     document.getElementById("ukedag").innerHTML="Torsdag"
        }
        
if(ukedag==5){
            document.getElementById("ukedag").innerHTML="Fredag"
               }
               

if(ukedag==6){
        document.getElementById("ukedag").innerHTML="Lørdag"
                   }






}

window.addEventListener("keydown", enter, false);
function enter(key){
    if(key.keyCode == "13"){
        klikk();
    
        }
}
