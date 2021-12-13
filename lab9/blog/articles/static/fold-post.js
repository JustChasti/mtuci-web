var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++){
    foldBtns[i].addEventListener("click", function(e) {
        if (e.target.className == "fold-button folded"){
            e.target.innerHTML = "свернуть";
            e.target.className = "fold-button";
            var displayState = "block";
            e.target.parentElement.className = "one-post";
        }
        else{
            e.target.innerHTML = "развернуть";
            e.target.className = "fold-button folded";
            var displayState = "none"
            e.target.parentElement.className = "one-post folded";
        }
    });
}