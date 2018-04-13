
var questionNo = 1;
showQuestion(questionNo);

function nextQuestion() {
    showQuestion(questionNo += 1);
}

function currentQuestion(n) {
    showQuestion(questionNo = n);
}

function showQuestion(n) {
    var i;
    var questions = document.getElementsByClassName('questionCard');

    if (n > questions.length || n < 1) {questionNo = 1}

    for (i = 0; i < questions.length; i++) {
        questions[i].style.display = 'none';
    }

    questions[questionNo-1].style.display = 'block';
}