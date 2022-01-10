function validateUserName(value)
{
	
   let isValid;
   
   if(value && value.length >= 3 && value.trim())
	   
   {
       document.getElementsByClassName("erroruName")[0].style="display:none;";
	   
       isValid = true;
	   
       enableOrDisableSubmitButton(true);
	   
   }else
   {
       document.getElementsByClassName("erroruName")[0].style="display:block;";
	   
       isValid = false;
	   
       enableOrDisableSubmitButton(false);
   }
  
   return isValid;
}

function validatePassword(value)
{
	
   let isValid ;
   
   if(value && value.trim())
   {
	   
       document.getElementsByClassName("errorPass")[0].style="display:none;";
	   
       isValid = true;
	   
       enableOrDisableSubmitButton(true);
	   
   }else
   {
	   
       document.getElementsByClassName("errorPass")[0].style="display:block;";
	   
       isValid = false;
	   
       enableOrDisableSubmitButton(false);
	   
   }  
   
   return isValid;
}

function enableOrDisableSubmitButton(flag)
{
	
   if(flag)
   {
	   
       let submitBtn = document.getElementById("submitBtn");
	   
       submitBtn.disabled=false;
	   
       submitBtn.className="button button-enabled";
   }
   else
   {
	   
       let submitBtn = document.getElementById("submitBtn");
	   
       submitBtn.disabled=true;
	   
       submitBtn.className="button button-disabled";
	   
   }
}

function checkAll(val)
{
	
   let uName = document.getElementById("uName").value;
   
   let Pass = document.getElementById("Pass").value;
   
   let uNameValid = validateUsertName(uName);
   
   let PassValid = validatePassword(Pass);
   
   if(uNameValid && PassValid)
   {
	   
       enableOrDisableSubmitButton(true);
	   
   }
   else
   {
	   
       enableOrDisableSubmitButton(false);
   }
}