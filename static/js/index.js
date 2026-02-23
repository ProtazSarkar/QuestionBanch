let questions = [];   // stores all questions

function addQuestion(){
    let q = document.getElementById("questionBox").value;

    if(q.trim() === "") return;

    questions.push(q);

    // show preview
    let li = document.createElement("li");
    li.textContent = q;
    document.getElementById("preview").appendChild(li);

    document.getElementById("questionBox").value="";
}

function sendAll(){

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            questions: questions
        })
    })
    .then(res => res.json())
    .then(data => {
        alert("Server response: " + data.message);
    })
    .catch(err => console.log(err));
}