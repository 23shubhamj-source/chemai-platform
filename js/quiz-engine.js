/* ==========================================================================
   ChemAI Platform - Chemistry Quiz Generator & Practice Engine
   ========================================================================== */

(function initQuizEngine() {
  const QUIZ_QUESTIONS = [
    {
      topic: "bonding",
      diff: "easy",
      q: "What is the molecular geometry of a water (H₂O) molecule according to VSEPR theory?",
      options: ["Linear (180°)", "Bent (~104.5°)", "Trigonal planar (120°)", "Tetrahedral (109.5°)"],
      answer: 1,
      explanation: "Water has four electron pairs around Oxygen (two bonding pairs and two lone pairs). The lone pair repulsion compresses the bond angle to ~104.5°, resulting in a bent shape."
    },
    {
      topic: "stoichiometry",
      diff: "medium",
      q: "How many moles of O₂ are required to completely combust 2 moles of propane (C₃H₈)?",
      options: ["5 moles", "7.5 moles", "10 moles", "12 moles"],
      answer: 2,
      explanation: "The balanced combustion reaction is: C₃H₈ + 5O₂ → 3CO₂ + 4H₂O. Therefore, 2 moles of C₃H₈ require 2 × 5 = 10 moles of O₂."
    },
    {
      topic: "acids",
      diff: "easy",
      q: "What is the pH of a 0.001 M HCl solution at 25°C?",
      options: ["pH = 1.0", "pH = 3.0", "pH = 7.0", "pH = 11.0"],
      answer: 1,
      explanation: "HCl is a strong monoprotic acid that dissociates completely: [H⁺] = 0.001 M = 10⁻³ M. pH = -log₁₀(10⁻³) = 3.0."
    },
    {
      topic: "thermodynamics",
      diff: "hard",
      q: "Under what conditions is a chemical reaction always spontaneous at all temperatures?",
      options: [
        "ΔH > 0 and ΔS > 0",
        "ΔH < 0 and ΔS > 0",
        "ΔH > 0 and ΔS < 0",
        "ΔH < 0 and ΔS < 0"
      ],
      answer: 1,
      explanation: "By Gibbs free energy: ΔG = ΔH - T·ΔS. When ΔH is negative (exothermic) and ΔS is positive (entropy increase), ΔG is strictly negative regardless of temperature T."
    },
    {
      topic: "organic",
      diff: "medium",
      q: "Which reagent is commonly used in organic chemistry to oxidize a primary alcohol to an aldehyde without over-oxidizing to a carboxylic acid?",
      options: [
        "KMnO₄ (Potassium permanganate)",
        "PCC (Pyridinium chlorochromate)",
        "K₂Cr₂O₇ / H₂SO₄",
        "LiAlH₄ (Lithium aluminum hydride)"
      ],
      answer: 1,
      explanation: "PCC in anhydrous dichloromethane (CH₂Cl₂) is a mild oxidizing agent that selectively stops the oxidation of primary alcohols at the aldehyde stage."
    },
    {
      topic: "periodic",
      diff: "easy",
      q: "Which element has the highest first ionization energy on the periodic table?",
      options: ["Fluorine (F)", "Helium (He)", "Cesium (Cs)", "Oxygen (O)"],
      answer: 1,
      explanation: "Helium has the highest first ionization energy (2372 kJ/mol) because its two electrons are in the 1s orbital closest to the nucleus with zero inner-shell shielding."
    }
  ];

  let currentQuestions = [];
  let currentIndex = 0;
  let score = 0;
  let selectedOption = null;

  window.startQuiz = function() {
    const topic = document.getElementById("quizTopicSelect")?.value || "all";
    const diff = document.getElementById("quizDiffSelect")?.value || "all";

    currentQuestions = QUIZ_QUESTIONS.filter((item) => {
      const matchTopic = topic === "all" || item.topic === topic;
      const matchDiff = diff === "all" || item.diff === diff;
      return matchTopic && matchDiff;
    });

    if (currentQuestions.length === 0) currentQuestions = QUIZ_QUESTIONS;

    currentIndex = 0;
    score = 0;
    selectedOption = null;

    document.getElementById("quizSetupPanel").style.display = "none";
    document.getElementById("quizResultPanel").style.display = "none";
    document.getElementById("quizActivePanel").style.display = "block";

    renderQuestion();
  };

  function renderQuestion() {
    const q = currentQuestions[currentIndex];
    selectedOption = null;

    document.getElementById("quizQuestionCounter").textContent = `Question ${currentIndex + 1} of ${currentQuestions.length}`;
    document.getElementById("quizQuestionText").textContent = q.q;

    const optContainer = document.getElementById("quizOptionsContainer");
    optContainer.innerHTML = "";

    q.options.forEach((text, idx) => {
      const btn = document.createElement("button");
      btn.className = "quiz-opt-btn";
      btn.innerHTML = `<span class="opt-letter">${String.fromCharCode(65 + idx)}</span> <span>${text}</span>`;
      btn.addEventListener("click", () => selectOption(idx, btn));
      optContainer.appendChild(btn);
    });

    const expBox = document.getElementById("quizExplanationBox");
    if (expBox) expBox.style.display = "none";

    const nextBtn = document.getElementById("quizNextBtn");
    if (nextBtn) {
      nextBtn.textContent = currentIndex === currentQuestions.length - 1 ? "Finish Quiz" : "Next Question";
      nextBtn.disabled = true;
    }
  }

  function selectOption(idx, btnElement) {
    if (selectedOption !== null) return; // Already answered
    selectedOption = idx;

    const q = currentQuestions[currentIndex];
    const isCorrect = idx === q.answer;
    if (isCorrect) score++;

    const buttons = document.querySelectorAll(".quiz-opt-btn");
    buttons.forEach((b, i) => {
      b.disabled = true;
      if (i === q.answer) b.classList.add("correct");
      else if (i === idx) b.classList.add("incorrect");
    });

    const expBox = document.getElementById("quizExplanationBox");
    if (expBox) {
      expBox.style.display = "block";
      expBox.innerHTML = `<strong>${isCorrect ? "✓ Correct!" : "✗ Incorrect."}</strong> ${q.explanation}`;
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
    document.getElementById("quizActivePanel").style.display = "none";
    const resPanel = document.getElementById("quizResultPanel");
    resPanel.style.display = "block";

    const pct = Math.round((score / currentQuestions.length) * 100);
    document.getElementById("quizScoreDisplay").textContent = `${score} / ${currentQuestions.length} (${pct}%)`;

    let msg = "Great effort! Review the study hub to master all chemistry topics.";
    if (pct >= 80) msg = "Outstanding mastery! You have a solid grasp of chemical theory and equations.";
    else if (pct >= 50) msg = "Good job! A few more practice sessions will get you to top scores.";

    document.getElementById("quizFeedbackMessage").textContent = msg;
  }

  window.restartQuiz = function() {
    document.getElementById("quizResultPanel").style.display = "none";
    document.getElementById("quizSetupPanel").style.display = "block";
  };
})();
