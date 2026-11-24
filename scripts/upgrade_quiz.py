import os

content = """/* ==========================================================================
   ChemAI Platform - Advanced Chemistry Quiz Generator & Practice Engine
   Supports 20 Chemistry Topics, 4 Difficulty Levels, Timed / Practice / Exam Modes
   ========================================================================== */

(function initQuizEngine() {
  let questionsPool = [];
  let currentQuestions = [];
  let userAnswers = []; // records { question, selectedIndex, isCorrect }
  let currentIndex = 0;
  let score = 0;
  let selectedOption = null;
  let quizMode = "practice"; // practice, timed, exam
  let timerInterval = null;
  let timeRemaining = 20;
  let totalTimeElapsed = 0;
  let totalTimerInterval = null;

  function getBaseQuestions() {
    if (window.CHEMAI_QUIZ_QUESTIONS && Array.isArray(window.CHEMAI_QUIZ_QUESTIONS) && window.CHEMAI_QUIZ_QUESTIONS.length > 0) {
      return window.CHEMAI_QUIZ_QUESTIONS;
    }
    return [
      {
        id: "atom_1", topic: "atomic", topicName: "Atomic Structure & Periodicity",
        diff: "easy", type: "mcq",
        q: "Which quantum number specifies the three-dimensional shape of an electron orbital?",
        options: ["Principal quantum number (n)", "Azimuthal / Angular momentum quantum number (l)", "Magnetic quantum number (ml)", "Spin quantum number (ms)"],
        answer: 1, explanation: "The azimuthal quantum number (l) designates orbital shape (0=s, 1=p, 2=d, 3=f)."
      },
      {
        id: "bond_1", topic: "bonding", topicName: "Chemical Bonding & Molecular Structure",
        diff: "easy", type: "mcq",
        q: "What is the molecular geometry of a water (H2O) molecule according to VSEPR theory?",
        options: ["Linear (180 deg)", "Bent (~104.5 deg)", "Trigonal planar (120 deg)", "Tetrahedral (109.5 deg)"],
        answer: 1, explanation: "Water has two bonding pairs and two lone pairs on oxygen, compressing the bond angle to ~104.5 deg."
      }
    ];
  }

  window.startQuiz = function() {
    questionsPool = getBaseQuestions();
    const topic = document.getElementById("quizTopicSelect")?.value || "all";
    const diff = document.getElementById("quizDiffSelect")?.value || "all";
    const mode = document.getElementById("quizModeSelect")?.value || "practice";
    const count = parseInt(document.getElementById("quizCountSelect")?.value || "10", 10);
    quizMode = mode;

    let filtered = questionsPool.filter(item => {
      const matchTopic = topic === "all" || item.topic === topic;
      const matchDiff = diff === "all" || item.diff === diff;
      return matchTopic && matchDiff;
    });

    if (filtered.length === 0) {
      filtered = questionsPool;
    }

    // Shuffle
    const shuffled = [...filtered].sort(() => 0.5 - Math.random());
    currentQuestions = shuffled.slice(0, Math.min(count, shuffled.length));

    currentIndex = 0;
    score = 0;
    selectedOption = null;
    userAnswers = [];
    totalTimeElapsed = 0;

    clearInterval(timerInterval);
    clearInterval(totalTimerInterval);
    totalTimerInterval = setInterval(() => { totalTimeElapsed++; }, 1000);

    const setupPanel = document.getElementById("quizSetupPanel");
    const resultPanel = document.getElementById("quizResultPanel");
    const activePanel = document.getElementById("quizActivePanel");

    if (setupPanel) setupPanel.style.display = "none";
    if (resultPanel) resultPanel.style.display = "none";
    if (activePanel) activePanel.style.display = "block";

    const timerBadge = document.getElementById("quizTimerBadge");
    if (timerBadge) {
      timerBadge.style.display = quizMode === "timed" ? "inline-flex" : "none";
    }

    renderQuestion();
  };

  function renderQuestion() {
    clearInterval(timerInterval);
    const q = currentQuestions[currentIndex];
    selectedOption = null;

    const counter = document.getElementById("quizQuestionCounter");
    if (counter) counter.textContent = "Question " + (currentIndex + 1) + " of " + currentQuestions.length;

    const topicBadge = document.getElementById("quizQuestionTopic");
    if (topicBadge) topicBadge.textContent = q.topicName || q.topic;

    const diffBadge = document.getElementById("quizQuestionDiff");
    if (diffBadge) {
      diffBadge.textContent = (q.diff || "medium").toUpperCase();
      diffBadge.className = "chip chip-" + (q.diff === "easy" ? "emerald" : q.diff === "hard" || q.diff === "expert" ? "rose" : "cobalt");
    }

    const qText = document.getElementById("quizQuestionText");
    if (qText) qText.textContent = q.q;

    const optContainer = document.getElementById("quizOptionsContainer");
    if (optContainer) {
      optContainer.innerHTML = "";
      q.options.forEach((text, idx) => {
        const btn = document.createElement("button");
        btn.type = "button";
        btn.className = "quiz-opt-btn";
        btn.innerHTML = '<span class="opt-letter">' + String.fromCharCode(65 + idx) + '</span> <span>' + text + '</span>';
        btn.addEventListener("click", () => selectOption(idx, btn));
        optContainer.appendChild(btn);
      });
    }

    const expBox = document.getElementById("quizExplanationBox");
    if (expBox) expBox.style.display = "none";

    const nextBtn = document.getElementById("quizNextBtn");
    if (nextBtn) {
      nextBtn.textContent = currentIndex === currentQuestions.length - 1 ? "Finish Quiz" : "Next Question ->";
      nextBtn.disabled = true;
    }

    // Timed mode countdown
    if (quizMode === "timed") {
      timeRemaining = 20;
      updateTimerDisplay();
      timerInterval = setInterval(() => {
        timeRemaining--;
        updateTimerDisplay();
        if (timeRemaining <= 0) {
          clearInterval(timerInterval);
          handleTimeExpired();
        }
      }, 1000);
    }
  }

  function updateTimerDisplay() {
    const el = document.getElementById("quizTimerCount");
    if (el) {
      el.textContent = timeRemaining + "s";
      el.style.color = timeRemaining <= 5 ? "var(--color-rose)" : "var(--color-emerald)";
    }
  }

  function handleTimeExpired() {
    if (selectedOption !== null) return;
    selectOption(-1, null);
  }

  function selectOption(idx, btnElement) {
    if (selectedOption !== null) return;
    selectedOption = idx;
    clearInterval(timerInterval);

    const q = currentQuestions[currentIndex];
    const isCorrect = idx === q.answer;
    if (isCorrect) score++;

    userAnswers.push({
      question: q,
      selectedIndex: idx,
      isCorrect: isCorrect
    });

    const buttons = document.querySelectorAll(".quiz-opt-btn");
    buttons.forEach((b, i) => {
      b.disabled = true;
      if (quizMode !== "exam") {
        if (i === q.answer) b.classList.add("correct");
        else if (i === idx) b.classList.add("incorrect");
      } else {
        if (i === idx) b.classList.add("selected");
      }
    });

    if (quizMode !== "exam") {
      const expBox = document.getElementById("quizExplanationBox");
      if (expBox) {
        expBox.style.display = "block";
        if (idx === -1) {
          expBox.innerHTML = '<strong style="color:var(--color-rose);">Time expired!</strong> The correct answer was <strong>' + String.fromCharCode(65 + q.answer) + '</strong>. ' + q.explanation;
        } else {
          expBox.innerHTML = '<strong style="color:' + (isCorrect ? 'var(--color-emerald)' : 'var(--color-rose)') + ';">' + (isCorrect ? 'Correct!' : 'Incorrect.') + '</strong> ' + q.explanation;
        }
      }
    }

    const nextBtn = document.getElementById("quizNextBtn");
    if (nextBtn) nextBtn.disabled = false;
  }

  window.advanceQuizQuestion = function() {
    if (currentIndex < currentQuestions.length - 1) {
      currentIndex++;
      renderQuestion();
    } else {
      finishQuiz();
    }
  };

  function finishQuiz() {
    clearInterval(timerInterval);
    clearInterval(totalTimerInterval);

    const activePanel = document.getElementById("quizActivePanel");
    const resPanel = document.getElementById("quizResultPanel");
    if (activePanel) activePanel.style.display = "none";
    if (resPanel) resPanel.style.display = "block";

    const pct = Math.round((score / currentQuestions.length) * 100);
    const scoreDisplay = document.getElementById("quizScoreDisplay");
    if (scoreDisplay) scoreDisplay.textContent = score + " / " + currentQuestions.length + " (" + pct + "%)";

    const timeDisplay = document.getElementById("quizTimeDisplay");
    if (timeDisplay) {
      const mins = Math.floor(totalTimeElapsed / 60);
      const secs = totalTimeElapsed % 60;
      timeDisplay.textContent = (mins > 0 ? mins + "m " : "") + secs + "s";
    }

    let grade = "Proficient";
    let msg = "Good effort! Continue practicing to master advanced chemistry concepts.";
    if (pct >= 90) {
      grade = "Master Chemist";
      msg = "Spectacular mastery! You demonstrate deep conceptual grasp and calculation precision.";
    } else if (pct >= 70) {
      grade = "Advanced Scholar";
      msg = "Very strong comprehension across organic, inorganic, and physical domains.";
    } else if (pct < 50) {
      grade = "Developing Knowledge";
      msg = "Keep going! Review the study notes and formula sheets below to strengthen fundamental laws.";
    }

    const gradeBadge = document.getElementById("quizGradeBadge");
    if (gradeBadge) gradeBadge.textContent = grade;

    const feedbackMsg = document.getElementById("quizFeedbackMessage");
    if (feedbackMsg) feedbackMsg.textContent = msg;

    // Render review items
    const reviewContainer = document.getElementById("quizReviewContainer");
    if (reviewContainer) {
      reviewContainer.innerHTML = "";
      userAnswers.forEach((ans, i) => {
        const item = document.createElement("div");
        item.style.cssText = "background:var(--bg-deep);border:1px solid " + (ans.isCorrect ? "rgba(16,185,129,0.3)" : "rgba(239,68,68,0.3)") + ";border-radius:var(--radius-md);padding:1rem;margin-bottom:0.75rem;text-align:left;font-size:0.88rem;";
        const userChoice = ans.selectedIndex === -1 ? "Timed Out" : ans.question.options[ans.selectedIndex];
        const correctChoice = ans.question.options[ans.question.answer];
        item.innerHTML = '<div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;"><strong style="color:var(--text-highlight);">Q' + (i + 1) + '. ' + ans.question.q + '</strong><span class="chip ' + (ans.isCorrect ? 'chip-emerald' : 'chip-rose') + '">' + (ans.isCorrect ? 'Correct' : 'Incorrect') + '</span></div>' +
          '<div style="color:var(--text-muted);margin-bottom:0.3rem;">Your Answer: <span style="color:' + (ans.isCorrect ? 'var(--color-emerald)' : 'var(--color-rose)') + ';">' + userChoice + '</span> | Correct: <strong style="color:var(--color-emerald);">' + correctChoice + '</strong></div>' +
          '<div style="font-size:0.82rem;color:var(--text-dim);border-top:1px dashed var(--border-subtle);padding-top:0.4rem;margin-top:0.4rem;"><em>Explanation:</em> ' + ans.question.explanation + '</div>';
        reviewContainer.appendChild(item);
      });
    }
  }

  window.restartQuiz = function() {
    const resPanel = document.getElementById("quizResultPanel");
    const setupPanel = document.getElementById("quizSetupPanel");
    if (resPanel) resPanel.style.display = "none";
    if (setupPanel) setupPanel.style.display = "block";
  };

  window.toggleQuizReview = function() {
    const container = document.getElementById("quizReviewContainer");
    if (container) {
      container.style.display = container.style.display === "none" ? "block" : "none";
    }
  };
})();
"""

with open("js/quiz-engine.js", "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully generated js/quiz-engine.js")
