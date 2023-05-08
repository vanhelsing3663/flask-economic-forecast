var myInput_mail = document.getElementById("psw-mail");
var letter_mail = document.getElementById("letter-mail");


myInput_mail.onfocus = function() {
  document.getElementById("message").style.display = "block";
}


myInput_mail.onblur = function() {
  document.getElementById("message").style.display = "none";
}


myInput_mail.onkeyup = function() {


  var numbers = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  if(myInput_mail.value.match(numbers)) {
    letter_mail.classList.remove("invalid");
    letter_mail.classList.add("valid");
  } else {
    letter_mail.classList.remove("valid");
    letter_mail.classList.add("invalid");
  }


}







var myInput = document.getElementById("psw-login");
var letter = document.getElementById("letter-login");
var capital = document.getElementById("capital-login");
var number = document.getElementById("number-login");
var length = document.getElementById("length-login");


myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}


myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}


myInput.onkeyup = function() {

  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
}


  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }


  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }


  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}







