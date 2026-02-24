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

    if (questions.length === 0) {
        alert("Add at least one question.");
        return;
    }

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            questions: questions
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server error");
        }
        return response.json();
    })
    .then(data => {
        console.log("Server response:", data);

        if (data.status === "success") {
            // redirect to download route
            window.location.href = "/download";
        } else {
            alert(data.message || "Something went wrong");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to generate PDF");
    });
}