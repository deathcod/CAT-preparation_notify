$(document).ready(function() 
{    $("#results").click(function() {  
if (              

document.getElementById("flip1").getAttribute("value")=='0' ||            

document.getElementById("flip2").getAttribute("value")=='0' ||            

document.getElementById("flip3").getAttribute("value")=='0' ||            

document.getElementById("flip4").getAttribute("value")=='0' ||            

document.getElementById("flip5").getAttribute("value")=='0' ||            

document.getElementById("flip6").getAttribute("value")=='0' ||            

document.getElementById("flip7").getAttribute("value")=='0' ||            

document.getElementById("flip8").getAttribute("value")=='0' ||            

document.getElementById("flip9").getAttribute("value")=='0' ||            

document.getElementById("flip10").getAttribute("value")=='0'            
) {            
alert("You're not done yet!");        
}        

else {
        
var cat1name = "1";                    
        
var cat2name = "2";                    
        
var cat3name = "3";                    
        
var cat4name = "4";                    
        
var cat5name = "5";                    
        
var cat6name = "6";                    
        
var cat7name = "7";                    
        
var cat8name = "8";                    
        
var cat9name = "9";                    
        
var cat10name = "10";                    


var cat1 = ($("input[@name=q1]:checked").val() != "b"); 
           
var cat2 = ($("input[@name=q2]:checked").val() !="a");  

var cat3 = ($("input[@name=q3]:checked").val() != "c");  

var cat4 = ($("input[@name=q4]:checked").val() != "e");  

var cat5 = ($("input[@name=q5]:checked").val() != "b"); 

var cat6 = ($("input[@name=q6]:checked").val() !="c");  

var cat7 = ($("input[@name=q7]:checked").val() !="c"); 

var cat8 = ($("input[@name=q8]:checked").val() != "e");  

var cat9 = ($("input[@name=q9]:checked").val() !="c"); 

var cat10 = ($("input[@name=q10]:checked").val() != "b");  

var categories = [];                        
flag=0
if (cat1) { categories.push(cat1name);flag+=1;}            
if (cat2) { categories.push(cat2name);flag+=1;}            
if (cat3) { categories.push(cat3name); flag+=1;}            
if (cat4) { categories.push(cat4name); flag+=1;}            
if (cat5) { categories.push(cat5name); flag+=1;}            
if (cat6) { categories.push(cat6name); flag+=1;}            
if (cat7) { categories.push(cat7name); flag+=1;}            
if (cat8) { categories.push(cat8name); flag+=1;}            
if (cat9) { categories.push(cat9name); flag+=1;}            
if (cat10) { categories.push(cat10name); flag+=1;} 
flag=10-flag                  
alert('Your score ='+flag+'/'+10)
var catStr = 'You ansed the following questions incorrectly: ' + categories.join(', ') + '';                     
$("#categorylist").text(catStr);                        
$("#categorylist").show("slow");            

if (cat1) { $("#category1").show("slow"); };            
if (cat2) { $("#category2").show("slow"); };            
if (cat3) { $("#category3").show("slow"); };            
if (cat4) { $("#category4").show("slow"); };            
if (cat5) { $("#category5").show("slow"); };            
if (cat6) { $("#category6").show("slow"); };            
if (cat7) { $("#category7").show("slow"); };            
if (cat8) { $("#category8").show("slow"); };            
if (cat9) { $("#category9").show("slow"); };            
if (cat10) { $("#category10").show("slow"); };            
if (cat11) { $("#category11").show("slow"); };
{ $("#closing").show("slow"); };
}
    });});