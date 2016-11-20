/**
 * Created by timothy on 9/18/16.
 */
function search() {
    var a = document.getElementById('search-bar');
    a.addEventListener('submit',function(e) {
        e.preventDefault();
        var b = document.getElementById('search-text').value;
        window.location.href = 'http://amazingblog.online/'+b;

    });

}

function clicked(){
    var valid = false;
    var user = document.getElementById('username');
    var pass = document.getElementById('password');

    var userList = ["timmy", "mf05"];
    var passList = ["60975", "27771"];

    for (var i=0; i < userList.length; i++){
        if (userList[i] == user.value){
            if(passList[i] == pass.value){
                valid = true;
                break;
            }
        }
    }
if (valid){window.location.href = "index.html";}
else {window.location.href = "login.html"; alert("ll");}

}

clicked();
